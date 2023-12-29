import math

class efficiency:
    iPUup        = 4
    iPUdown      = 5
    def __init__(self,abin):
        self.ptBin   = abin
        self.effData = -1
    
    def __init__(self,ptBin,etaBin,effData,errEffData):
        self.ptBin      = ptBin
        self.etaBin     = etaBin
        self.effData    = effData
        self.errEffData = errEffData        

    def __str__(self):
        return '%2.3f\t%2.3f\t%2.1f\t%2.1f\t%2.4f\t%2.4f\t%2.4f\t%2.4f\t%2.4f\t%2.4f\t%2.4f\t%2.4f' % (self.etaBin[0],self.etaBin[1],
                                                                                                       self.ptBin[0] ,self.ptBin[1] ,
                                                                                                       self.effData, self.errEffData) 

    def __add__(self,eff):
        if self.effData < 0 :
            return eff.deepcopy()
        if eff.effData < 0 :
            return self.deepcopy()
        
        ptbin  = self.ptBin
        etabin = self.etaBin
        errData2 = 1.0 / (1.0/(self.errEffData*self.errEffData)+1.0/(eff.errEffData*eff.errEffData))
        wData1   = 1.0 / (self.errEffData * self.errEffData) * errData2
        wData2   = 1.0 / (eff .errEffData * eff .errEffData) * errData2
        newEffData      = wData1 * self.effData + wData2 * eff.effData;
        newErrEffData   = math.sqrt(errData2)
        effout = efficiency(ptbin,etabin,newEffData,newErrEffData)
        return effout
    


import ROOT as rt
import numpy as np

def makeTGraphFromList( listOfEfficiencies , keyMin, keyMax ):
    grOut = rt.TGraphErrors(len(listOfEfficiencies))
    
    ip = 0
    for point in listOfEfficiencies:
        grOut.SetPoint(     ip, (point[keyMin]+point[keyMax])/2. , point['val'] )
        grOut.SetPointError(ip, (point[keyMax]-point[keyMin])/2. , point['err'] )
        ip = ip + 1

    #    print "###########################"
    #    print listOfEff
    #    grOut.Print()
    return grOut



class efficiencyList: 
    effList = {}

    def __init__(self):
        self.effList = {}

    
    def __str__(self):
        outStr = ''
        for ptBin in self.effList.keys():
            for etaBin in self.effList[ptBin].keys():
                outStr += str(self.effList[ptBin][etaBin])
                outStr += '\n'
        return outStr

    
    def addEfficiency( self, eff ):
        if not self.effList.has_key(eff.ptBin):
            self.effList[eff.ptBin] = {}
        self.effList[eff.ptBin][eff.etaBin] = eff

    def pt_1DGraph_list(self, doScaleFactor):
        listOfGraphs = {}
        for ptBin in self.effList.keys():
            for etaBin in self.effList[ptBin].keys():
                if etaBin[0] >= 0 and etaBin[1] > 0:
                    etaBinPlus  = etaBin
                    etaBinMinus = (-etaBin[1],-etaBin[0])
                    
                    effPlus  = self.effList[ptBin][etaBinPlus]
                    effMinus = None
                    if self.effList[ptBin].has_key(etaBinMinus):
                        effMinus =  self.effList[ptBin][etaBinMinus] 

                    effAverage = effPlus
                    if not effMinus is None:
                        effAverage = effPlus + effMinus

                        
                    if not listOfGraphs.has_key(etaBin):                        
                        ### init average efficiency 
                        listOfGraphs[etaBin] = []

                    aValue  = effAverage.effData
                    anError = 0.0 
                    listOfGraphs[etaBin].append( {'min': ptBin[0], 'max': ptBin[1],
                                                  'val': aValue  , 'err': anError } ) 
                                                  
        return listOfGraphs

    def pt_1DGraph_list_customEtaBining(self, etaBining, doScaleFactor):
        listOfGraphs = {}
        for abin in etaBining:
            listOfGraphs[abin] = []
            print(self.effList.keys())
            for ptBin in self.effList.keys():
                for etaBin in self.effList[ptBin].keys():
                    print(ptBin, etaBin)
                    if etaBin[0] >= 0 and etaBin[1] > 0:
                        etaBinPlus  = etaBin
                        etaBinMinus = (-etaBin[1],-etaBin[0])

                        if abin[0] < etaBin[0] or abin[1] > etaBin[1]:
                            continue
                        #                        if abin[0] >= etaBin[0] and abin[1] <= etaBin[1]:
                        #                            continue
                        effPlus  = self.effList[ptBin][etaBinPlus]
                        effMinus = None
                        if self.effList[ptBin].has_key(etaBinMinus):
                            effMinus =  self.effList[ptBin][etaBinMinus] 

                        effAverage = effPlus
                        if not effMinus is None:
                            effAverage = effPlus + effMinus

                        aValue  = effAverage.effData
                        anError = effAverage.errEffData 
                        listOfGraphs[abin].append( {'min': ptBin[0], 'max': ptBin[1],
                                                    'val': aValue  , 'err': anError } ) 
                                                  
        return listOfGraphs


    
    def eta_1DGraph_list(self, typeGR = 0 ):
        listOfGraphs = {}
        for ptBin in self.effList.keys():
            for etaBin in self.effList[ptBin].keys():
                if not listOfGraphs.has_key(ptBin):                        
                    ### init average efficiency 
                    listOfGraphs[ptBin] = []
                effAverage = self.effList[ptBin][etaBin]
                aValue  = effAverage.effData
                anError = effAverage.errEffData 
                listOfGraphs[ptBin].append( {'min': etaBin[0], 'max': etaBin[1],
                                             'val': aValue  , 'err': anError } )

        return listOfGraphs





    
