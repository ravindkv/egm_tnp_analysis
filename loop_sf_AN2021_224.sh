#!/bin/sh


settingslist="UL2016_preVFP UL2016_postVFP UL2017 UL2018"

declare -A flagdict
flagdict["UL2016_preVFP"]="passHltEle27WPTightGsf"
flagdict["UL2016_postVFP"]="passHltEle27WPTightGsf"
flagdict["UL2017"]="passHltEle32DoubleEGWPTightGsf"
flagdict["UL2018"]="passHltEle32WPTightGsf"


for settings in ${settingslist}
do
    command="python2.7 tnpEGM_fitter.py etc/config/settings_ele_${settings}.py --flag ${flagdict[$settings]} --createBins"
    echo Executing command : $command
    `$command`

    command="python2.7 tnpEGM_fitter.py etc/config/settings_ele_${settings}.py --flag ${flagdict[$settings]} --createHists"
    echo Executing command : $command
    `$command`

    command="python2.7 tnpEGM_fitter.py etc/config/settings_ele_${settings}.py --flag ${flagdict[$settings]} --doFit"
    echo Executing command : $command
    `$command`

    command="python2.7 tnpEGM_fitter.py etc/config/settings_ele_${settings}.py --flag ${flagdict[$settings]} --doFit --mcSig --altSig"
    echo Executing command : $command
    `$command`

    command="python2.7 tnpEGM_fitter.py etc/config/settings_ele_${settings}.py --flag ${flagdict[$settings]} --doFit --altSig"
    echo Executing command : $command
    `$command`
    
    command="python2.7 tnpEGM_fitter.py etc/config/settings_ele_${settings}.py --flag ${flagdict[$settings]} --doFit --altBkg"
    echo Executing command : $command
    `$command`

    command="python2.7 tnpEGM_fitter.py etc/config/settings_ele_${settings}.py --flag ${flagdict[$settings]} --sumUp"
    echo Executing command : $command
    `$command`

done

for settings in ${settingslist}
do
    command="python2.7 tnpEGM_fitter.py etc/config/settings_ele_${settings}_iso.py --flag passiso --createBins"
    echo Executing command : $command
    `$command`

    command="python2.7 tnpEGM_fitter.py etc/config/settings_ele_${settings}_iso.py --flag passiso --createHists"
    echo Executing command : $command
    `$command`

    command="python2.7 tnpEGM_fitter.py etc/config/settings_ele_${settings}_iso.py --flag passiso --doFit"
    echo Executing command : $command
    `$command`

    command="python2.7 tnpEGM_fitter.py etc/config/settings_ele_${settings}_iso.py --flag passiso --doFit --mcSig --altSig"
    echo Executing command : $command
    `$command`

    command="python2.7 tnpEGM_fitter.py etc/config/settings_ele_${settings}_iso.py --flag passiso --doFit --altSig"
    echo Executing command : $command
    `$command`
    
    command="python2.7 tnpEGM_fitter.py etc/config/settings_ele_${settings}_iso.py --flag passiso --doFit --altBkg"
    echo Executing command : $command
    `$command`

    command="python2.7 tnpEGM_fitter.py etc/config/settings_ele_${settings}_iso.py --flag passiso --sumUp"
    echo Executing command : $command
    `$command`

done

for settings in ${settingslist}
do
    command="python2.7 tnpEGM_fitter.py etc/config/settings_ele_${settings}_wpl.py --flag passingMVA94XwpLnoisoV2 --createBins"
    echo Executing command : $command
    `$command`

    command="python2.7 tnpEGM_fitter.py etc/config/settings_ele_${settings}_wpl.py --flag passingMVA94XwpLnoisoV2 --createHists"
    echo Executing command : $command
    `$command`

    command="python2.7 tnpEGM_fitter.py etc/config/settings_ele_${settings}_wpl.py --flag passingMVA94XwpLnoisoV2 --doFit"
    echo Executing command : $command
    `$command`

    command="python2.7 tnpEGM_fitter.py etc/config/settings_ele_${settings}_wpl.py --flag passingMVA94XwpLnoisoV2 --doFit --mcSig --altSig"
    echo Executing command : $command
    `$command`

    command="python2.7 tnpEGM_fitter.py etc/config/settings_ele_${settings}_wpl.py --flag passingMVA94XwpLnoisoV2 --doFit --altSig"
    echo Executing command : $command
    `$command`
    
    command="python2.7 tnpEGM_fitter.py etc/config/settings_ele_${settings}_wpl.py --flag passingMVA94XwpLnoisoV2 --doFit --altBkg"
    echo Executing command : $command
    `$command`

    command="python2.7 tnpEGM_fitter.py etc/config/settings_ele_${settings}_wpl.py --flag passingMVA94XwpLnoisoV2 --sumUp"
    echo Executing command : $command
    `$command`

done
