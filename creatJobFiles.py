import os
import sys
import itertools
sys.dont_write_bytecode = True
import FWCore.ParameterSet.Config as cms


ele30_allFilters = {'passHLTEG30L1SingleEGOrEtFilter': cms.vstring('hltEG30L1SingleEGOrEtFilter'), 'passHLTEle30WPTightClusterShapeFilter': cms.vstring('hltEle30WPTightClusterShapeFilter'), 'passHLTEle30WPTightHEFilter': cms.vstring('hltEle30WPTightHEFilter'), 'passHLTEle30WPTightEcalIsoFilter': cms.vstring('hltEle30WPTightEcalIsoFilter'), 'passHLTEle30WPTightHcalIsoFilter': cms.vstring('hltEle30WPTightHcalIsoFilter'), 'passHLTEle30WPTightPixelMatchFilter': cms.vstring('hltEle30WPTightPixelMatchFilter'), 'passHLTEle30WPTightPMS2Filter': cms.vstring('hltEle30WPTightPMS2Filter'), 'passHLTEle30WPTightGsfOneOEMinusOneOPFilter': cms.vstring('hltEle30WPTightGsfOneOEMinusOneOPFilter'), 'passHLTEle30WPTightGsfMissingHitsFilter': cms.vstring('hltEle30WPTightGsfMissingHitsFilter'), 'passHLTEle30WPTightGsfDetaFilter': cms.vstring('hltEle30WPTightGsfDetaFilter'), 'passHLTEle30WPTightGsfDphiFilter': cms.vstring('hltEle30WPTightGsfDphiFilter'), 'passHLTEle30WPTightGsfTrackIsoFilter': cms.vstring('hltEle30WPTightGsfTrackIsoFilter')}

ele115_allFilters = {'passHLTEGL1SingleEGNonIsoOrWithJetAndTauFilter': cms.vstring('hltEGL1SingleEGNonIsoOrWithJetAndTauFilter'), 'passHLTEG115EtFilter': cms.vstring('hltEG115EtFilter'), 'passHLTEG115CaloIdVTClusterShapeFilter': cms.vstring('hltEG115CaloIdVTClusterShapeFilter'), 'passHLTEG115CaloIdVTHEFilter': cms.vstring('hltEG115CaloIdVTHEFilter'), 'passHLTEle115CaloIdVTPixelMatchFilter': cms.vstring('hltEle115CaloIdVTPixelMatchFilter'), 'passHLTEle115CaloIdVTGsfTrkIdTGsfDetaFilter': cms.vstring('hltEle115CaloIdVTGsfTrkIdTGsfDetaFilter'), 'passHLTEle115CaloIdVTGsfTrkIdTGsfDphiFilter': cms.vstring('hltEle115CaloIdVTGsfTrkIdTGsfDphiFilter')}

