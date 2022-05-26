'''
from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

hub = PrimeHub()

hub.light_matrix.show_image('HAPPY')
'''
class PR:
    myclassname = "PR"
    name = None
    parent = None
    def __init__(self,name):
        self.name = name


class PRValue(PR):
    myclassname = "PRValue"

class PRMode(PR):

    def __init__(self,name):
        super(PRMode, self).__init__(name)
        self.vls = {}
        self.submodes = {}

    def aSM(self,m):
        self.submodes[m.name] = m

    def aV(self,v):
        self.vls[v.name] = v

    def getEgValue(self,v,curr):
        ret = None
        if v.name in self.vls.keys():
            ret = v
        else:
            if curr.name in self.vls.keys():
                ret = curr
            else:
                itk = list(self.vls.keys())[0]
                ret = self.vls[itk]

        return ret

    def getEgSMd(self,m,curr):
        ret = None
        found = False

        if m.name in self.submodes.keys():
            ret = m

        else:
            if curr.name in self.submodes.keys():
                ret = curr

            else:
                # If none of two are found, search the first submode with the same parent
                for ks in self.submodes.keys():
                    s = self.submodes[ks]
                    if s.parent == m.parent:
                        ret = s
                        break

        return ret


class PRNode(PR):
    selM = None

    def __init__(self,name):
        super(PRNode, self).__init__(name)
        self.mds = {}


    def aM(self,m):
        self.mds[m.name] = m
        m.parent = self
        if self.selM == None:
            self.selM = m

    def init(self):
        firstMode = list(self.mds.keys())[0]
        self.sM(firstMode)

    def setEgMode(self):
        if self.selM is None:
            self.init()

        # TODO: Check if this sM is redundant
        return self.sM(self.selM)

    def sM(self,m):
        return None

    def getEgMode(self,m):
        ret = None
        if self.parent is None:
            ret = m

        else:
            ret = self.parent.selM.getEgSMd(m,self.selM)

        return ret


class PRParam(PRNode):
    selV = None

    def __init__(self,name):
        super(PRParam, self).__init__(name)
        self.vls = {}

    def aV(self,v):
        self.vls[v.name] = v
        v.parent = self
        if self.selV == None:
            self.selV = v

    def setEgValue(self):
        return self.sV(self.selV)

    def sM(self,m):
        ret = self.getEgMode(m)

        if ret is None:
            mk = list(self.mds.keys())[0]
            ret = self.mds[mk]

        if ret != self.selM:
            self.selM = ret
            self.sV(self.selV)

        return ret

    def getEgValue(self,v,curr):
        ret = None
        if self.selM is None:
            self.init()

        ret = self.selM.getEgValue(v,curr)

        return ret

    def sV(self,v):
        ret = self.getEgValue(v,self.selV)
        if ret != self.selV:
            self.selV = ret

        return ret

class PRSys(PRNode):

    def __init__(self,name):
        super(PRSys, self).__init__(name)
        self.params = {}
        self.ss = {}

    def addParam(self,p):
        self.params[p.name] = p
        p.parent = self

    def aSS(self,s):
        self.ss[s.name] = s
        s.parent = self

    def sM(self,m):
        ret = self.getEgMode(m)
        if ret is None:
            mk = list(self.mds.keys())[0]
            ret = self.mds[mk]

        if ret != self.selM:
            self.selM = ret

            for k in self.params.keys():
                p = self.params[k]
                p.setEgMode()

            for k in self.ss.keys():
                s = self.ss[k]
                s.setEgMode()

        return ret


