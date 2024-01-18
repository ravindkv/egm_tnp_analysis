# Install stable branch
```bash
cmsrel CMSSW_11_2_0
cd CMSSW_11_2_0/src
cmsenv
git clone git@github.com:ravindkv/egm_tnp_analysis.git 
cd egm_tnp_analysis
make 
```
For 2022: DoubleEle_23_12_Leg1
 * python2.7 tnpEGM_fitter.py etc/config/settings_ele_Prompt2022.py  --flag passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg1L1match --createBins
 * python2.7 tnpEGM_fitter.py etc/config/settings_ele_Prompt2022.py  --flag passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg1L1match --createHists
 * python2.7 tnpEGM_fitter.py etc/config/settings_ele_Prompt2022.py  --flag passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg1L1match --doFit --sumUp


For 2023: Ele30 

 * python2.7 tnpEGM_fitter.py etc/config/settings_ele_Prompt2023.py  --flag passHLTEle30WPTightHcalIsoFilter --createBins
 * python2.7 tnpEGM_fitter.py etc/config/settings_ele_Prompt2023.py  --flag passHLTEle30WPTightHcalIsoFilter --createHists
 * python2.7 tnpEGM_fitter.py etc/config/settings_ele_Prompt2023.py  --flag passHLTEle30WPTightHcalIsoFilter --doFit --sumUp

 * python2.7 tnpEGM_fitter.py etc/config/settings_ele_Prompt2023.py  --flag passHLTEle30WPTightPixelMatchFilter --createBins
 * python2.7 tnpEGM_fitter.py etc/config/settings_ele_Prompt2023.py  --flag passHLTEle30WPTightPixelMatchFilter --createHists
 * python2.7 tnpEGM_fitter.py etc/config/settings_ele_Prompt2023.py  --flag passHLTEle30WPTightPixelMatchFilter --doFit --sumUp

 * python2.7 tnpEGM_fitter.py etc/config/settings_ele_Prompt2023.py  --flag passHLTEle30WPTightPMS2Filter --createBins
 * python2.7 tnpEGM_fitter.py etc/config/settings_ele_Prompt2023.py  --flag passHLTEle30WPTightPMS2Filter --createHists
 * python2.7 tnpEGM_fitter.py etc/config/settings_ele_Prompt2023.py  --flag passHLTEle30WPTightPMS2Filter --doFit --sumUp

 * python2.7 tnpEGM_fitter.py etc/config/settings_ele_Prompt2023.py  --flag passHLTEle30WPTightGsfOneOEMinusOneOPFilter --createBins
 * python2.7 tnpEGM_fitter.py etc/config/settings_ele_Prompt2023.py  --flag passHLTEle30WPTightGsfOneOEMinusOneOPFilter --createHists
 * python2.7 tnpEGM_fitter.py etc/config/settings_ele_Prompt2023.py  --flag passHLTEle30WPTightGsfOneOEMinusOneOPFilter --doFit --sumUp


