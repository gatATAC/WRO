
from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

hub = PrimeHub()

hub.light_matrix.show_image('HAPPY')

debug = False

class PORIS:
    myclassname = "PORIS"
    id = None
    idx = None
    ident = None
    name = None
    description = None
    parent = None
    def __init__(self,name):
        self.name = name


class PORISValue(PORIS):
    myclassname = "PORISValue"

class PORISValueFloat(PORISValue):
    myclassname = "PORISValueFloat"
    data = None
    min = None
    max = None
    default_data = None

    def setData(self,floatdata):
        if debug:
            print("Applying", floatdata, "name:", self.name, "min:", self.min, "max:", self.max)

        if floatdata >= self.min:
            if floatdata <= max:
                self.data = floatdata

        return self.data

class PORISValueText(PORISValue):
    myclassname = "PORISValueText"
    data = None
    default_data = None

    def setData(self,strdata):
        self.data = strdata

        return self.data

class PORISMode(PORIS):

    def __init__(self,name):
        super(PORISMode, self).__init__(name)
        self.values = {}
        self.submodes = {}

    def addSubMode(self,m):
        self.submodes[m.name] = m

    def addValue(self,v):
        self.values[v.name] = v

    def getEligibleValue(self,v,current):
        if debug:
            if (v != None):
                print("Entro en PORISMode getEligibleValue para el modo", self.name, "con valor propuesto", v.name)
            else:
                print("Entro en PORISMode getEligibleValue para el modo", self.name, "con valor propuesto NULO")

            print(self.values.keys())

        ret = None
        if v.name in self.values.keys():
            ret = v
        else:
            if current.name in self.values.keys():
                ret = current
            else:
                itk = list(self.values.keys())[0]
                ret = self.values[itk]

        return ret

    def getEligibleSubMode(self,m,current):
        if debug:
            print("Entro en PORISMode getEligibleSubMode para el modo", self.name, "con m =", m.name)

        ret = None
        found = False

        if debug:
            print(self.submodes.keys())

        if m.name in self.submodes.keys():
            ret = m

        else:
            if current.name in self.submodes.keys():
                ret = current

            else:
                # If none of two are found, search the first submode with the same parent
                if debug:
                    print("Pruebo aqui",self.submodes.keys())

                for ks in self.submodes.keys():
                    s = self.submodes[ks]
                    if debug:
                        print(s.name,s.parent.name)

                    if s.parent == m.parent:
                        ret = s
                        break

        return ret

    def getEligibleValueFromIdx(self,idx,current):
        vk = list(self.values.keys())[idx]
        result = self.getEligibleValue(self.values[vk],current)
        if result is None:
            ret = 0
        else:
            ret = result.idx

        return ret

    def getEligibleSubModeFromIdx(self,idx,current):
        mk = list(self.submodes.keys())[idx]
        result = self.getEligibleSubMode(self.submodes[mk],current)
        if result is None:
            ret = 0
        else:
            ret = result.idx

        return ret

class PORISNode(PORIS):
    selectedMode = None

    def __init__(self,name):
        super(PORISNode, self).__init__(name)
        self.modes = {}


    def addMode(self,m):
        self.modes[m.name] = m
        m.parent = self
        if self.selectedMode == None:
            self.selectedMode = m

    def init(self):
        if debug:
            print("Init de",self.name,", número de modos:" , len(self.modes))

        firstMode = list(self.modes.keys())[0]
        if debug:
            print("Init ", self.name + ":",firstMode.name)

        self.setMode(firstMode)

    def setEligibleMode(self):
        if debug:
            print("Entro en PORISNode setEligibleMode", self.name)

        if self.selectedMode is None:
            if debug:
                print("- selectedMode es NULO")

            self.init()

        if debug:
            print("- selectedMode es ahora", self.selectedMode.name)

        # TODO: Check if this setMode is redundant
        return self.setMode(self.selectedMode)

    def setMode(self,m):
        return None

    def setModeFromIdx(self,idx):
        mk = list(self.modes.keys())[idx]
        result = self.setMode(self.modes[mk])
        if result is None:
            ret = 0
        else:
            ret = result.idx

        if debug:
            print("Acaba la operación setMode con resultado", ret)

        return ret

    def getEligibleMode(self,m):
        if debug:
            print("Entro en PORISNode ",self.name, ".getEligibleMode("+m.name+")")

        ret = None
        if self.parent is None:
            if debug:
                print("El padre de", self.name, "es nulo")

            ret = m

        else:
            if debug:
                print("Buscamos entre los", len(self.parent.selectedMode.submodes),"submodos de",self.parent.name)
                print("selectedMode",self.selectedMode.name,m.name)

            ret = self.parent.selectedMode.getEligibleSubMode(m,self.selectedMode)

        if ret is None:
            if debug:
                print("No hubo suerte, el modo a seleccionar es nulo")

        else:
            if debug:
                print("El modo seleccionado es",ret.name)

        return ret


    def getEligibleModeFromIdx(self,idx):
        mk = list(self.modes.keys())[idx]
        result = self.getEligibleMode(self.submodes[mk])
        if result is None:
            ret = 0
        else:
            ret = result.idx

        return ret

    def getModeFromName(self,name):
        ret = None
        if name in self.modes.keys():
            ret = self.modes[name]

        return ret


class PORISParam(PORISNode):
    selectedValue = None

    def __init__(self,name):
        super(PORISParam, self).__init__(name)
        self.values = {}

    def addValue(self,v):
        self.values[v.name] = v
        v.parent = self
        if self.selectedValue == None:
            self.selectedValue = v

    def setEligibleValue(self):
        if debug:
            print("Entro en PORISParam setEligibleValue", self.name)

        return self.setValue(self.selectedValue)

    def setMode(self,m):
        if debug:
            print("Entro en Param",self.name+".setMode("+ m.name+"\")")

        ret = self.getEligibleMode(m)

        if debug:
            print("Estoy en",self.name)
            print(list(self.modes.keys()))

        if ret is None:
            mk = list(self.modes.keys())[0]
            ret = self.modes[mk]

        if ret != self.selectedMode:
            self.selectedMode = ret
            self.setValue(self.selectedValue)

        return ret

    def getValueFromName(self,name):
        ret = None
        if name in self.values.keys():
            ret = self.values[name]

        return ret

    def getEligibleValue(self,v,current):
        if debug:
            if v is None:
                print("Entro en PORISParam getEligibleValue ", self.name, "con valor NULO")
            else:
                print("Entro en PORISParam getEligibleValue ", self.name, "con valor", v.name)

            print("***",self.name,self.selectedMode.name,self.modes)

        ret = None

        if self.selectedMode is None:
            if debug:
                print("- selectedMode es NULO")

            self.init()

        ret = self.selectedMode.getEligibleValue(v,current)

        return ret

    def setValue(self,v):
        if debug:
            if v is None:
                print("Entro en PORISParam setValue", self.name, "con valor NULO")
            else:
                print("Entro en PORISParam setValue", self.name, "con valor", v.name)

        ret = self.getEligibleValue(v,self.selectedValue)
        if ret != self.selectedValue:
            self.selectedValue = ret

        return ret

    def getEligibleValueFromIdx(self,idx,current):
        vk = list(self.values.keys())[idx]
        result = self.getEligibleValue(self.values[vk],current)
        if result is None:
            ret = 0
        else:
            ret = result.idx

        return ret

    def setValueFromIdx(self,idx):
        vk = list(self.values.keys())[idx]
        result = self.setValue(self.values[vk])
        if result is None:
            ret = 0
        else:
            ret = result.idx

        return ret