class csysWROPR:
	def __init__(self):
		self.sysMision = PRSys("Mision")
		self.mdMisionUNK = PRMode("UNK")
		self.root = self.sysMision
		self.mdMisionNormal = PRMode("Normal")
		self.sysTr = PRSys("Tr")
		self.mdTrUNK = PRMode("UNK")
		self.mdP00  = PRMode("P00")
		self.mdP01  = PRMode("P01")
		self.mdP02  = PRMode("P02")
		self.mdP03  = PRMode("P03")
		self.mdP04  = PRMode("P04")
		self.mdP05  = PRMode("P05")
		self.mdP06  = PRMode("P06")
		self.mdP07  = PRMode("P07")
		self.mdP08  = PRMode("P08_")
		self.sysSit = PRSys("Situacion")
		self.mdUNK = PRMode("UNK")
		self.mdBNN00 = PRMode("BNN")
		self.mdNBB00 = PRMode("NBB")
		self.mdBBB00 = PRMode("BBB")
		self.mdNNB00 = PRMode("NNB")
		self.mdBNB00 = PRMode("BNB")
		self.mdNBN00 = PRMode("NBN")
		self.mdBBN00 = PRMode("BBN")
		self.mdNNN00 = PRMode("NNN")
		self.mdNBV01 = PRMode("NBV")
		self.mdBNB01 = PRMode("BNB")
		self.mdBBB01 = PRMode("BBB")
		self.mdBNN01 = PRMode("BNN")
		self.mdNBB01 = PRMode("NBB")
		self.mdNNB01 = PRMode("NNB")
		self.mdVBN01 = PRMode("VBN")
		self.mdBBN01 = PRMode("BBN")
		self.mdNNN01 = PRMode("NNN")
		self.mdNBN01 = PRMode("NBN")
		self.mdBBB02 = PRMode("BBB")
		self.mdBBN02 = PRMode("BBN")
		self.mdBNB02 = PRMode("BNB")
		self.mdBNN02 = PRMode("BNN")
		self.mdNBB02 = PRMode("NBB")
		self.mdNBN02 = PRMode("NBN")
		self.mdNBV02 = PRMode("NBV")
		self.mdNNB02 = PRMode("NNB")
		self.mdNNN02 = PRMode("NNN")
		self.mdVBN02 = PRMode("VBN")
		self.mdBBB03 = PRMode("BBB")
		self.mdBBN03 = PRMode("BBN")
		self.mdBNB03 = PRMode("BNB")
		self.mdBNN03 = PRMode("BNN")
		self.mdNBB03 = PRMode("NBB")
		self.mdNBN03 = PRMode("NBN")
		self.mdNBV03 = PRMode("NBV")
		self.mdNNB03 = PRMode("NNB")
		self.mdNNN03 = PRMode("NNN")
		self.mdVBN03 = PRMode("VBN")
		self.mdBBB04 = PRMode("BBB")
		self.mdBBN04 = PRMode("BBN")
		self.mdBNB04 = PRMode("BNB")
		self.mdBNN04 = PRMode("BNN")
		self.mdNBB04 = PRMode("NBB")
		self.mdNBN04 = PRMode("NBN")
		self.mdNBV04 = PRMode("NBV")
		self.mdNNB04 = PRMode("NNB")
		self.mdNNN04 = PRMode("NNN")
		self.mdVBN04 = PRMode("VBN")
		self.mdBBB05 = PRMode("BBB")
		self.mdBBN05 = PRMode("BBN")
		self.mdBNB05 = PRMode("BNB")
		self.mdBNN05 = PRMode("BNN")
		self.mdNBB05 = PRMode("NBB")
		self.mdNBN05 = PRMode("NBN")
		self.mdNNB05 = PRMode("NNB")
		self.mdNNN05 = PRMode("NNN")
		self.mdVBN06 = PRMode("VBN")
		self.mdNBB06 = PRMode("NBB")
		self.mdBNB06 = PRMode("BNB")
		self.mdNBN06 = PRMode("NBN")
		self.mdNNN06 = PRMode("NNN")
		self.mdBNN06 = PRMode("BNN")
		self.mdBBN06 = PRMode("BBN")
		self.mdBBB06 = PRMode("BBB")
		self.mdNBV06 = PRMode("NBV")
		self.mdNNB06 = PRMode("NNB")
		self.mdBBB07 = PRMode("BBB")
		self.mdBBN07 = PRMode("BBN")
		self.mdBNB07 = PRMode("BNB")
		self.mdBNN07 = PRMode("BNN")
		self.mdNBB07 = PRMode("NBB")
		self.mdNBN07 = PRMode("NBN")
		self.mdNBV07 = PRMode("NBV")
		self.mdNNB07 = PRMode("NNB")
		self.mdNNN07 = PRMode("NNN")
		self.mdVBN07 = PRMode("VBN")
		self.mdVVB07 = PRMode("VVB")
		self.mdVVV07 = PRMode("VVV")
		self.mdVVV08 = PRMode("VVV")
		self.mdVBN08 = PRMode("VBN")
		self.mdVVB08 = PRMode("VVB")
		self.sysDecMov = PRSys("DecMov")
		self.mdDecMvUNK = PRMode("UNK")
		self.mdDecMvFw = PRMode("Fw")
		self.mdCompIzq = PRMode("CompIzq")
		self.mdCompDer = PRMode("CompDer")
		self.mdGirarDer = PRMode("GirarDer")
		self.mdGirarIzq = PRMode("GirarIzq")
		self.mdStp = PRMode("Stp")
		self.prRdDer = PRParam("RdDer")
		self.mdRdDerUNK = PRMode("UNK")
		self.vlRdDer_UNK = PRValue("UNK")
		self.mdRdDerStp = PRMode("Stp")
		self.mdRdDerFw = PRMode("Fw")
		self.mdRdDerBw = PRMode("Bw")
		self.vlRdDer_Stp = PRValue("Stp")
		self.vlRdDer_Fw = PRValue("Fw")
		self.vlRdDer_Bw = PRValue("Bw")
		self.prRdIzq = PRParam("RdIzq")
		self.mdRdIzqUNK = PRMode("UNK")
		self.vlRdIzq_UNK = PRValue("UNK")
		self.mdRdIzqStp = PRMode("Stp")
		self.mdRdIzqFw = PRMode("Fw")
		self.mdRdIzqBw = PRMode("Bw")
		self.vlRdIzq_Stp = PRValue("Stp")
		self.vlRdIzq_Fw = PRValue("Fw")
		self.vlRdIzq_Bw = PRValue("Bw")
		self.sysNext = PRSys("Next")
		self.mdNextUNK = PRMode("UNK")
		self.mdNextSi = PRMode("Si")
		self.sysDecSeg = PRSys("DecSeg")
		self.mdDecSegUNK = PRMode("UNK")
		self.mdDecSegBNB = PRMode("BNB")
		self.mdDecSegVVB = PRMode("VVB")
		self.sysDecAp = PRSys("DecAp")
		self.mdDecApUNK = PRMode("UNK")
		self.mdDecApAbi = PRMode("Abi")
		self.mdDecApMedio = PRMode("Medio")
		self.mdDecApCerr = PRMode("Cerr")
		self.sysMision.aM(self.mdMisionUNK)
		self.sysMision.aM(self.mdMisionNormal)
		self.sysMision.aSS(self.sysTr)
		self.sysTr.aM(self.mdTrUNK)
		self.sysTr.aM(self.mdP00)
		self.sysTr.aM(self.mdP01)
		self.sysTr.aM(self.mdP02)
		self.sysTr.aM(self.mdP03)
		self.sysTr.aM(self.mdP04)
		self.sysTr.aM(self.mdP05)
		self.sysTr.aM(self.mdP06)
		self.sysTr.aM(self.mdP07)
		self.sysTr.aM(self.mdP08)
		self.sysTr.aSS(self.sysSit)
		self.sysSit.aM(self.mdUNK)
		self.sysSit.aM(self.mdBNN00)
		self.sysSit.aM(self.mdNBB00)
		self.sysSit.aM(self.mdBBB00)
		self.sysSit.aM(self.mdNNB00)
		self.sysSit.aM(self.mdBNB00)
		self.sysSit.aM(self.mdNBN00)
		self.sysSit.aM(self.mdBBN00)
		self.sysSit.aM(self.mdNNN00)
		self.sysSit.aM(self.mdNBV01)
		self.sysSit.aM(self.mdBNB01)
		self.sysSit.aM(self.mdBBB01)
		self.sysSit.aM(self.mdBNN01)
		self.sysSit.aM(self.mdNBB01)
		self.sysSit.aM(self.mdNNB01)
		self.sysSit.aM(self.mdVBN01)
		self.sysSit.aM(self.mdBBN01)
		self.sysSit.aM(self.mdNNN01)
		self.sysSit.aM(self.mdNBN01)
		self.sysSit.aM(self.mdBBB02)
		self.sysSit.aM(self.mdBBN02)
		self.sysSit.aM(self.mdBNB02)
		self.sysSit.aM(self.mdBNN02)
		self.sysSit.aM(self.mdNBB02)
		self.sysSit.aM(self.mdNBN02)
		self.sysSit.aM(self.mdNBV02)
		self.sysSit.aM(self.mdNNB02)
		self.sysSit.aM(self.mdNNN02)
		self.sysSit.aM(self.mdVBN02)
		self.sysSit.aM(self.mdBBB03)
		self.sysSit.aM(self.mdBBN03)
		self.sysSit.aM(self.mdBNB03)
		self.sysSit.aM(self.mdBNN03)
		self.sysSit.aM(self.mdNBB03)
		self.sysSit.aM(self.mdNBN03)
		self.sysSit.aM(self.mdNBV03)
		self.sysSit.aM(self.mdNNB03)
		self.sysSit.aM(self.mdNNN03)
		self.sysSit.aM(self.mdVBN03)
		self.sysSit.aM(self.mdBBB04)
		self.sysSit.aM(self.mdBBN04)
		self.sysSit.aM(self.mdBNB04)
		self.sysSit.aM(self.mdBNN04)
		self.sysSit.aM(self.mdNBB04)
		self.sysSit.aM(self.mdNBN04)
		self.sysSit.aM(self.mdNBV04)
		self.sysSit.aM(self.mdNNB04)
		self.sysSit.aM(self.mdNNN04)
		self.sysSit.aM(self.mdVBN04)
		self.sysSit.aM(self.mdBBB05)
		self.sysSit.aM(self.mdBBN05)
		self.sysSit.aM(self.mdBNB05)
		self.sysSit.aM(self.mdBNN05)
		self.sysSit.aM(self.mdNBB05)
		self.sysSit.aM(self.mdNBN05)
		self.sysSit.aM(self.mdNNB05)
		self.sysSit.aM(self.mdNNN05)
		self.sysSit.aM(self.mdVBN06)
		self.sysSit.aM(self.mdNBB06)
		self.sysSit.aM(self.mdBNB06)
		self.sysSit.aM(self.mdNBN06)
		self.sysSit.aM(self.mdNNN06)
		self.sysSit.aM(self.mdBNN06)
		self.sysSit.aM(self.mdBBN06)
		self.sysSit.aM(self.mdBBB06)
		self.sysSit.aM(self.mdNBV06)
		self.sysSit.aM(self.mdNNB06)
		self.sysSit.aM(self.mdBBB07)
		self.sysSit.aM(self.mdBBN07)
		self.sysSit.aM(self.mdBNB07)
		self.sysSit.aM(self.mdBNN07)
		self.sysSit.aM(self.mdNBB07)
		self.sysSit.aM(self.mdNBN07)
		self.sysSit.aM(self.mdNBV07)
		self.sysSit.aM(self.mdNNB07)
		self.sysSit.aM(self.mdNNN07)
		self.sysSit.aM(self.mdVBN07)
		self.sysSit.aM(self.mdVVB07)
		self.sysSit.aM(self.mdVVV07)
		self.sysSit.aM(self.mdVVV08)
		self.sysSit.aM(self.mdVBN08)
		self.sysSit.aM(self.mdVVB08)
		self.sysSit.aSS(self.sysDecMov)
		self.sysDecMov.aM(self.mdDecMvUNK)
		self.sysDecMov.aM(self.mdDecMvFw)
		self.sysDecMov.aM(self.mdCompIzq)
		self.sysDecMov.aM(self.mdCompDer)
		self.sysDecMov.aM(self.mdGirarDer)
		self.sysDecMov.aM(self.mdGirarIzq)
		self.sysDecMov.aM(self.mdStp)
		self.sysDecMov.addParam(self.prRdDer)
		self.prRdDer.aV(self.vlRdDer_UNK)
		self.prRdDer.aM(self.mdRdDerUNK)
		self.mdRdDerUNK.aV(self.vlRdDer_UNK)
		self.mdDecMvUNK.aSM(self.mdRdDerUNK)
		self.prRdDer.aM(self.mdStp)
		self.prRdDer.aM(self.mdRdDerFw)
		self.prRdDer.aM(self.mdRdDerBw)
		self.prRdDer.aV(self.vlRdDer_Stp)
		self.prRdDer.aV(self.vlRdDer_Fw)
		self.prRdDer.aV(self.vlRdDer_Bw)
		self.sysDecMov.addParam(self.prRdIzq)
		self.prRdIzq.aV(self.vlRdIzq_UNK)
		self.prRdIzq.aM(self.mdRdIzqUNK)
		self.mdRdIzqUNK.aV(self.vlRdIzq_UNK)
		self.mdDecMvUNK.aSM(self.mdRdIzqUNK)
		self.prRdIzq.aM(self.mdStp)
		self.prRdIzq.aM(self.mdRdIzqFw)
		self.prRdIzq.aM(self.mdRdIzqBw)
		self.prRdIzq.aV(self.vlRdIzq_Stp)
		self.prRdIzq.aV(self.vlRdIzq_Fw)
		self.prRdIzq.aV(self.vlRdIzq_Bw)
		self.sysSit.aSS(self.sysNext)
		self.sysNext.aM(self.mdNextUNK)
		self.sysNext.aM(self.mdNextSi)
		self.sysSit.aSS(self.sysDecSeg)
		self.sysDecSeg.aM(self.mdDecSegUNK)
		self.sysDecSeg.aM(self.mdDecSegBNB)
		self.sysDecSeg.aM(self.mdDecSegVVB)
		self.sysTr.aSS(self.sysDecAp)
		self.sysDecAp.aM(self.mdDecApUNK)
		self.sysDecAp.aM(self.mdDecApAbi)
		self.sysDecAp.aM(self.mdDecApMedio)
		self.sysDecAp.aM(self.mdDecApCerr)
		self.mdMisionNormal.aSM(self.mdP00)
		self.mdMisionNormal.aSM(self.mdP01)
		self.mdMisionNormal.aSM(self.mdP02)
		self.mdMisionNormal.aSM(self.mdP03)
		self.mdMisionNormal.aSM(self.mdP04)
		self.mdMisionNormal.aSM(self.mdP05)
		self.mdMisionNormal.aSM(self.mdP06)
		self.mdMisionNormal.aSM(self.mdP07)
		self.mdMisionNormal.aSM(self.mdP08)
		self.mdP00.aSM(self.mdNNB00)
		self.mdP00.aSM(self.mdBBB00)
		self.mdP00.aSM(self.mdBNB00)
		self.mdP00.aSM(self.mdNNN00)
		self.mdP00.aSM(self.mdBNN00)
		self.mdP00.aSM(self.mdBBN00)
		self.mdP00.aSM(self.mdNBB00)
		self.mdP00.aSM(self.mdNBN00)
		self.mdP01.aSM(self.mdNNB01)
		self.mdP01.aSM(self.mdBBB01)
		self.mdP01.aSM(self.mdBNB01)
		self.mdP01.aSM(self.mdNNN01)
		self.mdP01.aSM(self.mdBNN01)
		self.mdP01.aSM(self.mdBBN01)
		self.mdP01.aSM(self.mdNBB01)
		self.mdP01.aSM(self.mdNBN01)
		self.mdP01.aSM(self.mdVBN01)
		self.mdP01.aSM(self.mdNBV01)
		self.mdP02.aSM(self.mdNNB02)
		self.mdP02.aSM(self.mdBBB02)
		self.mdP02.aSM(self.mdBNB02)
		self.mdP02.aSM(self.mdNNN02)
		self.mdP02.aSM(self.mdBNN02)
		self.mdP02.aSM(self.mdBBN02)
		self.mdP02.aSM(self.mdNBB02)
		self.mdP02.aSM(self.mdNBN02)
		self.mdP02.aSM(self.mdNBV02)
		self.mdP02.aSM(self.mdVBN02)
		self.mdP03.aSM(self.mdBNN03)
		self.mdP03.aSM(self.mdBBB03)
		self.mdP03.aSM(self.mdBNB03)
		self.mdP03.aSM(self.mdNNN03)
		self.mdP03.aSM(self.mdNNB03)
		self.mdP03.aSM(self.mdBBN03)
		self.mdP03.aSM(self.mdNBB03)
		self.mdP03.aSM(self.mdNBN03)
		self.mdP03.aSM(self.mdNBV03)
		self.mdP03.aSM(self.mdVBN03)
		self.mdP04.aSM(self.mdBNN04)
		self.mdP04.aSM(self.mdBBB04)
		self.mdP04.aSM(self.mdBNB04)
		self.mdP04.aSM(self.mdNNN04)
		self.mdP04.aSM(self.mdNNB04)
		self.mdP04.aSM(self.mdBBN04)
		self.mdP04.aSM(self.mdNBB04)
		self.mdP04.aSM(self.mdNBN04)
		self.mdP04.aSM(self.mdNBV04)
		self.mdP04.aSM(self.mdVBN04)
		self.mdP05.aSM(self.mdBNN05)
		self.mdP05.aSM(self.mdBBB05)
		self.mdP05.aSM(self.mdBNB05)
		self.mdP05.aSM(self.mdNNN05)
		self.mdP05.aSM(self.mdNNB05)
		self.mdP05.aSM(self.mdBBN05)
		self.mdP05.aSM(self.mdNBB05)
		self.mdP05.aSM(self.mdNBN05)
		self.mdP06.aSM(self.mdBNN06)
		self.mdP06.aSM(self.mdBBB06)
		self.mdP06.aSM(self.mdBNB06)
		self.mdP06.aSM(self.mdNNN06)
		self.mdP06.aSM(self.mdNNB06)
		self.mdP06.aSM(self.mdBBN06)
		self.mdP06.aSM(self.mdNBB06)
		self.mdP06.aSM(self.mdNBN06)
		self.mdP06.aSM(self.mdNBV06)
		self.mdP07.aSM(self.mdBNN07)
		self.mdP07.aSM(self.mdBBB07)
		self.mdP07.aSM(self.mdBNB07)
		self.mdP07.aSM(self.mdNNN07)
		self.mdP07.aSM(self.mdNNB07)
		self.mdP07.aSM(self.mdBBN07)
		self.mdP07.aSM(self.mdNBB07)
		self.mdP07.aSM(self.mdNBN07)
		self.mdP07.aSM(self.mdVBN07)
		self.mdP07.aSM(self.mdVVB07)
		self.mdP07.aSM(self.mdVVV07)
		self.mdP07.aSM(self.mdNBV07)
		self.mdP08.aSM(self.mdVBN08)
		self.mdP08.aSM(self.mdVVB08)
		self.mdP08.aSM(self.mdVVV08)
		self.mdBNN00.aSM(self.mdCompDer)
		self.mdNBB00.aSM(self.mdCompIzq)
		self.mdBBB00.aSM(self.mdDecMvFw)
		self.mdNNB00.aSM(self.mdCompIzq)
		self.mdBNB00.aSM(self.mdDecMvFw)
		self.mdNBN00.aSM(self.mdDecMvFw)
		self.mdBBN00.aSM(self.mdCompDer)
		self.mdNNN00.aSM(self.mdDecMvFw)
		self.mdNBV01.aSM(self.mdGirarIzq)
		self.mdBNB01.aSM(self.mdDecMvFw)
		self.mdBBB01.aSM(self.mdStp)
		self.mdBNN01.aSM(self.mdGirarDer)
		self.mdNBB01.aSM(self.mdCompIzq)
		self.mdNNB01.aSM(self.mdCompIzq)
		self.mdVBN01.aSM(self.mdGirarDer)
		self.mdBBN01.aSM(self.mdCompDer)
		self.mdNNN01.aSM(self.mdGirarDer)
		self.mdNBN01.aSM(self.mdStp)
		self.mdBBB02.aSM(self.mdStp)
		self.mdBBN02.aSM(self.mdCompDer)
		self.mdBNB02.aSM(self.mdDecMvFw)
		self.mdBNN02.aSM(self.mdGirarDer)
		self.mdNBB02.aSM(self.mdCompIzq)
		self.mdNBN02.aSM(self.mdDecMvFw)
		self.mdNBV02.aSM(self.mdGirarIzq)
		self.mdNNB02.aSM(self.mdCompIzq)
		self.mdNNN02.aSM(self.mdGirarDer)
		self.mdVBN02.aSM(self.mdGirarDer)
		self.mdBBB03.aSM(self.mdStp)
		self.mdBBN03.aSM(self.mdCompDer)
		self.mdBNB03.aSM(self.mdDecMvFw)
		self.mdBNN03.aSM(self.mdCompDer)
		self.mdNBB03.aSM(self.mdCompIzq)
		self.mdNBN03.aSM(self.mdStp)
		self.mdNBV03.aSM(self.mdGirarIzq)
		self.mdNNB03.aSM(self.mdGirarIzq)
		self.mdNNN03.aSM(self.mdGirarIzq)
		self.mdVBN03.aSM(self.mdGirarDer)
		self.mdBBB04.aSM(self.mdCompDer)
		self.mdBBN04.aSM(self.mdCompDer)
		self.mdBNB04.aSM(self.mdDecMvFw)
		self.mdBNN04.aSM(self.mdCompDer)
		self.mdNBB04.aSM(self.mdCompIzq)
		self.mdNBN04.aSM(self.mdStp)
		self.mdNBV04.aSM(self.mdGirarIzq)
		self.mdNNB04.aSM(self.mdDecMvFw)
		self.mdNNN04.aSM(self.mdCompDer)
		self.mdVBN04.aSM(self.mdGirarDer)
		self.mdBBB05.aSM(self.mdStp)
		self.mdBBN05.aSM(self.mdCompDer)
		self.mdBNB05.aSM(self.mdDecMvFw)
		self.mdBNN05.aSM(self.mdCompDer)
		self.mdNBB05.aSM(self.mdCompIzq)
		self.mdNBN05.aSM(self.mdCompDer)
		self.mdNNB05.aSM(self.mdDecMvFw)
		self.mdNNN05.aSM(self.mdCompDer)
		self.mdVBN06.aSM(self.mdGirarDer)
		self.mdNBB06.aSM(self.mdCompIzq)
		self.mdBNB06.aSM(self.mdDecMvFw)
		self.mdNBN06.aSM(self.mdStp)
		self.mdNNN06.aSM(self.mdGirarDer)
		self.mdBNN06.aSM(self.mdCompDer)
		self.mdBBN06.aSM(self.mdCompDer)
		self.mdBBB06.aSM(self.mdStp)
		self.mdNBV06.aSM(self.mdGirarIzq)
		self.mdNNB06.aSM(self.mdGirarDer)
		self.mdBBB07.aSM(self.mdGirarDer)
		self.mdBBN07.aSM(self.mdGirarDer)
		self.mdBNB07.aSM(self.mdGirarIzq)
		self.mdBNN07.aSM(self.mdGirarIzq)
		self.mdNBB07.aSM(self.mdGirarDer)
		self.mdNBN07.aSM(self.mdGirarDer)
		self.mdNBV07.aSM(self.mdStp)
		self.mdNNB07.aSM(self.mdGirarDer)
		self.mdNNN07.aSM(self.mdGirarDer)
		self.mdVBN07.aSM(self.mdCompIzq)
		self.mdVVB07.aSM(self.mdDecMvFw)
		self.mdVVV07.aSM(self.mdGirarDer)
		self.mdVVV08.aSM(self.mdGirarDer)
		self.mdVBN08.aSM(self.mdCompIzq)
		self.mdVVB08.aSM(self.mdDecMvFw)
		self.mdDecMvFw.aSM(self.mdRdDerFw)
		self.mdCompIzq.aSM(self.mdRdDerFw)
		self.mdCompDer.aSM(self.mdRdDerStp)
		self.mdGirarDer.aSM(self.mdRdDerBw)
		self.mdGirarIzq.aSM(self.mdRdDerFw)
		self.mdStp.aSM(self.mdRdDerStp)
		self.mdRdDerStp.aV(self.vlRdDer_Stp)
		self.mdRdDerFw.aV(self.vlRdDer_Fw)
		self.mdRdDerBw.aV(self.vlRdDer_Bw)
		self.mdDecMvFw.aSM(self.mdRdIzqFw)
		self.mdCompIzq.aSM(self.mdRdIzqStp)
		self.mdCompDer.aSM(self.mdRdIzqFw)
		self.mdGirarDer.aSM(self.mdRdIzqFw)
		self.mdGirarIzq.aSM(self.mdRdIzqBw)
		self.mdStp.aSM(self.mdRdIzqStp)
		self.mdRdIzqStp.aV(self.vlRdIzq_Stp)
		self.mdRdIzqFw.aV(self.vlRdIzq_Fw)
		self.mdRdIzqBw.aV(self.vlRdIzq_Bw)
		self.mdBNB00.aSM(self.mdNextSi)
		self.mdBNN01.aSM(self.mdNextSi)
		self.mdNNN01.aSM(self.mdNextSi)
		self.mdBNN02.aSM(self.mdNextSi)
		self.mdNNN02.aSM(self.mdNextSi)
		self.mdNNB03.aSM(self.mdNextSi)
		self.mdNNN03.aSM(self.mdNextSi)
		self.mdNNB04.aSM(self.mdNextSi)
		self.mdNNN04.aSM(self.mdNextSi)
		self.mdBNB05.aSM(self.mdNextSi)
		self.mdNNN06.aSM(self.mdNextSi)
		self.mdNNB06.aSM(self.mdNextSi)
		self.mdVVB07.aSM(self.mdNextSi)
		self.mdVVV08.aSM(self.mdNextSi)
		self.mdBNB01.aSM(self.mdDecSegBNB)
		self.mdBNB02.aSM(self.mdDecSegBNB)
		self.mdBNB03.aSM(self.mdDecSegBNB)
		self.mdBNB04.aSM(self.mdDecSegBNB)
		self.mdBNB05.aSM(self.mdDecSegBNB)
		self.mdBNB06.aSM(self.mdDecSegBNB)
		self.mdVVB07.aSM(self.mdDecSegVVB)
		self.mdVVB08.aSM(self.mdDecSegVVB)
		self.mdP00.aSM(self.mdDecApCerr)
		self.mdP01.aSM(self.mdDecApCerr)
		self.mdP02.aSM(self.mdDecApAbi)
		self.mdP03.aSM(self.mdDecApAbi)
		self.mdP04.aSM(self.mdDecApAbi)
		self.mdP05.aSM(self.mdDecApAbi)
		self.mdP06.aSM(self.mdDecApAbi)
		self.mdP07.aSM(self.mdDecApAbi)
		self.mdP08.aSM(self.mdDecApAbi)

