#!/usr/bin/env python

import sys,os
from math import sqrt
import ROOT as rt
import CMS_lumi, tdrstyle

from efficiencyUtils import efficiency
from efficiencyUtils import efficiencyList
import efficiencyUtils as effUtil

tdrstyle.setTDRStyle()


effiMin = 0.68
effiMax = 1.07

def isFloat( myFloat ):
    try:
        float(myFloat)
        return True
    except:
        return False



graphColors = [rt.kBlack, rt.kGray+1, rt.kRed +1, rt.kRed-2, rt.kAzure+2, rt.kAzure-1, 
               rt.kSpring-1, rt.kYellow -2 , rt.kYellow+1,
               rt.kBlack, rt.kBlack, rt.kBlack, 
               rt.kBlack, rt.kBlack, rt.kBlack, rt.kBlack, rt.kBlack, rt.kBlack, rt.kBlack ]




def findMinMax( effis ):
    mini = +999
    maxi = -999

    for key in effis.keys():
        for eff in effis[key]:
            if eff['val'] - eff['err'] < mini:
                mini = eff['val'] - eff['err']
            if eff['val'] + eff['err'] > maxi:
                maxi = eff['val'] + eff['err']

    if mini > 0.18 and mini < 0.28:
        mini = 0.18
    if mini > 0.28 and mini < 0.38:
        mini = 0.28
    if mini > 0.38 and mini < 0.48:
        mini = 0.38
    if mini > 0.48 and mini < 0.58:
        mini = 0.48
    if mini > 0.58 and mini < 0.68:
        mini = 0.58
    if mini > 0.68 and mini < 0.78:
        mini = 0.68
    if mini > 0.78 and mini < 0.88:
        mini = 0.78
    if mini > 0.88:
        mini = 0.88
    if mini > 0.92:
        mini = 0.92

        
    if  maxi > 0.95:
        maxi = 1.17        
    elif maxi < 0.87:
        maxi = 0.87
    else:
        maxi = 1.07

    if maxi-mini > 0.5:
        maxi = maxi + 0.2
        
    return (mini,maxi)

    

def EffiGraph1D(effDataList,nameout, xAxis = 'pT', yAxis = 'eta'):
    W = 600
    H = 800
    yUp = 0.05
    canName = 'toto' + xAxis

    c = rt.TCanvas(canName,canName,50,50,H,W)
    c.SetTopMargin(0.055)
    c.SetBottomMargin(0.15)
    c.SetLeftMargin(0.15)
    c.cd()
    
    firstGraph = True
    leg = rt.TLegend(0.5,0.80,0.85 ,0.92)
    leg.SetFillColor(0)
    leg.SetBorderSize(0)

    igr = 0
    listOfTGraph1 = []

    xMin = 10
    xMax = 200
    if 'pT' in xAxis or 'pt' in xAxis:
        c.SetLogx()
        xMin = 10
        xMax = 500
    elif 'vtx' in xAxis or 'Vtx' in xAxis or 'PV' in xAxis:
        xMin =  3
        xMax = 42
    elif 'eta' in xAxis or 'Eta' in xAxis:
        xMin = -2.60
        xMax = +2.60
    elif 'phi' in xAxis or 'Phi' in xAxis:
        xMin = -2.60
        xMax = +2.60
    
    if 'abs' in xAxis or 'Abs' in xAxis:
        xMin = 0.0

    effminmax =  findMinMax( effDataList )
    effiMin = effminmax[0]
    effiMax = effminmax[1]
    effiMin = 0.18
    effiMax = 1.35

    for key in sorted(effDataList.keys()):
        grBinsEffData = effUtil.makeTGraphFromList(effDataList[key], 'min', 'max')
        grBinsEffData.SetMarkerColor( graphColors[igr] )
        grBinsEffData.SetLineColor(   graphColors[igr] )
        grBinsEffData.SetLineWidth(2) 
                
        grBinsEffData.GetHistogram().SetMinimum(effiMin)
        grBinsEffData.GetHistogram().SetMaximum(effiMax)

        grBinsEffData.GetHistogram().GetXaxis().SetLimits(xMin,xMax)
        grBinsEffData.GetHistogram().GetYaxis().SetTitleOffset(1)
        grBinsEffData.GetHistogram().GetYaxis().SetTitle("Data efficiency" )
        grBinsEffData.GetHistogram().GetYaxis().SetRangeUser( effiMin, effiMax )
        
        grBinsEffData.GetHistogram().GetXaxis().SetTitleOffset(1)
        if 'eta' in xAxis or 'Eta' in xAxis:
            grBinsEffData.GetHistogram().GetXaxis().SetTitle("SuperCluster #eta")
        if 'phi' in xAxis or 'Phi' in xAxis:
            grBinsEffData.GetHistogram().GetXaxis().SetTitle("Electron #phi")
        elif 'pt' in xAxis or 'pT' in xAxis:
            grBinsEffData.GetHistogram().GetXaxis().SetTitle("Electron p_{T}  [GeV]")  
        elif 'vtx' in xAxis or 'Vtx' in xAxis or 'PV' in xAxis:
            grBinsEffData.GetHistogram().GetXaxis().SetTitle("N_{vtx}") 

        ### to avoid loosing the TGraph keep it in memory by adding it to a list
        listOfTGraph1.append( grBinsEffData )
        if 'eta' in yAxis or 'Eta' in yAxis:
            leg.AddEntry( grBinsEffData, '%1.3f #leq | #eta | #leq  %1.3f' % (float(key[0]),float(key[1])), "PL")        
        elif 'phi' in yAxis or 'Phi' in yAxis:
            leg.AddEntry( grBinsEffData, '%1.3f #leq | #phi | #leq  %1.3f' % (float(key[0]),float(key[1])), "PL")        
        elif 'pt' in yAxis or 'pT' in yAxis:
            leg.AddEntry( grBinsEffData, '%3.0f #leq p_{T} #leq  %3.0f GeV' % (float(key[0]),float(key[1])), "PL")        
        elif 'vtx' in yAxis or 'Vtx' in yAxis or 'PV' in yAxis:
            leg.AddEntry( grBinsEffData, '%3.0f #leq nVtx #leq  %3.0f'      % (float(key[0]),float(key[1])), "PL")        
        
    for igr in range(len(listOfTGraph1)+1):

        option = "P"
        if igr == 1:
            option = "AP"

        use_igr = igr
        if use_igr == len(listOfTGraph1):
            use_igr = 0
            
        listOfTGraph1[use_igr].SetLineColor(graphColors[use_igr])
        listOfTGraph1[use_igr].SetMarkerColor(graphColors[use_igr])

        listOfTGraph1[use_igr].GetHistogram().SetMinimum(effiMin)
        listOfTGraph1[use_igr].GetHistogram().SetMaximum(effiMax)
        if 'pT' in xAxis or 'pt' in xAxis :
            listOfTGraph1[use_igr].GetHistogram().GetXaxis().SetMoreLogLabels()
        listOfTGraph1[use_igr].GetHistogram().GetXaxis().SetNoExponent()
        listOfTGraph1[use_igr].Draw(option)

    leg.Draw()    
    CMS_lumi.CMS_lumi(c, 5, 10)

    c.Print(nameout)
    listName = nameout.split('/')
    for iext in ["pdf","C","png"]:
        c.SaveAs(nameout.replace('egammaEffi.txt_egammaPlots',listName[-6].replace('tnp','')+'_SFvs'+xAxis+'_'+listName[-3]).replace('pdf',iext))

    #return listOfTGraph1

    #################################################    