class PORISSys(PORISNode):

    def __init__(self,name):
        super(PORISSys, self).__init__(name)
        self.params = {}
        self.subsystems = {}

    def addParam(self,p):
        self.params[p.name] = p
        p.parent = self

    def addSubsystem(self,s):
        self.subsystems[s.name] = s
        s.parent = self

    def setMode(self,m):
        if debug:
            print("Entro en Sys setMode de", self.name, "con modo", m.name)

        ret = self.getEligibleMode(m)
        if ret is None:
            if debug:
                print("el nuevo modo es NULO que es diferente del seleccionado")
                print(" Hemos de poner el modo UNKNOWN, que por defecto es el primero")

            mk = list(self.modes.keys())[0]
            ret = self.modes[mk]

        if ret != self.selectedMode:
            if debug:
                print("el nuevo modo es", ret.name)
                if self.selectedMode is not None:
                    print (" que es diferente de",self.selectedMode.name)
                else:
                    print(" que es diferente de NULO")

            self.selectedMode = ret

            for k in self.params.keys():
                p = self.params[k]
                p.setEligibleMode()

            for k in self.subsystems.keys():
                s = self.subsystems[k]
                s.setEligibleMode()

        else:
            if debug:
                print("el modo escogido es el mismo", ret.name)

        if debug:
            print("Salgo de Sys setMode de", self.name, "con m="+m.name, "y resultado =",ret.name)

        return ret


    def getSubSystemFromName(self,name):
        ret = None
        if name in self.subsystems.keys():
            ret = self.subsystems[name]

        return ret

    def getSubParamFromName(self,name):
        ret = None
        if name in self.params.keys():
            ret = self.params[name]

        return ret

    def getDescendantFromName(self,name):
        ret = self.getSubSystemFromName(name)
        if ret is None:
            for sk in self.subsystems.keys():
                s = self.subsystems[sk]
                ret = s.getDescendantFromName(name)
                if ret is not None:
                    break

        return ret

    def getDescendantParamFromName(self,name):
        ret = self.getSubParamFromName(name)
        if ret is None:
            print("no es un hijo directo")
            print(name,self.name,self.subsystems)
            for sk in self.subsystems.keys():
                if debug:
                    print(sk)

                s = self.subsystems[sk]
                ret = s.getDescendantParamFromName(name)
                if ret is not None:
                    if debug:
                        print("Tenemos",ret)

                    break

        return ret