ele23ele12_allFilters = {'passHLTEGL1SingleAndDoubleEGOrPairFilter': cms.vstring('hltEGL1SingleAndDoubleEGOrPairFilter'), 'passHLTEle23Ele12CaloIdLTrackIdLIsoVLEtLeg1Filter': cms.vstring('hltEle23Ele12CaloIdLTrackIdLIsoVLEtLeg1Filter'), 'passHLTEle23Ele12CaloIdLTrackIdLIsoVLEtLeg2Filter': cms.vstring('hltEle23Ele12CaloIdLTrackIdLIsoVLEtLeg2Filter'), 'passHLTEle23Ele12CaloIdLTrackIdLIsoVLClusterShapeLeg1Filter': cms.vstring('hltEle23Ele12CaloIdLTrackIdLIsoVLClusterShapeLeg1Filter'), 'passHLTEle23Ele12CaloIdLTrackIdLIsoVLClusterShapeLeg2Filter': cms.vstring('hltEle23Ele12CaloIdLTrackIdLIsoVLClusterShapeLeg2Filter'), 'passHLTEle23Ele12CaloIdLTrackIdLIsoVLHELeg1Filter': cms.vstring('hltEle23Ele12CaloIdLTrackIdLIsoVLHELeg1Filter'), 'passHLTEle23Ele12CaloIdLTrackIdLIsoVLHELeg2Filter': cms.vstring('hltEle23Ele12CaloIdLTrackIdLIsoVLHELeg2Filter'), 'passHLTEle23Ele12CaloIdLTrackIdLIsoVLEcalIsoLeg1Filter': cms.vstring('hltEle23Ele12CaloIdLTrackIdLIsoVLEcalIsoLeg1Filter'), 'passHLTEle23Ele12CaloIdLTrackIdLIsoVLEcalIsoLeg2Filter': cms.vstring('hltEle23Ele12CaloIdLTrackIdLIsoVLEcalIsoLeg2Filter'), 'passHLTEle23Ele12CaloIdLTrackIdLIsoVLHcalIsoLeg1Filter': cms.vstring('hltEle23Ele12CaloIdLTrackIdLIsoVLHcalIsoLeg1Filter'), 'passHLTEle23Ele12CaloIdLTrackIdLIsoVLHcalIsoLeg2Filter': cms.vstring('hltEle23Ele12CaloIdLTrackIdLIsoVLHcalIsoLeg2Filter'), 'passHLTEle23Ele12CaloIdLTrackIdLIsoVLPixelMatchLeg1Filter': cms.vstring('hltEle23Ele12CaloIdLTrackIdLIsoVLPixelMatchLeg1Filter'), 'passHLTEle23Ele12CaloIdLTrackIdLIsoVLPixelMatchLeg2Filter': cms.vstring('hltEle23Ele12CaloIdLTrackIdLIsoVLPixelMatchLeg2Filter'), 'passHLTEle23Ele12CaloIdLTrackIdLIsoVLOneOEMinusOneOPLeg1Filter': cms.vstring('hltEle23Ele12CaloIdLTrackIdLIsoVLOneOEMinusOneOPLeg1Filter'), 'passHLTEle23Ele12CaloIdLTrackIdLIsoVLOneOEMinusOneOPLeg2Filter': cms.vstring('hltEle23Ele12CaloIdLTrackIdLIsoVLOneOEMinusOneOPLeg2Filter'), 'passHLTEle23Ele12CaloIdLTrackIdLIsoVLDetaLeg1Filter': cms.vstring('hltEle23Ele12CaloIdLTrackIdLIsoVLDetaLeg1Filter'), 'passHLTEle23Ele12CaloIdLTrackIdLIsoVLDetaLeg2Filter': cms.vstring('hltEle23Ele12CaloIdLTrackIdLIsoVLDetaLeg2Filter'), 'passHLTEle23Ele12CaloIdLTrackIdLIsoVLDphiLeg1Filter': cms.vstring('hltEle23Ele12CaloIdLTrackIdLIsoVLDphiLeg1Filter'), 'passHLTEle23Ele12CaloIdLTrackIdLIsoVLDphiLeg2Filter': cms.vstring('hltEle23Ele12CaloIdLTrackIdLIsoVLDphiLeg2Filter'), 'passHLTEle23Ele12CaloIdLTrackIdLIsoVLTrackIsoLeg1Filter': cms.vstring('hltEle23Ele12CaloIdLTrackIdLIsoVLTrackIsoLeg1Filter'), 'passHLTEle23Ele12CaloIdLTrackIdLIsoVLTrackIsoLeg2Filter': cms.vstring('hltEle23Ele12CaloIdLTrackIdLIsoVLTrackIsoLeg2Filter')}

doubleEle33_leg1_allFilters = {'passHLTEGL1SingleAndDoubleEGNonIsoOrWithEG26WithJetAndTauFilter': cms.vstring('hltEGL1SingleAndDoubleEGNonIsoOrWithEG26WithJetAndTauFilter'), 'passHLTEG33EtFilter': cms.vstring('hltEG33EtFilter'), 'passHLTEG33HEFilter': cms.vstring('hltEG33HEFilter'), 'passHLTEG33CaloIdLClusterShapeFilter': cms.vstring('hltEG33CaloIdLClusterShapeFilter'), 'passHLTEle33CaloIdLPixelMatchFilter': cms.vstring('hltEle33CaloIdLPixelMatchFilter')}

doubleEle33_leg2_allFilters = {'passHLTDiEG33EtUnseededFilter': cms.vstring('hltDiEG33EtUnseededFilter'), 'passHLTDiEG33HEUnseededFilter': cms.vstring('hltDiEG33HEUnseededFilter'), 'passHLTDiEG33CaloIdLClusterShapeUnseededFilter': cms.vstring('hltDiEG33CaloIdLClusterShapeUnseededFilter'), 'passHLTDiEle33CaloIdLPixelMatchUnseededFilter': cms.vstring('hltDiEle33CaloIdLPixelMatchUnseededFilter')}

