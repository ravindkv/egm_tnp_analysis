from libPython.tnpClassUtils import tnpSample

eos2022 = '/eos/cms/store/group/phys_egamma/tnpTuples/rverma/2023-12-05/2022/'
Prompt2022 = {
    'DY_amcatnloext' : tnpSample('DY_amcatnloext' , eos2022 + "DY_NLO_preEE.root" , isMC = True, nEvts =  -1),
    'data_Run2022C' : tnpSample('data_Run2022C'   , eos2022 + "data_EGamma_Run2022C.root" , lumi = 14.02672485),
    'data_Run2022D' : tnpSample('data_Run2022D'   , eos2022 + "data_EGamma_Run2022D.root" , lumi = 14.02672485),
    'data_Run2022E' : tnpSample('data_Run2022E'   , eos2022 + "data_EGamma_Run2022E.root" , lumi = 14.02672485),
    'data_Run2022F' : tnpSample('data_Run2022F'   , eos2022 + 'data_EGamma_Run2022F.root' , lumi = 14.02672485),
    'data_Run2022G' : tnpSample('data_Run2022G'   , eos2022 + 'data_EGamma_Run2022G.root' , lumi = 7.060617355),
}

eos2023 = '/eos/cms/store/group/phys_egamma/tnpTuples/rverma/2023-12-05/2023/'
Prompt2023 = {
    'DY_amcatnloext' : tnpSample('DY_amcatnloext' , eos2022 + "DY_NLO_preEE.root" , isMC = True, nEvts =  -1),
    'data_Run2023B' : tnpSample('data_Run2023B'   , eos2023 + "data_EGamma_Run2023B.root" , lumi = 14.02672485),
    'data_Run2023C' : tnpSample('data_Run2023C'   , eos2023 + "data_EGamma_Run2023C.root" , lumi = 14.02672485),
    'data_Run2023D' : tnpSample('data_Run2023D'   , eos2023 + "data_EGamma_Run2023D.root" , lumi = 14.02672485),
}