class csysWROPORIS:
    def __init__(self):
        self.sysMision = PORISSys("Mision")
        self.mdMisionUNKNOWN = PORISMode("UNKNOWN")
        self.root = self.sysMision
        self.mdMisionNormal = PORISMode("Normal")
        self.sysTramo = PORISSys("Tramo")
        self.mdTramoUNKNOWN = PORISMode("UNKNOWN")
        self.mdTramoP00_SituarBNB_finBNB_Avanzar = PORISMode("P00_SituarBNB_finBNB_Avanzar")
        self.mdTramoP01_SeguirBNB_finder_giroder_abrir = PORISMode("P01_SeguirBNB_finder_giroder_abrir")
        self.mdTramoP02_SeguirBNB_finder_giroder = PORISMode("P02_SeguirBNB_finder_giroder")
        self.mdTramoP03_SeguirBNB_finizq_giroizq = PORISMode("P03_SeguirBNB_finizq_giroizq")
        self.mdTramoP04_SeguirBNB_fincruce_rect = PORISMode("P04_SeguirBNB_fincruce_rect")
        self.mdTramoP05_SeguirNNB_finBNB_rect = PORISMode("P05_SeguirNNB_finBNB_rect")
        self.mdTramoP06_SeguirBNB_finizq_giroder = PORISMode("P06_SeguirBNB_finizq_giroder")
        self.mdTramoP07_SituarVVB_finVVB_Avanzar = PORISMode("P07_SituarVVB_finVVB_Avanzar")
        self.mdTramoP08_SeguirVVB_finVVV_giroder = PORISMode("P08_SeguirVVB_finVVV_giroder")
        self.sysSituacion = PORISSys("Situacion")
        self.mdSituacionUNKNOWN = PORISMode("UNKNOWN")
        self.mdSituacionBNN_00 = PORISMode("BNN_00")
        self.mdSituacionNBB_00 = PORISMode("NBB_00")
        self.mdSituacionBBB_00 = PORISMode("BBB_00")
        self.mdSituacionNNB_00 = PORISMode("NNB_00")
        self.mdSituacionBNB_00 = PORISMode("BNB_00")
        self.mdSituacionNBN_00 = PORISMode("NBN_00")
        self.mdSituacionBBN_00 = PORISMode("BBN_00")
        self.mdSituacionNNN_00 = PORISMode("NNN_00")
        self.mdSituacionNBV_01 = PORISMode("NBV_01")
        self.mdSituacionBNB_01 = PORISMode("BNB_01")
        self.mdSituacionBBB_01 = PORISMode("BBB_01")
        self.mdSituacionBNN_01 = PORISMode("BNN_01")
        self.mdSituacionNBB_01 = PORISMode("NBB_01")
        self.mdSituacionNNB_01 = PORISMode("NNB_01")
        self.mdSituacionVBN_01 = PORISMode("VBN_01")
        self.mdSituacionBBN_01 = PORISMode("BBN_01")
        self.mdSituacionNNN_01 = PORISMode("NNN_01")
        self.mdSituacionNBN_01 = PORISMode("NBN_01")
        self.mdSituacionBBB_02 = PORISMode("BBB_02")
        self.mdSituacionBBN_02 = PORISMode("BBN_02")
        self.mdSituacionBNB_02 = PORISMode("BNB_02")
        self.mdSituacionBNN_02 = PORISMode("BNN_02")
        self.mdSituacionNBB_02 = PORISMode("NBB_02")
        self.mdSituacionNBN_02 = PORISMode("NBN_02")
        self.mdSituacionNBV_02 = PORISMode("NBV_02")
        self.mdSituacionNNB_02 = PORISMode("NNB_02")
        self.mdSituacionNNN_02 = PORISMode("NNN_02")
        self.mdSituacionVBN_02 = PORISMode("VBN_02")
        self.mdSituacionBBB_03 = PORISMode("BBB_03")
        self.mdSituacionBBN_03 = PORISMode("BBN_03")
        self.mdSituacionBNB_03 = PORISMode("BNB_03")
        self.mdSituacionBNN_03 = PORISMode("BNN_03")
        self.mdSituacionNBB_03 = PORISMode("NBB_03")
        self.mdSituacionNBN_03 = PORISMode("NBN_03")
        self.mdSituacionNBV_03 = PORISMode("NBV_03")
        self.mdSituacionNNB_03 = PORISMode("NNB_03")
        self.mdSituacionNNN_03 = PORISMode("NNN_03")
        self.mdSituacionVBN_03 = PORISMode("VBN_03")
        self.mdSituacionBBB_04 = PORISMode("BBB_04")
        self.mdSituacionBBN_04 = PORISMode("BBN_04")
        self.mdSituacionBNB_04 = PORISMode("BNB_04")
        self.mdSituacionBNN_04 = PORISMode("BNN_04")
        self.mdSituacionNBB_04 = PORISMode("NBB_04")
        self.mdSituacionNBN_04 = PORISMode("NBN_04")
        self.mdSituacionNBV_04 = PORISMode("NBV_04")
        self.mdSituacionNNB_04 = PORISMode("NNB_04")
        self.mdSituacionNNN_04 = PORISMode("NNN_04")
        self.mdSituacionVBN_04 = PORISMode("VBN_04")
        self.mdSituacionBBB_05 = PORISMode("BBB_05")
        self.mdSituacionBBN_05 = PORISMode("BBN_05")
        self.mdSituacionBNB_05 = PORISMode("BNB_05")
        self.mdSituacionBNN_05 = PORISMode("BNN_05")
        self.mdSituacionNBB_05 = PORISMode("NBB_05")
        self.mdSituacionNBN_05 = PORISMode("NBN_05")
        self.mdSituacionNNB_05 = PORISMode("NNB_05")
        self.mdSituacionNNN_05 = PORISMode("NNN_05")
        self.mdSituacionVBN_06 = PORISMode("VBN_06")
        self.mdSituacionNBB_06 = PORISMode("NBB_06")
        self.mdSituacionBNB_06 = PORISMode("BNB_06")
        self.mdSituacionNBN_06 = PORISMode("NBN_06")
        self.mdSituacionNNN_06 = PORISMode("NNN_06")
        self.mdSituacionBNN_06 = PORISMode("BNN_06")
        self.mdSituacionBBN_06 = PORISMode("BBN_06")
        self.mdSituacionBBB_06 = PORISMode("BBB_06")
        self.mdSituacionNBV_06 = PORISMode("NBV_06")
        self.mdSituacionNNB_06 = PORISMode("NNB_06")
        self.mdSituacionBBB_07 = PORISMode("BBB_07")
        self.mdSituacionBBN_07 = PORISMode("BBN_07")
        self.mdSituacionBNB_07 = PORISMode("BNB_07")
        self.mdSituacionBNN_07 = PORISMode("BNN_07")
        self.mdSituacionNBB_07 = PORISMode("NBB_07")
        self.mdSituacionNBN_07 = PORISMode("NBN_07")
        self.mdSituacionNBV_07 = PORISMode("NBV_07")
        self.mdSituacionNNB_07 = PORISMode("NNB_07")
        self.mdSituacionNNN_07 = PORISMode("NNN_07")
        self.mdSituacionVBN_07 = PORISMode("VBN_07")
        self.mdSituacionVVB_07 = PORISMode("VVB_07")
        self.mdSituacionVVV_07 = PORISMode("VVV_07")
        self.mdSituacionVVV_08 = PORISMode("VVV_08")
        self.mdSituacionVBN_08 = PORISMode("VBN_08")
        self.mdSituacionVVB_08 = PORISMode("VVB_08")
        self.sysDecisionMovimiento = PORISSys("DecisionMovimiento")
        self.mdDecisionMovimientoUNKNOWN = PORISMode("UNKNOWN")
        self.mdDecisionMovimientoAvanzar = PORISMode("Avanzar")
        self.mdDecisionMovimientoCompasIzq = PORISMode("CompasIzq")
        self.mdDecisionMovimientoCompasDer = PORISMode("CompasDer")
        self.mdDecisionMovimientoGirarDer = PORISMode("GirarDer")
        self.mdDecisionMovimientoGirarIzq = PORISMode("GirarIzq")
        self.mdDecisionMovimientoParar = PORISMode("Parar")
        self.prRuedaDer = PORISParam("RuedaDer")
        self.mdRuedaDerUNKNOWN = PORISMode("UNKNOWN")
        self.vlRuedaDer_UNKNOWN = PORISValue("UNKNOWN")
        self.mdRuedaDerParada = PORISMode("Parada")
        self.mdRuedaDerAvanzar = PORISMode("Avanzar")
        self.mdRuedaDerRetroceder = PORISMode("Retroceder")
        self.vlRuedaDer_Quieta = PORISValue("Quieta")
        self.vlRuedaDer_Adelante = PORISValue("Adelante")
        self.vlRuedaDer_Atras = PORISValue("Atras")
        self.prRuedaIzq = PORISParam("RuedaIzq")
        self.mdRuedaIzqUNKNOWN = PORISMode("UNKNOWN")
        self.vlRuedaIzq_UNKNOWN = PORISValue("UNKNOWN")
        self.mdRuedaIzqParada = PORISMode("Parada")
        self.mdRuedaIzqAvanzar = PORISMode("Avanzar")
        self.mdRuedaIzqRetroceder = PORISMode("Retroceder")
        self.vlRuedaIzq_Quieta = PORISValue("Quieta")
        self.vlRuedaIzq_Adelante = PORISValue("Adelante")
        self.vlRuedaIzq_Atras = PORISValue("Atras")
        self.sysNuevoPaso = PORISSys("NuevoPaso")
        self.mdNuevoPasoUNKNOWN = PORISMode("UNKNOWN")
        self.mdNuevoPasoNo = PORISMode("No")
        self.mdNuevoPasoSi = PORISMode("Si")
        self.sysDecisionSeguidor = PORISSys("DecisionSeguidor")
        self.mdDecisionSeguidorUNKNOWN = PORISMode("UNKNOWN")
        self.mdDecisionSeguidorBNB = PORISMode("BNB")
        self.mdDecisionSeguidorVVB = PORISMode("VVB")
        self.sysDecisionAparejo = PORISSys("DecisionAparejo")
        self.mdDecisionAparejoUNKNOWN = PORISMode("UNKNOWN")
        self.mdDecisionAparejoAbierto = PORISMode("Abierto")
        self.mdDecisionAparejoMedio = PORISMode("Medio")
        self.mdDecisionAparejoCerrado = PORISMode("Cerrado")
        self.sysMision.addMode(self.mdMisionUNKNOWN)
        self.sysMision.addMode(self.mdMisionNormal)
        self.sysMision.addSubsystem(self.sysTramo)
        self.sysTramo.addMode(self.mdTramoUNKNOWN)
        self.sysTramo.addMode(self.mdTramoP00_SituarBNB_finBNB_Avanzar)
        self.sysTramo.addMode(self.mdTramoP01_SeguirBNB_finder_giroder_abrir)
        self.sysTramo.addMode(self.mdTramoP02_SeguirBNB_finder_giroder)
        self.sysTramo.addMode(self.mdTramoP03_SeguirBNB_finizq_giroizq)
        self.sysTramo.addMode(self.mdTramoP04_SeguirBNB_fincruce_rect)
        self.sysTramo.addMode(self.mdTramoP05_SeguirNNB_finBNB_rect)
        self.sysTramo.addMode(self.mdTramoP06_SeguirBNB_finizq_giroder)
        self.sysTramo.addMode(self.mdTramoP07_SituarVVB_finVVB_Avanzar)
        self.sysTramo.addMode(self.mdTramoP08_SeguirVVB_finVVV_giroder)
        self.sysTramo.addSubsystem(self.sysSituacion)
        self.sysSituacion.addMode(self.mdSituacionUNKNOWN)
        self.sysSituacion.addMode(self.mdSituacionBNN_00)
        self.sysSituacion.addMode(self.mdSituacionNBB_00)
        self.sysSituacion.addMode(self.mdSituacionBBB_00)
        self.sysSituacion.addMode(self.mdSituacionNNB_00)
        self.sysSituacion.addMode(self.mdSituacionBNB_00)
        self.sysSituacion.addMode(self.mdSituacionNBN_00)
        self.sysSituacion.addMode(self.mdSituacionBBN_00)
        self.sysSituacion.addMode(self.mdSituacionNNN_00)
        self.sysSituacion.addMode(self.mdSituacionNBV_01)
        self.sysSituacion.addMode(self.mdSituacionBNB_01)
        self.sysSituacion.addMode(self.mdSituacionBBB_01)
        self.sysSituacion.addMode(self.mdSituacionBNN_01)
        self.sysSituacion.addMode(self.mdSituacionNBB_01)
        self.sysSituacion.addMode(self.mdSituacionNNB_01)
        self.sysSituacion.addMode(self.mdSituacionVBN_01)
        self.sysSituacion.addMode(self.mdSituacionBBN_01)
        self.sysSituacion.addMode(self.mdSituacionNNN_01)
        self.sysSituacion.addMode(self.mdSituacionNBN_01)
        self.sysSituacion.addMode(self.mdSituacionBBB_02)
        self.sysSituacion.addMode(self.mdSituacionBBN_02)
        self.sysSituacion.addMode(self.mdSituacionBNB_02)
        self.sysSituacion.addMode(self.mdSituacionBNN_02)
        self.sysSituacion.addMode(self.mdSituacionNBB_02)
        self.sysSituacion.addMode(self.mdSituacionNBN_02)
        self.sysSituacion.addMode(self.mdSituacionNBV_02)
        self.sysSituacion.addMode(self.mdSituacionNNB_02)
        self.sysSituacion.addMode(self.mdSituacionNNN_02)
        self.sysSituacion.addMode(self.mdSituacionVBN_02)
        self.sysSituacion.addMode(self.mdSituacionBBB_03)
        self.sysSituacion.addMode(self.mdSituacionBBN_03)
        self.sysSituacion.addMode(self.mdSituacionBNB_03)
        self.sysSituacion.addMode(self.mdSituacionBNN_03)
        self.sysSituacion.addMode(self.mdSituacionNBB_03)
        self.sysSituacion.addMode(self.mdSituacionNBN_03)
        self.sysSituacion.addMode(self.mdSituacionNBV_03)
        self.sysSituacion.addMode(self.mdSituacionNNB_03)
        self.sysSituacion.addMode(self.mdSituacionNNN_03)
        self.sysSituacion.addMode(self.mdSituacionVBN_03)
        self.sysSituacion.addMode(self.mdSituacionBBB_04)
        self.sysSituacion.addMode(self.mdSituacionBBN_04)
        self.sysSituacion.addMode(self.mdSituacionBNB_04)
        self.sysSituacion.addMode(self.mdSituacionBNN_04)
        self.sysSituacion.addMode(self.mdSituacionNBB_04)
        self.sysSituacion.addMode(self.mdSituacionNBN_04)
        self.sysSituacion.addMode(self.mdSituacionNBV_04)
        self.sysSituacion.addMode(self.mdSituacionNNB_04)
        self.sysSituacion.addMode(self.mdSituacionNNN_04)
        self.sysSituacion.addMode(self.mdSituacionVBN_04)
        self.sysSituacion.addMode(self.mdSituacionBBB_05)
        self.sysSituacion.addMode(self.mdSituacionBBN_05)
        self.sysSituacion.addMode(self.mdSituacionBNB_05)
        self.sysSituacion.addMode(self.mdSituacionBNN_05)
        self.sysSituacion.addMode(self.mdSituacionNBB_05)
        self.sysSituacion.addMode(self.mdSituacionNBN_05)
        self.sysSituacion.addMode(self.mdSituacionNNB_05)
        self.sysSituacion.addMode(self.mdSituacionNNN_05)
        self.sysSituacion.addMode(self.mdSituacionVBN_06)
        self.sysSituacion.addMode(self.mdSituacionNBB_06)
        self.sysSituacion.addMode(self.mdSituacionBNB_06)
        self.sysSituacion.addMode(self.mdSituacionNBN_06)
        self.sysSituacion.addMode(self.mdSituacionNNN_06)
        self.sysSituacion.addMode(self.mdSituacionBNN_06)
        self.sysSituacion.addMode(self.mdSituacionBBN_06)
        self.sysSituacion.addMode(self.mdSituacionBBB_06)
        self.sysSituacion.addMode(self.mdSituacionNBV_06)
        self.sysSituacion.addMode(self.mdSituacionNNB_06)
        self.sysSituacion.addMode(self.mdSituacionBBB_07)
        self.sysSituacion.addMode(self.mdSituacionBBN_07)
        self.sysSituacion.addMode(self.mdSituacionBNB_07)
        self.sysSituacion.addMode(self.mdSituacionBNN_07)
        self.sysSituacion.addMode(self.mdSituacionNBB_07)
        self.sysSituacion.addMode(self.mdSituacionNBN_07)
        self.sysSituacion.addMode(self.mdSituacionNBV_07)
        self.sysSituacion.addMode(self.mdSituacionNNB_07)
        self.sysSituacion.addMode(self.mdSituacionNNN_07)
        self.sysSituacion.addMode(self.mdSituacionVBN_07)
        self.sysSituacion.addMode(self.mdSituacionVVB_07)
        self.sysSituacion.addMode(self.mdSituacionVVV_07)
        self.sysSituacion.addMode(self.mdSituacionVVV_08)
        self.sysSituacion.addMode(self.mdSituacionVBN_08)
        self.sysSituacion.addMode(self.mdSituacionVVB_08)
        self.sysSituacion.addSubsystem(self.sysDecisionMovimiento)
        self.sysDecisionMovimiento.addMode(self.mdDecisionMovimientoUNKNOWN)
        self.sysDecisionMovimiento.addMode(self.mdDecisionMovimientoAvanzar)
        self.sysDecisionMovimiento.addMode(self.mdDecisionMovimientoCompasIzq)
        self.sysDecisionMovimiento.addMode(self.mdDecisionMovimientoCompasDer)
        self.sysDecisionMovimiento.addMode(self.mdDecisionMovimientoGirarDer)
        self.sysDecisionMovimiento.addMode(self.mdDecisionMovimientoGirarIzq)
        self.sysDecisionMovimiento.addMode(self.mdDecisionMovimientoParar)
        self.sysDecisionMovimiento.addParam(self.prRuedaDer)
        self.prRuedaDer.addValue(self.vlRuedaDer_UNKNOWN)
        self.prRuedaDer.addMode(self.mdRuedaDerUNKNOWN)
        self.mdRuedaDerUNKNOWN.addValue(self.vlRuedaDer_UNKNOWN)
        self.mdDecisionMovimientoUNKNOWN.addSubMode(self.mdRuedaDerUNKNOWN)
        self.prRuedaDer.addMode(self.mdRuedaDerParada)
        self.prRuedaDer.addMode(self.mdRuedaDerAvanzar)
        self.prRuedaDer.addMode(self.mdRuedaDerRetroceder)
        self.prRuedaDer.addValue(self.vlRuedaDer_Quieta)
        self.prRuedaDer.addValue(self.vlRuedaDer_Adelante)
        self.prRuedaDer.addValue(self.vlRuedaDer_Atras)
        self.sysDecisionMovimiento.addParam(self.prRuedaIzq)
        self.prRuedaIzq.addValue(self.vlRuedaIzq_UNKNOWN)
        self.prRuedaIzq.addMode(self.mdRuedaIzqUNKNOWN)
        self.mdRuedaIzqUNKNOWN.addValue(self.vlRuedaIzq_UNKNOWN)
        self.mdDecisionMovimientoUNKNOWN.addSubMode(self.mdRuedaIzqUNKNOWN)
        self.prRuedaIzq.addMode(self.mdRuedaIzqParada)
        self.prRuedaIzq.addMode(self.mdRuedaIzqAvanzar)
        self.prRuedaIzq.addMode(self.mdRuedaIzqRetroceder)
        self.prRuedaIzq.addValue(self.vlRuedaIzq_Quieta)
        self.prRuedaIzq.addValue(self.vlRuedaIzq_Adelante)
        self.prRuedaIzq.addValue(self.vlRuedaIzq_Atras)
        self.sysSituacion.addSubsystem(self.sysNuevoPaso)
        self.sysNuevoPaso.addMode(self.mdNuevoPasoUNKNOWN)
        self.sysNuevoPaso.addMode(self.mdNuevoPasoNo)
        self.sysNuevoPaso.addMode(self.mdNuevoPasoSi)
        self.sysSituacion.addSubsystem(self.sysDecisionSeguidor)
        self.sysDecisionSeguidor.addMode(self.mdDecisionSeguidorUNKNOWN)
        self.sysDecisionSeguidor.addMode(self.mdDecisionSeguidorBNB)
        self.sysDecisionSeguidor.addMode(self.mdDecisionSeguidorVVB)
        self.sysTramo.addSubsystem(self.sysDecisionAparejo)
        self.sysDecisionAparejo.addMode(self.mdDecisionAparejoUNKNOWN)
        self.sysDecisionAparejo.addMode(self.mdDecisionAparejoAbierto)
        self.sysDecisionAparejo.addMode(self.mdDecisionAparejoMedio)
        self.sysDecisionAparejo.addMode(self.mdDecisionAparejoCerrado)
        self.mdMisionNormal.addSubMode(self.mdTramoP00_SituarBNB_finBNB_Avanzar)
        self.mdMisionNormal.addSubMode(self.mdTramoP01_SeguirBNB_finder_giroder_abrir)
        self.mdMisionNormal.addSubMode(self.mdTramoP02_SeguirBNB_finder_giroder)
        self.mdMisionNormal.addSubMode(self.mdTramoP03_SeguirBNB_finizq_giroizq)
        self.mdMisionNormal.addSubMode(self.mdTramoP04_SeguirBNB_fincruce_rect)
        self.mdMisionNormal.addSubMode(self.mdTramoP05_SeguirNNB_finBNB_rect)
        self.mdMisionNormal.addSubMode(self.mdTramoP06_SeguirBNB_finizq_giroder)
        self.mdMisionNormal.addSubMode(self.mdTramoP07_SituarVVB_finVVB_Avanzar)
        self.mdMisionNormal.addSubMode(self.mdTramoP08_SeguirVVB_finVVV_giroder)
        self.mdTramoP00_SituarBNB_finBNB_Avanzar.addSubMode(self.mdSituacionNNB_00)
        self.mdTramoP00_SituarBNB_finBNB_Avanzar.addSubMode(self.mdSituacionBBB_00)
        self.mdTramoP00_SituarBNB_finBNB_Avanzar.addSubMode(self.mdSituacionBNB_00)
        self.mdTramoP00_SituarBNB_finBNB_Avanzar.addSubMode(self.mdSituacionNNN_00)
        self.mdTramoP00_SituarBNB_finBNB_Avanzar.addSubMode(self.mdSituacionBNN_00)
        self.mdTramoP00_SituarBNB_finBNB_Avanzar.addSubMode(self.mdSituacionBBN_00)
        self.mdTramoP00_SituarBNB_finBNB_Avanzar.addSubMode(self.mdSituacionNBB_00)
        self.mdTramoP00_SituarBNB_finBNB_Avanzar.addSubMode(self.mdSituacionNBN_00)
        self.mdTramoP01_SeguirBNB_finder_giroder_abrir.addSubMode(self.mdSituacionNNB_01)
        self.mdTramoP01_SeguirBNB_finder_giroder_abrir.addSubMode(self.mdSituacionBBB_01)
        self.mdTramoP01_SeguirBNB_finder_giroder_abrir.addSubMode(self.mdSituacionBNB_01)
        self.mdTramoP01_SeguirBNB_finder_giroder_abrir.addSubMode(self.mdSituacionNNN_01)
        self.mdTramoP01_SeguirBNB_finder_giroder_abrir.addSubMode(self.mdSituacionBNN_01)
        self.mdTramoP01_SeguirBNB_finder_giroder_abrir.addSubMode(self.mdSituacionBBN_01)
        self.mdTramoP01_SeguirBNB_finder_giroder_abrir.addSubMode(self.mdSituacionNBB_01)
        self.mdTramoP01_SeguirBNB_finder_giroder_abrir.addSubMode(self.mdSituacionNBN_01)
        self.mdTramoP01_SeguirBNB_finder_giroder_abrir.addSubMode(self.mdSituacionVBN_01)
        self.mdTramoP01_SeguirBNB_finder_giroder_abrir.addSubMode(self.mdSituacionNBV_01)
        self.mdTramoP02_SeguirBNB_finder_giroder.addSubMode(self.mdSituacionNNB_02)
        self.mdTramoP02_SeguirBNB_finder_giroder.addSubMode(self.mdSituacionBBB_02)
        self.mdTramoP02_SeguirBNB_finder_giroder.addSubMode(self.mdSituacionBNB_02)
        self.mdTramoP02_SeguirBNB_finder_giroder.addSubMode(self.mdSituacionNNN_02)
        self.mdTramoP02_SeguirBNB_finder_giroder.addSubMode(self.mdSituacionBNN_02)
        self.mdTramoP02_SeguirBNB_finder_giroder.addSubMode(self.mdSituacionBBN_02)
        self.mdTramoP02_SeguirBNB_finder_giroder.addSubMode(self.mdSituacionNBB_02)
        self.mdTramoP02_SeguirBNB_finder_giroder.addSubMode(self.mdSituacionNBN_02)
        self.mdTramoP02_SeguirBNB_finder_giroder.addSubMode(self.mdSituacionNBV_02)
        self.mdTramoP02_SeguirBNB_finder_giroder.addSubMode(self.mdSituacionVBN_02)
        self.mdTramoP03_SeguirBNB_finizq_giroizq.addSubMode(self.mdSituacionBNN_03)
        self.mdTramoP03_SeguirBNB_finizq_giroizq.addSubMode(self.mdSituacionBBB_03)
        self.mdTramoP03_SeguirBNB_finizq_giroizq.addSubMode(self.mdSituacionBNB_03)
        self.mdTramoP03_SeguirBNB_finizq_giroizq.addSubMode(self.mdSituacionNNN_03)
        self.mdTramoP03_SeguirBNB_finizq_giroizq.addSubMode(self.mdSituacionNNB_03)
        self.mdTramoP03_SeguirBNB_finizq_giroizq.addSubMode(self.mdSituacionBBN_03)
        self.mdTramoP03_SeguirBNB_finizq_giroizq.addSubMode(self.mdSituacionNBB_03)
        self.mdTramoP03_SeguirBNB_finizq_giroizq.addSubMode(self.mdSituacionNBN_03)
        self.mdTramoP03_SeguirBNB_finizq_giroizq.addSubMode(self.mdSituacionNBV_03)
        self.mdTramoP03_SeguirBNB_finizq_giroizq.addSubMode(self.mdSituacionVBN_03)
        self.mdTramoP04_SeguirBNB_fincruce_rect.addSubMode(self.mdSituacionBNN_04)
        self.mdTramoP04_SeguirBNB_fincruce_rect.addSubMode(self.mdSituacionBBB_04)
        self.mdTramoP04_SeguirBNB_fincruce_rect.addSubMode(self.mdSituacionBNB_04)
        self.mdTramoP04_SeguirBNB_fincruce_rect.addSubMode(self.mdSituacionNNN_04)
        self.mdTramoP04_SeguirBNB_fincruce_rect.addSubMode(self.mdSituacionNNB_04)
        self.mdTramoP04_SeguirBNB_fincruce_rect.addSubMode(self.mdSituacionBBN_04)
        self.mdTramoP04_SeguirBNB_fincruce_rect.addSubMode(self.mdSituacionNBB_04)
        self.mdTramoP04_SeguirBNB_fincruce_rect.addSubMode(self.mdSituacionNBN_04)
        self.mdTramoP04_SeguirBNB_fincruce_rect.addSubMode(self.mdSituacionNBV_04)
        self.mdTramoP04_SeguirBNB_fincruce_rect.addSubMode(self.mdSituacionVBN_04)
        self.mdTramoP05_SeguirNNB_finBNB_rect.addSubMode(self.mdSituacionBNN_05)
        self.mdTramoP05_SeguirNNB_finBNB_rect.addSubMode(self.mdSituacionBBB_05)
        self.mdTramoP05_SeguirNNB_finBNB_rect.addSubMode(self.mdSituacionBNB_05)
        self.mdTramoP05_SeguirNNB_finBNB_rect.addSubMode(self.mdSituacionNNN_05)
        self.mdTramoP05_SeguirNNB_finBNB_rect.addSubMode(self.mdSituacionNNB_05)
        self.mdTramoP05_SeguirNNB_finBNB_rect.addSubMode(self.mdSituacionBBN_05)
        self.mdTramoP05_SeguirNNB_finBNB_rect.addSubMode(self.mdSituacionNBB_05)
        self.mdTramoP05_SeguirNNB_finBNB_rect.addSubMode(self.mdSituacionNBN_05)
        self.mdTramoP06_SeguirBNB_finizq_giroder.addSubMode(self.mdSituacionBNN_06)
        self.mdTramoP06_SeguirBNB_finizq_giroder.addSubMode(self.mdSituacionBBB_06)
        self.mdTramoP06_SeguirBNB_finizq_giroder.addSubMode(self.mdSituacionBNB_06)
        self.mdTramoP06_SeguirBNB_finizq_giroder.addSubMode(self.mdSituacionNNN_06)
        self.mdTramoP06_SeguirBNB_finizq_giroder.addSubMode(self.mdSituacionNNB_06)
        self.mdTramoP06_SeguirBNB_finizq_giroder.addSubMode(self.mdSituacionBBN_06)
        self.mdTramoP06_SeguirBNB_finizq_giroder.addSubMode(self.mdSituacionNBB_06)
        self.mdTramoP06_SeguirBNB_finizq_giroder.addSubMode(self.mdSituacionNBN_06)
        self.mdTramoP06_SeguirBNB_finizq_giroder.addSubMode(self.mdSituacionNBV_06)
        self.mdTramoP07_SituarVVB_finVVB_Avanzar.addSubMode(self.mdSituacionBNN_07)
        self.mdTramoP07_SituarVVB_finVVB_Avanzar.addSubMode(self.mdSituacionBBB_07)
        self.mdTramoP07_SituarVVB_finVVB_Avanzar.addSubMode(self.mdSituacionBNB_07)
        self.mdTramoP07_SituarVVB_finVVB_Avanzar.addSubMode(self.mdSituacionNNN_07)
        self.mdTramoP07_SituarVVB_finVVB_Avanzar.addSubMode(self.mdSituacionNNB_07)
        self.mdTramoP07_SituarVVB_finVVB_Avanzar.addSubMode(self.mdSituacionBBN_07)
        self.mdTramoP07_SituarVVB_finVVB_Avanzar.addSubMode(self.mdSituacionNBB_07)
        self.mdTramoP07_SituarVVB_finVVB_Avanzar.addSubMode(self.mdSituacionNBN_07)
        self.mdTramoP07_SituarVVB_finVVB_Avanzar.addSubMode(self.mdSituacionVBN_07)
        self.mdTramoP07_SituarVVB_finVVB_Avanzar.addSubMode(self.mdSituacionVVB_07)
        self.mdTramoP07_SituarVVB_finVVB_Avanzar.addSubMode(self.mdSituacionVVV_07)
        self.mdTramoP07_SituarVVB_finVVB_Avanzar.addSubMode(self.mdSituacionNBV_07)
        self.mdTramoP08_SeguirVVB_finVVV_giroder.addSubMode(self.mdSituacionVBN_08)
        self.mdTramoP08_SeguirVVB_finVVV_giroder.addSubMode(self.mdSituacionVVB_08)
        self.mdTramoP08_SeguirVVB_finVVV_giroder.addSubMode(self.mdSituacionVVV_08)
        self.mdSituacionBNN_00.addSubMode(self.mdDecisionMovimientoCompasDer)
        self.mdSituacionNBB_00.addSubMode(self.mdDecisionMovimientoCompasIzq)
        self.mdSituacionBBB_00.addSubMode(self.mdDecisionMovimientoAvanzar)
        self.mdSituacionNNB_00.addSubMode(self.mdDecisionMovimientoCompasIzq)
        self.mdSituacionBNB_00.addSubMode(self.mdDecisionMovimientoAvanzar)
        self.mdSituacionNBN_00.addSubMode(self.mdDecisionMovimientoAvanzar)
        self.mdSituacionBBN_00.addSubMode(self.mdDecisionMovimientoCompasDer)
        self.mdSituacionNNN_00.addSubMode(self.mdDecisionMovimientoAvanzar)
        self.mdSituacionNBV_01.addSubMode(self.mdDecisionMovimientoGirarIzq)
        self.mdSituacionBNB_01.addSubMode(self.mdDecisionMovimientoAvanzar)
        self.mdSituacionBBB_01.addSubMode(self.mdDecisionMovimientoParar)
        self.mdSituacionBNN_01.addSubMode(self.mdDecisionMovimientoGirarDer)
        self.mdSituacionNBB_01.addSubMode(self.mdDecisionMovimientoCompasIzq)
        self.mdSituacionNNB_01.addSubMode(self.mdDecisionMovimientoCompasIzq)
        self.mdSituacionVBN_01.addSubMode(self.mdDecisionMovimientoGirarDer)
        self.mdSituacionBBN_01.addSubMode(self.mdDecisionMovimientoCompasDer)
        self.mdSituacionNNN_01.addSubMode(self.mdDecisionMovimientoGirarDer)
        self.mdSituacionNBN_01.addSubMode(self.mdDecisionMovimientoParar)
        self.mdSituacionBBB_02.addSubMode(self.mdDecisionMovimientoParar)
        self.mdSituacionBBN_02.addSubMode(self.mdDecisionMovimientoCompasDer)
        self.mdSituacionBNB_02.addSubMode(self.mdDecisionMovimientoAvanzar)
        self.mdSituacionBNN_02.addSubMode(self.mdDecisionMovimientoGirarDer)
        self.mdSituacionNBB_02.addSubMode(self.mdDecisionMovimientoCompasIzq)
        self.mdSituacionNBN_02.addSubMode(self.mdDecisionMovimientoAvanzar)
        self.mdSituacionNBV_02.addSubMode(self.mdDecisionMovimientoGirarIzq)
        self.mdSituacionNNB_02.addSubMode(self.mdDecisionMovimientoCompasIzq)
        self.mdSituacionNNN_02.addSubMode(self.mdDecisionMovimientoGirarDer)
        self.mdSituacionVBN_02.addSubMode(self.mdDecisionMovimientoGirarDer)
        self.mdSituacionBBB_03.addSubMode(self.mdDecisionMovimientoParar)
        self.mdSituacionBBN_03.addSubMode(self.mdDecisionMovimientoCompasDer)
        self.mdSituacionBNB_03.addSubMode(self.mdDecisionMovimientoAvanzar)
        self.mdSituacionBNN_03.addSubMode(self.mdDecisionMovimientoCompasDer)
        self.mdSituacionNBB_03.addSubMode(self.mdDecisionMovimientoCompasIzq)
        self.mdSituacionNBN_03.addSubMode(self.mdDecisionMovimientoParar)
        self.mdSituacionNBV_03.addSubMode(self.mdDecisionMovimientoGirarIzq)
        self.mdSituacionNNB_03.addSubMode(self.mdDecisionMovimientoGirarIzq)
        self.mdSituacionNNN_03.addSubMode(self.mdDecisionMovimientoGirarIzq)
        self.mdSituacionVBN_03.addSubMode(self.mdDecisionMovimientoGirarDer)
        self.mdSituacionBBB_04.addSubMode(self.mdDecisionMovimientoCompasDer)
        self.mdSituacionBBN_04.addSubMode(self.mdDecisionMovimientoCompasDer)
        self.mdSituacionBNB_04.addSubMode(self.mdDecisionMovimientoAvanzar)
        self.mdSituacionBNN_04.addSubMode(self.mdDecisionMovimientoCompasDer)
        self.mdSituacionNBB_04.addSubMode(self.mdDecisionMovimientoCompasIzq)
        self.mdSituacionNBN_04.addSubMode(self.mdDecisionMovimientoParar)
        self.mdSituacionNBV_04.addSubMode(self.mdDecisionMovimientoGirarIzq)
        self.mdSituacionNNB_04.addSubMode(self.mdDecisionMovimientoAvanzar)
        self.mdSituacionNNN_04.addSubMode(self.mdDecisionMovimientoCompasDer)
        self.mdSituacionVBN_04.addSubMode(self.mdDecisionMovimientoGirarDer)
        self.mdSituacionBBB_05.addSubMode(self.mdDecisionMovimientoParar)
        self.mdSituacionBBN_05.addSubMode(self.mdDecisionMovimientoCompasDer)
        self.mdSituacionBNB_05.addSubMode(self.mdDecisionMovimientoAvanzar)
        self.mdSituacionBNN_05.addSubMode(self.mdDecisionMovimientoCompasDer)
        self.mdSituacionNBB_05.addSubMode(self.mdDecisionMovimientoCompasIzq)
        self.mdSituacionNBN_05.addSubMode(self.mdDecisionMovimientoCompasDer)
        self.mdSituacionNNB_05.addSubMode(self.mdDecisionMovimientoAvanzar)
        self.mdSituacionNNN_05.addSubMode(self.mdDecisionMovimientoCompasDer)
        self.mdSituacionVBN_06.addSubMode(self.mdDecisionMovimientoGirarDer)
        self.mdSituacionNBB_06.addSubMode(self.mdDecisionMovimientoCompasIzq)
        self.mdSituacionBNB_06.addSubMode(self.mdDecisionMovimientoAvanzar)
        self.mdSituacionNBN_06.addSubMode(self.mdDecisionMovimientoParar)
        self.mdSituacionNNN_06.addSubMode(self.mdDecisionMovimientoGirarDer)
        self.mdSituacionBNN_06.addSubMode(self.mdDecisionMovimientoCompasDer)
        self.mdSituacionBBN_06.addSubMode(self.mdDecisionMovimientoCompasDer)
        self.mdSituacionBBB_06.addSubMode(self.mdDecisionMovimientoParar)
        self.mdSituacionNBV_06.addSubMode(self.mdDecisionMovimientoGirarIzq)
        self.mdSituacionNNB_06.addSubMode(self.mdDecisionMovimientoGirarDer)
        self.mdSituacionBBB_07.addSubMode(self.mdDecisionMovimientoGirarDer)
        self.mdSituacionBBN_07.addSubMode(self.mdDecisionMovimientoGirarDer)
        self.mdSituacionBNB_07.addSubMode(self.mdDecisionMovimientoGirarIzq)
        self.mdSituacionBNN_07.addSubMode(self.mdDecisionMovimientoGirarIzq)
        self.mdSituacionNBB_07.addSubMode(self.mdDecisionMovimientoGirarDer)
        self.mdSituacionNBN_07.addSubMode(self.mdDecisionMovimientoGirarDer)
        self.mdSituacionNBV_07.addSubMode(self.mdDecisionMovimientoParar)
        self.mdSituacionNNB_07.addSubMode(self.mdDecisionMovimientoGirarDer)
        self.mdSituacionNNN_07.addSubMode(self.mdDecisionMovimientoGirarDer)
        self.mdSituacionVBN_07.addSubMode(self.mdDecisionMovimientoCompasIzq)
        self.mdSituacionVVB_07.addSubMode(self.mdDecisionMovimientoAvanzar)
        self.mdSituacionVVV_07.addSubMode(self.mdDecisionMovimientoGirarDer)
        self.mdSituacionVVV_08.addSubMode(self.mdDecisionMovimientoGirarDer)
        self.mdSituacionVBN_08.addSubMode(self.mdDecisionMovimientoCompasIzq)
        self.mdSituacionVVB_08.addSubMode(self.mdDecisionMovimientoAvanzar)
        self.mdDecisionMovimientoAvanzar.addSubMode(self.mdRuedaDerAvanzar)
        self.mdDecisionMovimientoCompasIzq.addSubMode(self.mdRuedaDerAvanzar)
        self.mdDecisionMovimientoCompasDer.addSubMode(self.mdRuedaDerParada)
        self.mdDecisionMovimientoGirarDer.addSubMode(self.mdRuedaDerRetroceder)
        self.mdDecisionMovimientoGirarIzq.addSubMode(self.mdRuedaDerAvanzar)
        self.mdDecisionMovimientoParar.addSubMode(self.mdRuedaDerParada)
        self.mdRuedaDerParada.addValue(self.vlRuedaDer_Quieta)
        self.mdRuedaDerAvanzar.addValue(self.vlRuedaDer_Adelante)
        self.mdRuedaDerRetroceder.addValue(self.vlRuedaDer_Atras)
        self.mdDecisionMovimientoAvanzar.addSubMode(self.mdRuedaIzqAvanzar)
        self.mdDecisionMovimientoCompasIzq.addSubMode(self.mdRuedaIzqParada)
        self.mdDecisionMovimientoCompasDer.addSubMode(self.mdRuedaIzqAvanzar)
        self.mdDecisionMovimientoGirarDer.addSubMode(self.mdRuedaIzqAvanzar)
        self.mdDecisionMovimientoGirarIzq.addSubMode(self.mdRuedaIzqRetroceder)
        self.mdDecisionMovimientoParar.addSubMode(self.mdRuedaIzqParada)
        self.mdRuedaIzqParada.addValue(self.vlRuedaIzq_Quieta)
        self.mdRuedaIzqAvanzar.addValue(self.vlRuedaIzq_Adelante)
        self.mdRuedaIzqRetroceder.addValue(self.vlRuedaIzq_Atras)
        self.mdSituacionBNN_00.addSubMode(self.mdNuevoPasoNo)
        self.mdSituacionNBB_00.addSubMode(self.mdNuevoPasoNo)
        self.mdSituacionBBB_00.addSubMode(self.mdNuevoPasoNo)
        self.mdSituacionNNB_00.addSubMode(self.mdNuevoPasoNo)
        self.mdSituacionBNB_00.addSubMode(self.mdNuevoPasoSi)
        self.mdSituacionNBN_00.addSubMode(self.mdNuevoPasoNo)
        self.mdSituacionBBN_00.addSubMode(self.mdNuevoPasoNo)
        self.mdSituacionNNN_00.addSubMode(self.mdNuevoPasoNo)
        self.mdSituacionNBV_01.addSubMode(self.mdNuevoPasoNo)
        self.mdSituacionBNB_01.addSubMode(self.mdNuevoPasoNo)
        self.mdSituacionBBB_01.addSubMode(self.mdNuevoPasoNo)
        self.mdSituacionBNN_01.addSubMode(self.mdNuevoPasoSi)
        self.mdSituacionNBB_01.addSubMode(self.mdNuevoPasoNo)
        self.mdSituacionNNB_01.addSubMode(self.mdNuevoPasoNo)
        self.mdSituacionVBN_01.addSubMode(self.mdNuevoPasoNo)
        self.mdSituacionBBN_01.addSubMode(self.mdNuevoPasoNo)
        self.mdSituacionNNN_01.addSubMode(self.mdNuevoPasoSi)
        self.mdSituacionNBN_01.addSubMode(self.mdNuevoPasoNo)
        self.mdSituacionBBB_02.addSubMode(self.mdNuevoPasoNo)
        self.mdSituacionBBN_02.addSubMode(self.mdNuevoPasoNo)
        self.mdSituacionBNB_02.addSubMode(self.mdNuevoPasoNo)
        self.mdSituacionBNN_02.addSubMode(self.mdNuevoPasoSi)
        self.mdSituacionBNN_02.addSubMode(self.mdNuevoPasoNo)
        self.mdSituacionNBB_02.addSubMode(self.mdNuevoPasoNo)
        self.mdSituacionNBN_02.addSubMode(self.mdNuevoPasoNo)
        self.mdSituacionNBV_02.addSubMode(self.mdNuevoPasoNo)
        self.mdSituacionNNB_02.addSubMode(self.mdNuevoPasoNo)
        self.mdSituacionNNN_02.addSubMode(self.mdNuevoPasoSi)
        self.mdSituacionNNN_02.addSubMode(self.mdNuevoPasoNo)
        self.mdSituacionVBN_02.addSubMode(self.mdNuevoPasoNo)
        self.mdSituacionBBB_03.addSubMode(self.mdNuevoPasoNo)
        self.mdSituacionBBN_03.addSubMode(self.mdNuevoPasoNo)
        self.mdSituacionBNB_03.addSubMode(self.mdNuevoPasoNo)
        self.mdSituacionBNN_03.addSubMode(self.mdNuevoPasoNo)
        self.mdSituacionNBB_03.addSubMode(self.mdNuevoPasoNo)
        self.mdSituacionNBN_03.addSubMode(self.mdNuevoPasoNo)
        self.mdSituacionNBV_03.addSubMode(self.mdNuevoPasoNo)
        self.mdSituacionNNB_03.addSubMode(self.mdNuevoPasoSi)
        self.mdSituacionNNN_03.addSubMode(self.mdNuevoPasoSi)
        self.mdSituacionNNN_03.addSubMode(self.mdNuevoPasoNo)
        self.mdSituacionVBN_03.addSubMode(self.mdNuevoPasoNo)
        self.mdSituacionNNB_04.addSubMode(self.mdNuevoPasoSi)
        self.mdSituacionNNN_04.addSubMode(self.mdNuevoPasoSi)
        self.mdSituacionBNB_05.addSubMode(self.mdNuevoPasoSi)
        self.mdSituacionNNN_06.addSubMode(self.mdNuevoPasoSi)
        self.mdSituacionNNB_06.addSubMode(self.mdNuevoPasoSi)
        self.mdSituacionVVB_07.addSubMode(self.mdNuevoPasoSi)
        self.mdSituacionVVV_08.addSubMode(self.mdNuevoPasoSi)
        self.mdSituacionBNB_01.addSubMode(self.mdDecisionSeguidorBNB)
        self.mdSituacionBNB_02.addSubMode(self.mdDecisionSeguidorBNB)
        self.mdSituacionBNB_03.addSubMode(self.mdDecisionSeguidorBNB)
        self.mdSituacionBNB_04.addSubMode(self.mdDecisionSeguidorBNB)
        self.mdSituacionBNB_05.addSubMode(self.mdDecisionSeguidorBNB)
        self.mdSituacionBNB_06.addSubMode(self.mdDecisionSeguidorBNB)
        self.mdSituacionVVB_07.addSubMode(self.mdDecisionSeguidorVVB)
        self.mdSituacionVVB_08.addSubMode(self.mdDecisionSeguidorVVB)
        self.mdTramoP00_SituarBNB_finBNB_Avanzar.addSubMode(self.mdDecisionAparejoCerrado)
        self.mdTramoP01_SeguirBNB_finder_giroder_abrir.addSubMode(self.mdDecisionAparejoCerrado)
        self.mdTramoP02_SeguirBNB_finder_giroder.addSubMode(self.mdDecisionAparejoAbierto)
        self.mdTramoP03_SeguirBNB_finizq_giroizq.addSubMode(self.mdDecisionAparejoAbierto)
        self.mdTramoP04_SeguirBNB_fincruce_rect.addSubMode(self.mdDecisionAparejoAbierto)
        self.mdTramoP05_SeguirNNB_finBNB_rect.addSubMode(self.mdDecisionAparejoAbierto)
        self.mdTramoP06_SeguirBNB_finizq_giroder.addSubMode(self.mdDecisionAparejoAbierto)
        self.mdTramoP07_SituarVVB_finVVB_Avanzar.addSubMode(self.mdDecisionAparejoAbierto)
        self.mdTramoP08_SeguirVVB_finVVV_giroder.addSubMode(self.mdDecisionAparejoAbierto)