allFilters = {}
allFilters.update(ele30_allFilters) 
allFilters.update(ele115_allFilters)
allFilters.update(ele23ele12_allFilters)
allFilters.update(doubleEle33_leg1_allFilters)
allFilters.update(doubleEle33_leg2_allFilters)

if __name__ == "__main__":
    #---------------------------
    # Create tar file
    #---------------------------
    if os.path.exists("tmpSub"):
        os.system("rm -r tmpSub")
        print("Deleted dir: tmpSub")
    os.system("mkdir -p tmpSub/log")
    print("Created dir: tmpSub")
    condorLogDir = "log"
    cmssw_base = os.environ.get("CMSSW_BASE")
    cmssw_version = cmssw_base.split('/')[-1].strip()
    tarFile = "tmpSub/egm_tnp_analysis.tar.gz"
    os.system("tar --exclude-tag-under=FILE -zcvf %s ../egm_tnp_analysis --exclude results --exclude .git"%(tarFile))

    #---------------------------
    # Create executable file 
    #---------------------------
    shFile = open("tmpSub/tnpEGM_fitter.sh", 'w')
    shFile.write('#!/bin/bash\n')
    shFile.write('printf "Start Running TnP at ";/bin/date\n')
    shFile.write('echo ${_CONDOR_SCRATCH_DIR}\n')
    shFile.write('source /cvmfs/cms.cern.ch/cmsset_default.sh\n')
    shFile.write('export SCRAM_ARCH=slc7_amd64_gcc700\n')
    shFile.write('scramv1 project CMSSW %s\n'%cmssw_version)
    shFile.write('cd %s/src\n'%cmssw_version)
    shFile.write('eval `scramv1 runtime -sh`\n')
    shFile.write('cd ../..\n')
    shFile.write('tar --strip-components=1 -zxf egm_tnp_analysis.tar.gz\n')
    shFile.write('echo $1\n')
    shFile.write('python2.7 tnpEGM_fitter.py etc/config/settings_ele_Prompt2023.py  --flag $1 --createBins\n')
    shFile.write('python2.7 tnpEGM_fitter.py etc/config/settings_ele_Prompt2023.py  --flag $1 --createHists\n')
    shFile.write('python2.7 tnpEGM_fitter.py etc/config/settings_ele_Prompt2023.py  --flag $1 --doFit\n')
    shFile.write('python2.7 tnpEGM_fitter.py etc/config/settings_ele_Prompt2023.py  --flag $1 --sumUp\n')
    shFile.write('printf "Done at ";/bin/date\n')
    shFile.write('xrdcp -f results/Prompt2023D/tnpEleTrig/$1//eff_$1*.pdf %s/src/egm_tnp_analysis/results'%cmssw_base)

    #---------------------------
    # Create job files 
    #---------------------------
    os.system("cp /tmp/x509up_u93032 tmpSub")
    jdlName = 'submitJobs.jdl'
    jdlFile = open('tmpSub/%s'%jdlName,'w')
    jdlFile.write('Executable =  tnpEGM_fitter.sh \n')
    common_command = \
    'Universe   = vanilla\n\
    should_transfer_files = YES\n\
    when_to_transfer_output = ON_EXIT\n\
    Transfer_Input_Files = egm_tnp_analysis.tar.gz, tnpEGM_fitter.sh\n\
    x509userproxy        = x509up_u93032\n\
    +JobFlavour = \'workday\'\n\
    Output = %s/log_$(cluster)_$(process).stdout\n\
    Error  = %s/log_$(cluster)_$(process).stderr\n\
    Log  = %s/log_$(cluster)_$(process).condor\n\n'%(condorLogDir, condorLogDir, condorLogDir)
    jdlFile.write(common_command)

    for filt in allFilters.keys(): 
        args =  'Arguments  = %s\n' %filt
        args += "Queue 1\n\n"
        jdlFile.write(args)
    jdlFile.close() 

    print('\ncd tmpSub && condor_submit submitJobs.jdl\n')
