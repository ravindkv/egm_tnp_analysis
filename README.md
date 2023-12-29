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


For 2022: DoubleEle_23_12_Leg2
 * python2.7 tnpEGM_fitter.py etc/config/settings_ele_Prompt2022.py  --flag passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg2 --createBins
 * python2.7 tnpEGM_fitter.py etc/config/settings_ele_Prompt2022.py  --flag passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg2 --createHists
 * python2.7 tnpEGM_fitter.py etc/config/settings_ele_Prompt2022.py  --flag passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg2 --doFit --sumUp



For 2022: DoubleEle_23_12_Leg2
 * python2.7 tnpEGM_fitter.py etc/config/settings_ele_Prompt2022.py  --flag passHltDoubleEle33CaloIdLMWUnsLeg --createBins
 * python2.7 tnpEGM_fitter.py etc/config/settings_ele_Prompt2022.py  --flag passHltDoubleEle33CaloIdLMWUnsLeg --createHists
 * python2.7 tnpEGM_fitter.py etc/config/settings_ele_Prompt2022.py  --flag passHltDoubleEle33CaloIdLMWUnsLeg --doFit --sumUp