'''
motorIzq = Motor('A')
motorDer = Motor('B')

def ruedas():
    global model
    global motorIzq,motorDer

    if model.prRdIzq.selV == model.vlRdIzq_Fw:
        motorIzq.start(100)
    else:
        if model.prRdIzq.selV == model.vlRdIzq_Bw:
            motorIzq.start(-100)
        else:
            motorIzq.stop()    

    if model.prRdDer.selV == model.vlRdDer_Fw:
        motorDer.start(100)
    else:
        if model.prRdDer.selV == model.vlRdDer_Bw:
            motorDer.start(-100)
        else:
            motorDer.stop()

def para_todo():
    motorIzq.stop()
    motorDer.stop()
'''
model = csysWROPR()



# Mostramos información del modelo
print("Nombre de modelo:",model.root.name)

# Seleccionamos el modo de misión Normal
model.root.sM(model.mdMisionNormal)
print("\n\n\nModo actual de la misión:",model.root.selM.name)

fin = False

# Iteramos por todos los tramos
for t in model.root.selM.submodes:
    tr = model.root.selM.submodes[t]
    model.sysTr.sM(tr)
    print("\n\n\nTramo actual:",t)
    # Iteramos todas las situaciones posibles del tramo
    for d in tr.submodes:
        dr = tr.submodes[d]
        model.sysSit.sM(dr)
        print("Situación actual:",model.sysSit.selM.name)
        print("Decisión actual movilidad:",model.sysDecMov.selM.name)
        print("Decisión actual aparejo:",model.sysDecAp.selM.name)
        print("Decisión actual siguiente paso:",model.sysNext.selM.name)
        print("Ruedas: ",model.prRdDer.selV.name,model.prRdIzq.selV.name)
        #ruedas()

hub = PrimeHub()

hub.light_matrix.show_image('HAPPY')

#para_todo()