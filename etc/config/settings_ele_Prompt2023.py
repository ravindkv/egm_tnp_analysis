#############################################################
########## General settings
#############################################################
# flag to be Tested
cutpass80 = '(( abs(probe_sc_eta) < 0.8 && probe_Ele_nonTrigMVA > %f ) ||  ( abs(probe_sc_eta) > 0.8 && abs(probe_sc_eta) < 1.479&& probe_Ele_nonTrigMVA > %f ) || ( abs(probe_sc_eta) > 1.479 && probe_Ele_nonTrigMVA > %f ) )' % (0.967083,0.929117,0.726311)
cutpass90 = '(( abs(probe_sc_eta) < 0.8 && probe_Ele_nonTrigMVA > %f ) ||  ( abs(probe_sc_eta) > 0.8 && abs(probe_sc_eta) < 1.479&& probe_Ele_nonTrigMVA > %f ) || ( abs(probe_sc_eta) > 1.479 && probe_Ele_nonTrigMVA > %f ) )' % (0.913286,0.805013,0.358969)

# flag to be Tested

flags = {
'passHLTEG30L1SingleEGOrEtFilter' : ('passHLTEG30L1SingleEGOrEtFilter==1'),
'passHLTEle30WPTightClusterShapeFilter' : ('passHLTEle30WPTightClusterShapeFilter==1'),
'passHLTEle30WPTightHEFilter' : ('passHLTEle30WPTightHEFilter==1'),
'passHLTEle30WPTightEcalIsoFilter' : ('passHLTEle30WPTightEcalIsoFilter==1'),
'passHLTEle30WPTightHcalIsoFilter' : ('passHLTEle30WPTightHcalIsoFilter==1'),
'passHLTEle30WPTightPixelMatchFilter' : ('passHLTEle30WPTightPixelMatchFilter==1'),
'passHLTEle30WPTightPMS2Filter' : ('passHLTEle30WPTightPMS2Filter==1'),
'passHLTEle30WPTightGsfOneOEMinusOneOPFilter' : ('passHLTEle30WPTightGsfOneOEMinusOneOPFilter==1'),
'passHLTEle30WPTightGsfMissingHitsFilter' : ('passHLTEle30WPTightGsfMissingHitsFilter==1'),
'passHLTEle30WPTightGsfDetaFilter' : ('passHLTEle30WPTightGsfDetaFilter==1'),
'passHLTEle30WPTightGsfDphiFilter' : ('passHLTEle30WPTightGsfDphiFilter==1'),
'passHLTEle30WPTightGsfTrackIsoFilter' : ('passHLTEle30WPTightGsfTrackIsoFilter==1'),
'passHLTEGL1SingleEGNonIsoOrWithJetAndTauFilter' : ('passHLTEGL1SingleEGNonIsoOrWithJetAndTauFilter==1'),
'passHLTEG115EtFilter' : ('passHLTEG115EtFilter==1'),
'passHLTEG115CaloIdVTClusterShapeFilter' : ('passHLTEG115CaloIdVTClusterShapeFilter==1'),
'passHLTEG115CaloIdVTHEFilter' : ('passHLTEG115CaloIdVTHEFilter==1'),
'passHLTEle115CaloIdVTPixelMatchFilter' : ('passHLTEle115CaloIdVTPixelMatchFilter==1'),
'passHLTEle115CaloIdVTGsfTrkIdTGsfDetaFilter' : ('passHLTEle115CaloIdVTGsfTrkIdTGsfDetaFilter==1'),
'passHLTEle115CaloIdVTGsfTrkIdTGsfDphiFilter' : ('passHLTEle115CaloIdVTGsfTrkIdTGsfDphiFilter==1'),
'passHLTEGL1SingleAndDoubleEGOrPairFilter' : ('passHLTEGL1SingleAndDoubleEGOrPairFilter==1'),
'passHLTEle23Ele12CaloIdLTrackIdLIsoVLEtLeg1Filter' : ('passHLTEle23Ele12CaloIdLTrackIdLIsoVLEtLeg1Filter==1'),
'passHLTEle23Ele12CaloIdLTrackIdLIsoVLEtLeg2Filter' : ('passHLTEle23Ele12CaloIdLTrackIdLIsoVLEtLeg2Filter==1'),
'passHLTEle23Ele12CaloIdLTrackIdLIsoVLClusterShapeLeg1Filter' : ('passHLTEle23Ele12CaloIdLTrackIdLIsoVLClusterShapeLeg1Filter==1'),
'passHLTEle23Ele12CaloIdLTrackIdLIsoVLClusterShapeLeg2Filter' : ('passHLTEle23Ele12CaloIdLTrackIdLIsoVLClusterShapeLeg2Filter==1'),
'passHLTEle23Ele12CaloIdLTrackIdLIsoVLHELeg1Filter' : ('passHLTEle23Ele12CaloIdLTrackIdLIsoVLHELeg1Filter==1'),
'passHLTEle23Ele12CaloIdLTrackIdLIsoVLHELeg2Filter' : ('passHLTEle23Ele12CaloIdLTrackIdLIsoVLHELeg2Filter==1'),
'passHLTEle23Ele12CaloIdLTrackIdLIsoVLEcalIsoLeg1Filter' : ('passHLTEle23Ele12CaloIdLTrackIdLIsoVLEcalIsoLeg1Filter==1'),
'passHLTEle23Ele12CaloIdLTrackIdLIsoVLEcalIsoLeg2Filter' : ('passHLTEle23Ele12CaloIdLTrackIdLIsoVLEcalIsoLeg2Filter==1'),
'passHLTEle23Ele12CaloIdLTrackIdLIsoVLHcalIsoLeg1Filter' : ('passHLTEle23Ele12CaloIdLTrackIdLIsoVLHcalIsoLeg1Filter==1'),
'passHLTEle23Ele12CaloIdLTrackIdLIsoVLHcalIsoLeg2Filter' : ('passHLTEle23Ele12CaloIdLTrackIdLIsoVLHcalIsoLeg2Filter==1'),
'passHLTEle23Ele12CaloIdLTrackIdLIsoVLPixelMatchLeg1Filter' : ('passHLTEle23Ele12CaloIdLTrackIdLIsoVLPixelMatchLeg1Filter==1'),
'passHLTEle23Ele12CaloIdLTrackIdLIsoVLPixelMatchLeg2Filter' : ('passHLTEle23Ele12CaloIdLTrackIdLIsoVLPixelMatchLeg2Filter==1'),
'passHLTEle23Ele12CaloIdLTrackIdLIsoVLOneOEMinusOneOPLeg1Filter' : ('passHLTEle23Ele12CaloIdLTrackIdLIsoVLOneOEMinusOneOPLeg1Filter==1'),
'passHLTEle23Ele12CaloIdLTrackIdLIsoVLOneOEMinusOneOPLeg2Filter' : ('passHLTEle23Ele12CaloIdLTrackIdLIsoVLOneOEMinusOneOPLeg2Filter==1'),
'passHLTEle23Ele12CaloIdLTrackIdLIsoVLDetaLeg1Filter' : ('passHLTEle23Ele12CaloIdLTrackIdLIsoVLDetaLeg1Filter==1'),
'passHLTEle23Ele12CaloIdLTrackIdLIsoVLDetaLeg2Filter' : ('passHLTEle23Ele12CaloIdLTrackIdLIsoVLDetaLeg2Filter==1'),
'passHLTEle23Ele12CaloIdLTrackIdLIsoVLDphiLeg1Filter' : ('passHLTEle23Ele12CaloIdLTrackIdLIsoVLDphiLeg1Filter==1'),
'passHLTEle23Ele12CaloIdLTrackIdLIsoVLDphiLeg2Filter' : ('passHLTEle23Ele12CaloIdLTrackIdLIsoVLDphiLeg2Filter==1'),
'passHLTEle23Ele12CaloIdLTrackIdLIsoVLTrackIsoLeg1Filter' : ('passHLTEle23Ele12CaloIdLTrackIdLIsoVLTrackIsoLeg1Filter==1'),
'passHLTEle23Ele12CaloIdLTrackIdLIsoVLTrackIsoLeg2Filter' : ('passHLTEle23Ele12CaloIdLTrackIdLIsoVLTrackIsoLeg2Filter==1'),
'passHLTEGL1SingleAndDoubleEGNonIsoOrWithEG26WithJetAndTauFilter' : ('passHLTEGL1SingleAndDoubleEGNonIsoOrWithEG26WithJetAndTauFilter==1'),
'passHLTEG33EtFilter' : ('passHLTEG33EtFilter==1'),
'passHLTEG33HEFilter' : ('passHLTEG33HEFilter==1'),
'passHLTEG33CaloIdLClusterShapeFilter' : ('passHLTEG33CaloIdLClusterShapeFilter==1'),
'passHLTEle33CaloIdLPixelMatchFilter' : ('passHLTEle33CaloIdLPixelMatchFilter==1'),
'passHLTDiEG33EtUnseededFilter' : ('passHLTDiEG33EtUnseededFilter==1'),
'passHLTDiEG33HEUnseededFilter' : ('passHLTDiEG33HEUnseededFilter==1'),
'passHLTDiEG33CaloIdLClusterShapeUnseededFilter' : ('passHLTDiEG33CaloIdLClusterShapeUnseededFilter==1'),
'passHLTDiEle33CaloIdLPixelMatchUnseededFilter' : ('passHLTDiEle33CaloIdLPixelMatchUnseededFilter==1'),
}
baseOutDir = 'results/Prompt2023D/tnpEleTrig/'