motorIzq = Motor('A')
motorDer = Motor('B')
sensorizq = ColorSensor('C')
sensorcentro = ColorSensor('E')
sensorder = ColorSensor('D')
motorAparejo = Motor('F')

def letracolor(cstr):
    # 'black','violet','blue','cyan','green','yellow','red','white',None
    if cstr == 'black':
        return 'N'
    if cstr == 'white':
        return 'B'
    if cstr == 'green':
        return 'V'
    if cstr == 'blue':
        return 'Z'
    if cstr == 'cyan':
        return 'C'
    if cstr == 'red':
        return 'R'
    if cstr == 'violet':
        return 'O'
    else:
        return '-'

'''
tamfilt = 4
indexfilt = 0
filtizq = ['-'] * tamfilt
filtcent = ['-'] * tamfilt
filtder = ['-'] * tamfilt
letraizq = '-'
letracent = '-'
letrader = '-'


def sensores():
    global letraizq,letracent,letrader,indexfilt
    # Introducimos el sensado actual en el vector de filtrado
    filtizq[indexfilt] = letracolor(sensorizq.get_color())
    filtcent[indexfilt] = letracolor(sensorder.get_color())
    filtder[indexfilt] = letracolor(sensorder.get_color())
    # Calculamos el siguiente índice
    indexfilt += 1
    if indexfilt >= tamfilt:
        indexfilt = 0

    # Vamos a ver si todos son iguales
    okizq = all(ele == filtizq[0] for ele in filtizq)
    okicent = all(ele == filtcent[0] for ele in filtcent)
    okder = all(ele == filtder[0] for ele in filtder)

    # Si alguno de los elementos es todo igual, guardamos la letra unánime
    if okizq:
        letraizq = filtizq[0]
    if okicent:
        letracent = filtcent[0]
    if okizq:
        letrader = filtder[0]

    return letraizq+letracent+letrader
'''

