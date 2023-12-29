
### python specific import
import argparse
import os
import sys
import pickle
import shutil
from multiprocessing import Pool


parser = argparse.ArgumentParser(description='tnp EGM fitter')
parser.add_argument('--checkBins'  , action='store_true'  , help = 'check  bining definition')
parser.add_argument('--createBins' , action='store_true'  , help = 'create bining definition')
parser.add_argument('--createHists', action='store_true'  , help = 'create histograms')
parser.add_argument('--sample'     , default='all'        , help = 'create histograms (per sample, expert only)')
parser.add_argument('--doFit'      , action='store_true'  , help = 'fit sample (sample should be defined in settings.py)')
parser.add_argument('--doPlot'     , action='store_true'  , help = 'plotting')
parser.add_argument('--sumUp'      , action='store_true'  , help = 'sum up efficiencies')
parser.add_argument('--iBin'       , dest = 'binNumber'   , type = int,  default=-1, help='bin number (to refit individual bin)')
parser.add_argument('--flag'       , default = None       , help ='WP to test')
parser.add_argument('settings'     , default = None       , help = 'setting file [mandatory]')


args = parser.parse_args()

print '===> settings %s <===' % args.settings
importSetting = 'import %s as tnpConf' % args.settings.replace('/','.').split('.py')[0]
print importSetting
exec(importSetting)

### tnp library
import libPython.binUtils  as tnpBiner
import libPython.rootUtils as tnpRoot


if args.flag is None:
    print '[tnpEGM_fitter] flag is MANDATORY, this is the working point as defined in the settings.py'
    sys.exit(0)
    
if not args.flag in tnpConf.flags.keys() :
    print '[tnpEGM_fitter] flag %s not found in flags definitions' % args.flag
    print '  --> define in settings first'
    print '  In settings I found flags: '
    print tnpConf.flags.keys()
    sys.exit(1)

outputDirectory = '%s/%s/' % (tnpConf.baseOutDir,args.flag)

print '===>  Output directory: '
print outputDirectory


####################################################################
##### Create (check) Bins
####################################################################
if args.checkBins:
    tnpBins = tnpBiner.createBins(tnpConf.biningDef,tnpConf.cutBase)
    tnpBiner.tuneCuts( tnpBins, tnpConf.additionalCuts )
    for ib in range(len(tnpBins['bins'])):
        print tnpBins['bins'][ib]['name']
        print '  - cut: ',tnpBins['bins'][ib]['cut']
    sys.exit(0)
    
if args.createBins:
    if os.path.exists( outputDirectory ):
            shutil.rmtree( outputDirectory )
    os.makedirs( outputDirectory )
    tnpBins = tnpBiner.createBins(tnpConf.biningDef,tnpConf.cutBase)
    tnpBiner.tuneCuts( tnpBins, tnpConf.additionalCuts )
    pickle.dump( tnpBins, open( '%s/bining.pkl'%(outputDirectory),'wb') )
    print 'created dir: %s ' % outputDirectory
    print 'bining created successfully... '
    print 'Note than any additional call to createBins will overwrite directory %s' % outputDirectory
    sys.exit(0)

tnpBins = pickle.load( open( '%s/bining.pkl'%(outputDirectory),'rb') )


####################################################################
##### Create Histograms
####################################################################
sampleMC = tnpConf.samplesDef['mcNom']

if sampleMC is None:
    print '[tnpEGM_fitter, prelim checks]: MC sample not available... check your settings'
    sys.exit(1)
for s in tnpConf.samplesDef.keys():
    sample =  tnpConf.samplesDef[s]
    if sample is None: continue
    setattr( sample, 'mcRef'     , sampleMC )
    setattr( sample, 'tree'     ,'%s/fitter_tree' % tnpConf.tnpTreeDir )
    setattr( sample, 'histFile' , '%s/%s_%s.root' % ( outputDirectory , sample.name, args.flag ) )