#############################################################
########## samples definition  - preparing the samples
#############################################################
### samples are defined in etc/inputs/tnpSampleDef.py
### not: you can setup another sampleDef File in inputs
import etc.inputs.tnpSampleDef as tnpSamples
tnpTreeDir = 'tnpEleTrig'

samplesDef = {
    'data'   : tnpSamples.Prompt2023['data_Run2023D'].clone(),
    'mcNom'  : tnpSamples.Prompt2022['DY_amcatnloext'].clone(),
}

## can add data sample easily
#samplesDef['data'].add_sample( tnpSamples.Prompt2022['data_Run2022G'] )
#samplesDef['data'].add_sample( tnpSamples.Prompt2022['data_Run2022C'] )

#samplesDef['data'  ].set_cut('run >= 273726')
samplesDef['data' ].set_tnpTree(tnpTreeDir)
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_tnpTree(tnpTreeDir)
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_mcTruth()

## set MC weight, can use several pileup rw for different data taking periods
weightName = 'weights_2017_runBCDEF.totWeight'
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_weight(weightName)
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_puTree('/eos/cms/store/group/phys_egamma/swmukher/UL2017/PU_miniAOD/DY_amcatnloext_ele.pu.puTree.root')


#############################################################
########## bining definition  [can be nD bining]
#############################################################
phibins = [
        -3.32,
        -2.97,
        -2.62,
        -2.27,
        -1.92,
        -1.57,
        -1.22,
        -0.87,
        -0.52,
        -0.18,
        0.18,
        0.52,
        0.87,
        1.22,
        1.57,
        1.92,
        2.27,
        2.62,
        2.97,
        3.32
    ]