def sensores():
    # Introducimos el sensado actual en el vector de filtrado
    letraizq = letracolor(sensorizq.get_color())
    letracent = letracolor(sensorcentro.get_color())
    letrader = letracolor(sensorder.get_color())

    return letraizq+letracent+letrader

def ruedas():
    global model
    global motorIzq,motorDer

    if model.prRuedaIzq.selectedValue == model.vlRuedaIzq_Adelante:
        motorIzq.start(-10)
    else:
        if model.prRuedaIzq.selectedValue == model.vlRuedaIzq_Atras:
            motorIzq.start(10)
        else:
            motorIzq.stop()

    if model.prRuedaDer.selectedValue == model.vlRuedaDer_Adelante:
        motorDer.start(10)
    else:
        if model.prRuedaDer.selectedValue == model.vlRuedaDer_Atras:
            motorDer.start(-10)
        else:
            motorDer.stop()

def para_todo():
    motorIzq.stop()
    motorDer.stop()

model = csysWROPORIS()

hub = PrimeHub()

hub.light_matrix.show_image('HAPPY')

# Mostramos información del modelo
print("Nombre de modelo:",model.root.name)

# Seleccionamos el modo de Mision Normal
model.root.setMode(model.mdMisionNormal)
print("\n\n\nModo actual de la Mision:",model.root.selectedMode.name)