if args.createHists:

    import libPython.histUtils as tnpHist

    def parallel_hists(sampleType):
        sample =  tnpConf.samplesDef[sampleType]
        if sample is None : return
        if sampleType == args.sample or args.sample == 'all' :
            print 'creating histogram for sample '
            sample.dump()
            var = { 'name' : 'pair_mass', 'nbins' : 80, 'min' : 50, 'max': 130 }
            tnpHist.makePassFailHistograms( sample, tnpConf.flags[args.flag], tnpBins, var )
    
    pool = Pool()
    pool.map(parallel_hists, tnpConf.samplesDef.keys())

    sys.exit(0)


####################################################################
##### Actual Fitter
####################################################################
sampleToFit = tnpConf.samplesDef['data']
if sampleToFit is None:
    print '[tnpEGM_fitter, prelim checks]: sample (data) not available... check your settings'
    sys.exit(1)

for s in tnpConf.samplesDef.keys():
    sample =  tnpConf.samplesDef[s]
    if sample is None: continue
    setattr( sample, 'nominalFit', '%s/%s_%s.nominalFit.root' % ( outputDirectory , sample.name, args.flag ) )

if  args.doFit:
    sampleToFit.dump()
    def parallel_fit(ib):
        if (args.binNumber >= 0 and ib == args.binNumber) or args.binNumber < 0:
            tnpRoot.histFitterNominal( sampleToFit, tnpBins['bins'][ib], tnpConf.tnpParNomFit )
    pool = Pool()
    pool.map(parallel_fit, range(len(tnpBins['bins'])))

    args.doPlot = True
     
####################################################################
##### dumping plots
####################################################################
if  args.doPlot:
    fileName = sampleToFit.nominalFit
    fitType  = 'nominalFit'
    os.system('hadd -f %s %s' % (fileName, fileName.replace('.root', '-*.root')))

    plottingDir = '%s/plots/%s/%s' % (outputDirectory,sampleToFit.name,fitType)
    if not os.path.exists( plottingDir ):
        os.makedirs( plottingDir )
    shutil.copy('etc/inputs/index.php.listPlots','%s/index.php' % plottingDir)

    for ib in range(len(tnpBins['bins'])):
        if (args.binNumber >= 0 and ib == args.binNumber) or args.binNumber < 0:
            tnpRoot.histPlotter( fileName, tnpBins['bins'][ib], plottingDir )

    print ' ===> Plots saved in <======='
#    print 'localhost/%s/' % plottingDir


####################################################################
##### dumping egamma txt file 
####################################################################
if args.sumUp:
    sampleToFit.dump()
    info = {
        'data'        : sampleToFit.histFile,
        'dataNominal' : sampleToFit.nominalFit,
        'mcNominal'   : sampleToFit.mcRef.histFile,
        }

    effis = None
    effFileName ='%s/egammaEffi.txt' % outputDirectory 
    fOut = open( effFileName,'w')
    
    for ib in range(len(tnpBins['bins'])):
        effis = tnpRoot.getAllEffi( info, tnpBins['bins'][ib] )

        ### formatting assuming 2D bining -- to be fixed        
        v1Range = tnpBins['bins'][ib]['title'].split(';')[1].split('<')
        v2Range = tnpBins['bins'][ib]['title'].split(';')[2].split('<')
        if ib == 0 :
            astr = '### var1 : %s' % v1Range[1]
            print astr
            fOut.write( astr + '\n' )
            astr = '### var2 : %s' % v2Range[1]
            print astr
            fOut.write( astr + '\n' )
            
        astr =  '%+8.5f\t%+8.5f\t%+8.5f\t%+8.5f\t%5.5f\t%5.5f' % (
            float(v1Range[0]), float(v1Range[2]),
            float(v2Range[0]), float(v2Range[2]),
            effis['dataNominal'][0],effis['dataNominal'][1],
            )
        print astr
        fOut.write( astr + '\n' )
    fOut.close()

    print 'Effis saved in file : ',  effFileName
    import libPython.EGammaID_scaleFactors as egm_sf
    egm_sf.doEGM_SFs(effFileName,sampleToFit.lumi)
