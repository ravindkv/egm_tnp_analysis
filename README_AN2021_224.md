# Install stable branch
```bash
cmsrel CMSSW_11_2_0
cd CMSSW_11_2_0/src
cmsenv
git clone git@github.com:ravindkv/egm_tnp_analysis.git 
cd egm_tnp_analysis
git checkout AN2021_224
make 
```
Trigger scale factor :

For 2016PreVFP:
 * python2.7 tnpEGM_fitter.py etc/config/settings_ele_UL2016_preVFP.py  --flag passHltEle27WPTightGsf --createBins
 * python2.7 tnpEGM_fitter.py etc/config/settings_ele_UL2016_preVFP.py  --flag passHltEle27WPTightGsf --createHists
 * python2.7 tnpEGM_fitter.py etc/config/settings_ele_UL2016_preVFP.py  --flag passHltEle27WPTightGsf --doFit --sumUp

For 2016PostVFP:
 * python2.7 tnpEGM_fitter.py etc/config/settings_ele_UL2016_postVFP.py  --flag passHltEle27WPTightGsf --createBins
 * python2.7 tnpEGM_fitter.py etc/config/settings_ele_UL2016_postVFP.py  --flag passHltEle27WPTightGsf --createHists
 * python2.7 tnpEGM_fitter.py etc/config/settings_ele_UL2016_postVFP.py  --flag passHltEle27WPTightGsf --doFit --sumUp

For 2017:
 * python2.7 tnpEGM_fitter.py etc/config/settings_ele_UL2017.py  --flag passHltEle32DoubleEGWPTightGsf --createBins
 * python2.7 tnpEGM_fitter.py etc/config/settings_ele_UL2017.py  --flag passHltEle32DoubleEGWPTightGsf --createHists
 * python2.7 tnpEGM_fitter.py etc/config/settings_ele_UL2017.py  --flag passHltEle32DoubleEGWPTightGsf --doFit --sumUp

For 2018:
 * python2.7 tnpEGM_fitter.py etc/config/settings_ele_UL2018.py  --flag passHltEle32WPTightGsf  --createBins
 * python2.7 tnpEGM_fitter.py etc/config/settings_ele_UL2018.py  --flag passHltEle32WPTightGsf  --createHists


Isolation scale factor :

For 2016PreVFP:
 * python2.7 tnpEGM_fitter.py etc/config/settings_ele_UL2016_preVFP_iso.py  --flag passiso --createBins
 * python2.7 tnpEGM_fitter.py etc/config/settings_ele_UL2016_preVFP_iso.py  --flag passiso --createHists
 * python2.7 tnpEGM_fitter.py etc/config/settings_ele_UL2016_preVFP_iso.py  --flag passiso --doFit --sumUp

For 2016PostVFP:
 * python2.7 tnpEGM_fitter.py etc/config/settings_ele_UL2016_postVFP_iso.py  --flag passiso --createBins
 * python2.7 tnpEGM_fitter.py etc/config/settings_ele_UL2016_postVFP_iso.py  --flag passiso --createHists
 * python2.7 tnpEGM_fitter.py etc/config/settings_ele_UL2016_postVFP_iso.py  --flag passiso --doFit --sumUp

For 2017:
 * python2.7 tnpEGM_fitter.py etc/config/settings_ele_UL2017_iso.py  --flag passiso --createBins
 * python2.7 tnpEGM_fitter.py etc/config/settings_ele_UL2017_iso.py  --flag passiso --createHists
 * python2.7 tnpEGM_fitter.py etc/config/settings_ele_UL2017_iso.py  --flag passiso --doFit --sumUp

For 2018:
 * python2.7 tnpEGM_fitter.py etc/config/settings_ele_UL2018_iso.py  --flag passiso  --createBins
 * python2.7 tnpEGM_fitter.py etc/config/settings_ele_UL2018_iso.py  --flag passiso  --createHists
 * python2.7 tnpEGM_fitter.py etc/config/settings_ele_UL2018_iso.py  --flag passiso  --doFit --sumUp