# Ordenamos los tramos
tramos = [
model.mdTramoP00_SituarBNB_finBNB_Avanzar,
model.mdTramoP01_SeguirBNB_finder_giroder_abrir,
model.mdTramoP02_SeguirBNB_finder_giroder,
model.mdTramoP03_SeguirBNB_finizq_giroizq,
model.mdTramoP04_SeguirBNB_fincruce_rect,
model.mdTramoP05_SeguirNNB_finBNB_rect,
model.mdTramoP06_SeguirBNB_finizq_giroder,
model.mdTramoP07_SituarVVB_finVVB_Avanzar,
model.mdTramoP08_SeguirVVB_finVVV_giroder
]



fin = False
tramo = 0
# Iteramos por todos los tramos
for tr in tramos:
    model.sysNuevoPaso.selectedMode = model.mdNuevoPasoUNKNOWN
    model.sysTramo.setMode(tr)
    print("\n\n\nTramo actual:",tr.name)
    hub.light_matrix.write(str(tramo))
    para_todo()
    wait_for_seconds(2)
    ruedas()
    nuevotramo = False
    while not nuevotramo:
        # Averiguamos la situacion en la que estamos
        d = sensores()
        #hub.light_matrix.write(d)
        d += '_0'+str(tramo)
        #print(tr.submodes.keys())
        if d in tr.submodes.keys():
            dr = tr.submodes[d]
            model.sysSituacion.setMode(dr)
            print("Situación actual:",model.sysSituacion.selectedMode.name)
            #print("Decisión actual movilidad:",model.sysDecisionMovimiento.selectedMode.name)
            #print("Decisión actual aparejo:",model.sysDecisionAparejo.selectedMode.name)
            np = model.sysNuevoPaso.selectedMode
            #print("Decisión actual siguiente paso:",np.name)
            #print("Ruedas: ",model.prRuedaIzq.selectedValue.name,model.prRuedaDer.selectedValue.name)
            ruedas()
            #wait_for_seconds(0.1)
            if (np == model.mdNuevoPasoSi):
                nuevotramo = True
                tramo += 1

        #wait_for_seconds(0.1)
        #hub.light_matrix.write(str(tramo))
        #wait_for_seconds(0.1)



para_todo()