biningDef = [
  { 'var' : 'el_phi' , 'type': 'float', 'bins':phibins},
  #{ 'var' : 'el_phi' , 'type': 'float', 'bins':[ -3.0,-2.0,-1.566, -1.0, 0.0, 1.0, 1.566, 2.0, 3.0]},
  #{ 'var' : 'el_eta' , 'type': 'float', 'bins':[-2.5,-2.0,-1.566,-1.4442, -0.8, 0.0, 0.8, 1.4442, 1.566, 2.0, 2.5] },
   #{ 'var' : 'el_pt' , 'type': 'float', 'bins':[10,20,35,50,100,200,500]} 
   #{ 'var' : 'el_pt' , 'type': 'float', 'bins':[10,35,100,500]} 
   { 'var' : 'el_pt' , 'type': 'float', 'bins':[10,100,500]} 
   #{ 'var' : 'el_eta' , 'type': 'float', 'bins':[-2.5,-1.566,0.0,1.556,2.5]} 
]
#############################################################
########## Cuts definition for all samples
#############################################################
cutBase   = 'tag_Ele_pt > 35 && abs(tag_sc_eta) < 2.17 && el_q*tag_Ele_q < 0 && passingCutBasedTight122XV1==1'

additionalCuts = { 
    0 : 'tag_Ele_trigMVA > 0.92 ',
    1 : 'tag_Ele_trigMVA > 0.92 ',
    2 : 'tag_Ele_trigMVA > 0.92 ',
    3 : 'tag_Ele_trigMVA > 0.92 ',
    4 : 'tag_Ele_trigMVA > 0.92 ',
    5 : 'tag_Ele_trigMVA > 0.92 ',
    6 : 'tag_Ele_trigMVA > 0.92 ',
    7 : 'tag_Ele_trigMVA > 0.92 ',
    8 : 'tag_Ele_trigMVA > 0.92 ',
    9 : 'tag_Ele_trigMVA > 0.92 '
}

#### or remove any additional cut (default)
additionalCuts = None

#############################################################
########## fitting params to tune fit by hand if necessary
#############################################################
tnpParNomFit = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[0.9,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[0.9,0.5,5.0]",
    "acmsP[60.,50.,80.]","betaP[0.05,0.01,0.08]","gammaP[0.1, -2, 2]","peakP[90.0]",
    "acmsF[60.,50.,80.]","betaF[0.05,0.01,0.08]","gammaF[0.1, -2, 2]","peakF[90.0]",
    ]