def doEGM_SFs(filein, lumi, axis = ['pT','eta'] ):
    print " Opening file: %s (plot lumi: %3.1f)" % ( filein, lumi )
    CMS_lumi.lumi_13TeV = "%+3.1f fb^{-1}" % lumi 

    nameOutBase = filein 
    if not os.path.exists( filein ) :
        print 'file %s does not exist' % filein
        sys.exit(1)


    fileWithEff = open(filein, 'r')
    effGraph = efficiencyList()
    
    for line in fileWithEff :
        modifiedLine = line.lstrip(' ').rstrip(' ').rstrip('\n')
        numbers = modifiedLine.split('\t')
        if len(numbers) > 0 and isFloat(numbers[0]):
            etaKey = ( float(numbers[0]), float(numbers[1]) )
            ptKey  = ( float(numbers[2]), min(500,float(numbers[3])) )
        
            myeff = efficiency(ptKey,etaKey,float(numbers[4]),float(numbers[5]))

            effGraph.addEfficiency(myeff)

    fileWithEff.close()

    customEtaBining = []
    if 'eta' in  axis[1]:
        customEtaBining.append( (0.000,0.800))
        customEtaBining.append( (0.800,1.444))
        customEtaBining.append( (1.566,2.000))
        customEtaBining.append( (2.000,2.500))
    else:
        customEtaBining.append( (0.000,1.000))
        customEtaBining.append( (1.000,1.566))
        customEtaBining.append( (1.566,2.000))
        customEtaBining.append( (2.000,3.000))
    print("customBining = ", customEtaBining)


    pdfout = nameOutBase + '_egammaPlots.pdf'
    cDummy = rt.TCanvas()
    cDummy.Print( pdfout + "[" )

    EffiGraph1D( effGraph.pt_1DGraph_list_customEtaBining(customEtaBining, False ) , 
                 pdfout,
                 xAxis = axis[0], yAxis = axis[1] )
    EffiGraph1D( effGraph.eta_1DGraph_list( typeGR =  0 ), 
                 pdfout,
                 xAxis = axis[1], yAxis = axis[0] )
    cDummy.Print( pdfout + "]" )

if __name__ == "__main__":

    import argparse
    parser = argparse.ArgumentParser(description='tnp EGM scale factors')
    parser.add_argument('--lumi'  , type = float, default = -1, help = 'Lumi (just for plotting purpose)')
    parser.add_argument('txtFile' , default = None, help = 'EGM formatted txt file')
    parser.add_argument('--PV'    , action  = 'store_true', help = 'plot 1 vs nVtx instead of pT' )
    args = parser.parse_args()

    if args.txtFile is None:
        print ' - Needs EGM txt file as input'
        sys.exit(1)
    

    CMS_lumi.lumi_13TeV = "5.5 fb^{-1}"
    CMS_lumi.writeExtraText = 1
    CMS_lumi.lumi_sqrtS = "13.6 TeV"
    
    axis = ['pT','eta']
    if args.PV:
        axis = ['nVtx','eta']

    doEGM_SFs(args.txtFile, args.lumi,axis)
