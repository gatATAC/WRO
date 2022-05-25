from PORIS import *

class csysWROPORIS:
	def __init__(self):
		identcounter = 1
		sysMision = PORISSys("Mision")
		self.sysMision = sysMision
		mdMisionMode_UNKNOWN = PORISMode("MisionMode_UNKNOWN")
		self.mdMisionMode_UNKNOWN = mdMisionMode_UNKNOWN
		self.root = sysMision
		mdMisionMode_Normal = PORISMode("MisionMode_Normal")
		self.mdMisionMode_Normal = mdMisionMode_Normal
		sysTramo = PORISSys("Tramo")
		self.sysTramo = sysTramo
		mdTramoMode_UNKNOWN = PORISMode("TramoMode_UNKNOWN")
		self.mdTramoMode_UNKNOWN = mdTramoMode_UNKNOWN
		mdTramoMode_P00_SituarBNB_finBNB_Avanzar = PORISMode("TramoMode_P00_SituarBNB_finBNB_Avanzar")
		self.mdTramoMode_P00_SituarBNB_finBNB_Avanzar = mdTramoMode_P00_SituarBNB_finBNB_Avanzar
		mdTramoMode_P01_SeguirBNB_finder_giroder_abrir = PORISMode("TramoMode_P01_SeguirBNB_finder_giroder_abrir")
		self.mdTramoMode_P01_SeguirBNB_finder_giroder_abrir = mdTramoMode_P01_SeguirBNB_finder_giroder_abrir
		mdTramoMode_P02_SeguirBNB_finder_giroder = PORISMode("TramoMode_P02_SeguirBNB_finder_giroder")
		self.mdTramoMode_P02_SeguirBNB_finder_giroder = mdTramoMode_P02_SeguirBNB_finder_giroder
		mdTramoMode_P03_SeguirBNB_finizq_giroizq = PORISMode("TramoMode_P03_SeguirBNB_finizq_giroizq")
		self.mdTramoMode_P03_SeguirBNB_finizq_giroizq = mdTramoMode_P03_SeguirBNB_finizq_giroizq
		mdTramoMode_P04_SeguirBNB_fincruce_rect = PORISMode("TramoMode_P04_SeguirBNB_fincruce_rect")
		self.mdTramoMode_P04_SeguirBNB_fincruce_rect = mdTramoMode_P04_SeguirBNB_fincruce_rect
		mdTramoMode_P05_SeguirNNB_finBNB_rect = PORISMode("TramoMode_P05_SeguirNNB_finBNB_rect")
		self.mdTramoMode_P05_SeguirNNB_finBNB_rect = mdTramoMode_P05_SeguirNNB_finBNB_rect
		mdTramoMode_P06_SeguirBNB_finizq_giroder = PORISMode("TramoMode_P06_SeguirBNB_finizq_giroder")
		self.mdTramoMode_P06_SeguirBNB_finizq_giroder = mdTramoMode_P06_SeguirBNB_finizq_giroder
		mdTramoMode_P07_SituarVVB_finVVB_Avanzar = PORISMode("TramoMode_P07_SituarVVB_finVVB_Avanzar")
		self.mdTramoMode_P07_SituarVVB_finVVB_Avanzar = mdTramoMode_P07_SituarVVB_finVVB_Avanzar
		mdTramoMode_P08_SeguirVVB_finVVV_giroder = PORISMode("TramoMode_P08_SeguirVVB_finVVV_giroder")
		self.mdTramoMode_P08_SeguirVVB_finVVV_giroder = mdTramoMode_P08_SeguirVVB_finVVV_giroder
		sysSituacion = PORISSys("Situacion")
		self.sysSituacion = sysSituacion
		mdSituacionMode_UNKNOWN = PORISMode("SituacionMode_UNKNOWN")
		self.mdSituacionMode_UNKNOWN = mdSituacionMode_UNKNOWN
		mdSituacionMode_BNN_00 = PORISMode("SituacionMode_BNN_00")
		self.mdSituacionMode_BNN_00 = mdSituacionMode_BNN_00
		mdSituacionMode_NBB_00 = PORISMode("SituacionMode_NBB_00")
		self.mdSituacionMode_NBB_00 = mdSituacionMode_NBB_00
		mdSituacionMode_BBB_00 = PORISMode("SituacionMode_BBB_00")
		self.mdSituacionMode_BBB_00 = mdSituacionMode_BBB_00
		mdSituacionMode_NNB_00 = PORISMode("SituacionMode_NNB_00")
		self.mdSituacionMode_NNB_00 = mdSituacionMode_NNB_00
		mdSituacionMode_BNB_00 = PORISMode("SituacionMode_BNB_00")
		self.mdSituacionMode_BNB_00 = mdSituacionMode_BNB_00
		mdSituacionMode_NBN_00 = PORISMode("SituacionMode_NBN_00")
		self.mdSituacionMode_NBN_00 = mdSituacionMode_NBN_00
		mdSituacionMode_BBN_00 = PORISMode("SituacionMode_BBN_00")
		self.mdSituacionMode_BBN_00 = mdSituacionMode_BBN_00
		mdSituacionMode_NNN_00 = PORISMode("SituacionMode_NNN_00")
		self.mdSituacionMode_NNN_00 = mdSituacionMode_NNN_00
		mdSituacionMode_NBV_01 = PORISMode("SituacionMode_NBV_01")
		self.mdSituacionMode_NBV_01 = mdSituacionMode_NBV_01
		mdSituacionMode_BNB_01 = PORISMode("SituacionMode_BNB_01")
		self.mdSituacionMode_BNB_01 = mdSituacionMode_BNB_01
		mdSituacionMode_BBB_01 = PORISMode("SituacionMode_BBB_01")
		self.mdSituacionMode_BBB_01 = mdSituacionMode_BBB_01
		mdSituacionMode_BNN_01 = PORISMode("SituacionMode_BNN_01")
		self.mdSituacionMode_BNN_01 = mdSituacionMode_BNN_01
		mdSituacionMode_NBB_01 = PORISMode("SituacionMode_NBB_01")
		self.mdSituacionMode_NBB_01 = mdSituacionMode_NBB_01
		mdSituacionMode_NNB_01 = PORISMode("SituacionMode_NNB_01")
		self.mdSituacionMode_NNB_01 = mdSituacionMode_NNB_01
		mdSituacionMode_VBN_01 = PORISMode("SituacionMode_VBN_01")
		self.mdSituacionMode_VBN_01 = mdSituacionMode_VBN_01
		mdSituacionMode_BBN_01 = PORISMode("SituacionMode_BBN_01")
		self.mdSituacionMode_BBN_01 = mdSituacionMode_BBN_01
		mdSituacionMode_NNN_01 = PORISMode("SituacionMode_NNN_01")
		self.mdSituacionMode_NNN_01 = mdSituacionMode_NNN_01
		mdSituacionMode_NBN_01 = PORISMode("SituacionMode_NBN_01")
		self.mdSituacionMode_NBN_01 = mdSituacionMode_NBN_01
		mdSituacionMode_BBB_02 = PORISMode("SituacionMode_BBB_02")
		self.mdSituacionMode_BBB_02 = mdSituacionMode_BBB_02
		mdSituacionMode_BBN_02 = PORISMode("SituacionMode_BBN_02")
		self.mdSituacionMode_BBN_02 = mdSituacionMode_BBN_02
		mdSituacionMode_BNB_02 = PORISMode("SituacionMode_BNB_02")
		self.mdSituacionMode_BNB_02 = mdSituacionMode_BNB_02
		mdSituacionMode_BNN_02 = PORISMode("SituacionMode_BNN_02")
		self.mdSituacionMode_BNN_02 = mdSituacionMode_BNN_02
		mdSituacionMode_NBB_02 = PORISMode("SituacionMode_NBB_02")
		self.mdSituacionMode_NBB_02 = mdSituacionMode_NBB_02
		mdSituacionMode_NBN_02 = PORISMode("SituacionMode_NBN_02")
		self.mdSituacionMode_NBN_02 = mdSituacionMode_NBN_02
		mdSituacionMode_NBV_02 = PORISMode("SituacionMode_NBV_02")
		self.mdSituacionMode_NBV_02 = mdSituacionMode_NBV_02
		mdSituacionMode_NNB_02 = PORISMode("SituacionMode_NNB_02")
		self.mdSituacionMode_NNB_02 = mdSituacionMode_NNB_02
		mdSituacionMode_NNN_02 = PORISMode("SituacionMode_NNN_02")
		self.mdSituacionMode_NNN_02 = mdSituacionMode_NNN_02
		mdSituacionMode_VBN_02 = PORISMode("SituacionMode_VBN_02")
		self.mdSituacionMode_VBN_02 = mdSituacionMode_VBN_02
		mdSituacionMode_BBB_03 = PORISMode("SituacionMode_BBB_03")
		self.mdSituacionMode_BBB_03 = mdSituacionMode_BBB_03
		mdSituacionMode_BBN_03 = PORISMode("SituacionMode_BBN_03")
		self.mdSituacionMode_BBN_03 = mdSituacionMode_BBN_03
		mdSituacionMode_BNB_03 = PORISMode("SituacionMode_BNB_03")
		self.mdSituacionMode_BNB_03 = mdSituacionMode_BNB_03
		mdSituacionMode_BNN_03 = PORISMode("SituacionMode_BNN_03")
		self.mdSituacionMode_BNN_03 = mdSituacionMode_BNN_03
		mdSituacionMode_NBB_03 = PORISMode("SituacionMode_NBB_03")
		self.mdSituacionMode_NBB_03 = mdSituacionMode_NBB_03
		mdSituacionMode_NBN_03 = PORISMode("SituacionMode_NBN_03")
		self.mdSituacionMode_NBN_03 = mdSituacionMode_NBN_03
		mdSituacionMode_NBV_03 = PORISMode("SituacionMode_NBV_03")
		self.mdSituacionMode_NBV_03 = mdSituacionMode_NBV_03
		mdSituacionMode_NNB_03 = PORISMode("SituacionMode_NNB_03")
		self.mdSituacionMode_NNB_03 = mdSituacionMode_NNB_03
		mdSituacionMode_NNN_03 = PORISMode("SituacionMode_NNN_03")
		self.mdSituacionMode_NNN_03 = mdSituacionMode_NNN_03
		mdSituacionMode_VBN_03 = PORISMode("SituacionMode_VBN_03")
		self.mdSituacionMode_VBN_03 = mdSituacionMode_VBN_03
		mdSituacionMode_BBB_04 = PORISMode("SituacionMode_BBB_04")
		self.mdSituacionMode_BBB_04 = mdSituacionMode_BBB_04
		mdSituacionMode_BBN_04 = PORISMode("SituacionMode_BBN_04")
		self.mdSituacionMode_BBN_04 = mdSituacionMode_BBN_04
		mdSituacionMode_BNB_04 = PORISMode("SituacionMode_BNB_04")
		self.mdSituacionMode_BNB_04 = mdSituacionMode_BNB_04
		mdSituacionMode_BNN_04 = PORISMode("SituacionMode_BNN_04")
		self.mdSituacionMode_BNN_04 = mdSituacionMode_BNN_04
		mdSituacionMode_NBB_04 = PORISMode("SituacionMode_NBB_04")
		self.mdSituacionMode_NBB_04 = mdSituacionMode_NBB_04
		mdSituacionMode_NBN_04 = PORISMode("SituacionMode_NBN_04")
		self.mdSituacionMode_NBN_04 = mdSituacionMode_NBN_04
		mdSituacionMode_NBV_04 = PORISMode("SituacionMode_NBV_04")
		self.mdSituacionMode_NBV_04 = mdSituacionMode_NBV_04
		mdSituacionMode_NNB_04 = PORISMode("SituacionMode_NNB_04")
		self.mdSituacionMode_NNB_04 = mdSituacionMode_NNB_04
		mdSituacionMode_NNN_04 = PORISMode("SituacionMode_NNN_04")
		self.mdSituacionMode_NNN_04 = mdSituacionMode_NNN_04
		mdSituacionMode_VBN_04 = PORISMode("SituacionMode_VBN_04")
		self.mdSituacionMode_VBN_04 = mdSituacionMode_VBN_04
		mdSituacionMode_BBB_05 = PORISMode("SituacionMode_BBB_05")
		self.mdSituacionMode_BBB_05 = mdSituacionMode_BBB_05
		mdSituacionMode_BBN_05 = PORISMode("SituacionMode_BBN_05")
		self.mdSituacionMode_BBN_05 = mdSituacionMode_BBN_05
		mdSituacionMode_BNB_05 = PORISMode("SituacionMode_BNB_05")
		self.mdSituacionMode_BNB_05 = mdSituacionMode_BNB_05
		mdSituacionMode_BNN_05 = PORISMode("SituacionMode_BNN_05")
		self.mdSituacionMode_BNN_05 = mdSituacionMode_BNN_05
		mdSituacionMode_NBB_05 = PORISMode("SituacionMode_NBB_05")
		self.mdSituacionMode_NBB_05 = mdSituacionMode_NBB_05
		mdSituacionMode_NBN_05 = PORISMode("SituacionMode_NBN_05")
		self.mdSituacionMode_NBN_05 = mdSituacionMode_NBN_05
		mdSituacionMode_NNB_05 = PORISMode("SituacionMode_NNB_05")
		self.mdSituacionMode_NNB_05 = mdSituacionMode_NNB_05
		mdSituacionMode_NNN_05 = PORISMode("SituacionMode_NNN_05")
		self.mdSituacionMode_NNN_05 = mdSituacionMode_NNN_05
		mdSituacionMode_VBN_06 = PORISMode("SituacionMode_VBN_06")
		self.mdSituacionMode_VBN_06 = mdSituacionMode_VBN_06
		mdSituacionMode_NBB_06 = PORISMode("SituacionMode_NBB_06")
		self.mdSituacionMode_NBB_06 = mdSituacionMode_NBB_06
		mdSituacionMode_BNB_06 = PORISMode("SituacionMode_BNB_06")
		self.mdSituacionMode_BNB_06 = mdSituacionMode_BNB_06
		mdSituacionMode_NBN_06 = PORISMode("SituacionMode_NBN_06")
		self.mdSituacionMode_NBN_06 = mdSituacionMode_NBN_06
		mdSituacionMode_NNN_06 = PORISMode("SituacionMode_NNN_06")
		self.mdSituacionMode_NNN_06 = mdSituacionMode_NNN_06
		mdSituacionMode_BNN_06 = PORISMode("SituacionMode_BNN_06")
		self.mdSituacionMode_BNN_06 = mdSituacionMode_BNN_06
		mdSituacionMode_BBN_06 = PORISMode("SituacionMode_BBN_06")
		self.mdSituacionMode_BBN_06 = mdSituacionMode_BBN_06
		mdSituacionMode_BBB_06 = PORISMode("SituacionMode_BBB_06")
		self.mdSituacionMode_BBB_06 = mdSituacionMode_BBB_06
		mdSituacionMode_NBV_06 = PORISMode("SituacionMode_NBV_06")
		self.mdSituacionMode_NBV_06 = mdSituacionMode_NBV_06
		mdSituacionMode_NNB_06 = PORISMode("SituacionMode_NNB_06")
		self.mdSituacionMode_NNB_06 = mdSituacionMode_NNB_06
		mdSituacionMode_BBB_07 = PORISMode("SituacionMode_BBB_07")
		self.mdSituacionMode_BBB_07 = mdSituacionMode_BBB_07
		mdSituacionMode_BBN_07 = PORISMode("SituacionMode_BBN_07")
		self.mdSituacionMode_BBN_07 = mdSituacionMode_BBN_07
		mdSituacionMode_BNB_07 = PORISMode("SituacionMode_BNB_07")
		self.mdSituacionMode_BNB_07 = mdSituacionMode_BNB_07
		mdSituacionMode_BNN_07 = PORISMode("SituacionMode_BNN_07")
		self.mdSituacionMode_BNN_07 = mdSituacionMode_BNN_07
		mdSituacionMode_NBB_07 = PORISMode("SituacionMode_NBB_07")
		self.mdSituacionMode_NBB_07 = mdSituacionMode_NBB_07
		mdSituacionMode_NBN_07 = PORISMode("SituacionMode_NBN_07")
		self.mdSituacionMode_NBN_07 = mdSituacionMode_NBN_07
		mdSituacionMode_NBV_07 = PORISMode("SituacionMode_NBV_07")
		self.mdSituacionMode_NBV_07 = mdSituacionMode_NBV_07
		mdSituacionMode_NNB_07 = PORISMode("SituacionMode_NNB_07")
		self.mdSituacionMode_NNB_07 = mdSituacionMode_NNB_07
		mdSituacionMode_NNN_07 = PORISMode("SituacionMode_NNN_07")
		self.mdSituacionMode_NNN_07 = mdSituacionMode_NNN_07
		mdSituacionMode_VBN_07 = PORISMode("SituacionMode_VBN_07")
		self.mdSituacionMode_VBN_07 = mdSituacionMode_VBN_07
		mdSituacionMode_VVB_07 = PORISMode("SituacionMode_VVB_07")
		self.mdSituacionMode_VVB_07 = mdSituacionMode_VVB_07
		mdSituacionMode_VVV_07 = PORISMode("SituacionMode_VVV_07")
		self.mdSituacionMode_VVV_07 = mdSituacionMode_VVV_07
		mdSituacionMode_VVV_08 = PORISMode("SituacionMode_VVV_08")
		self.mdSituacionMode_VVV_08 = mdSituacionMode_VVV_08
		mdSituacionMode_VBN_08 = PORISMode("SituacionMode_VBN_08")
		self.mdSituacionMode_VBN_08 = mdSituacionMode_VBN_08
		mdSituacionMode_VVB_08 = PORISMode("SituacionMode_VVB_08")
		self.mdSituacionMode_VVB_08 = mdSituacionMode_VVB_08
		sysDecisionMovimiento = PORISSys("DecisionMovimiento")
		self.sysDecisionMovimiento = sysDecisionMovimiento
		mdDecisionMovimientoMode_UNKNOWN = PORISMode("DecisionMovimientoMode_UNKNOWN")
		self.mdDecisionMovimientoMode_UNKNOWN = mdDecisionMovimientoMode_UNKNOWN
		mdDecisionMovimientoMode_Avanzar = PORISMode("DecisionMovimientoMode_Avanzar")
		self.mdDecisionMovimientoMode_Avanzar = mdDecisionMovimientoMode_Avanzar
		mdDecisionMovimientoMode_CompasIzq = PORISMode("DecisionMovimientoMode_CompasIzq")
		self.mdDecisionMovimientoMode_CompasIzq = mdDecisionMovimientoMode_CompasIzq
		mdDecisionMovimientoMode_CompasDer = PORISMode("DecisionMovimientoMode_CompasDer")
		self.mdDecisionMovimientoMode_CompasDer = mdDecisionMovimientoMode_CompasDer
		mdDecisionMovimientoMode_GirarDer = PORISMode("DecisionMovimientoMode_GirarDer")
		self.mdDecisionMovimientoMode_GirarDer = mdDecisionMovimientoMode_GirarDer
		mdDecisionMovimientoMode_GirarIzq = PORISMode("DecisionMovimientoMode_GirarIzq")
		self.mdDecisionMovimientoMode_GirarIzq = mdDecisionMovimientoMode_GirarIzq
		mdDecisionMovimientoMode_Parar = PORISMode("DecisionMovimientoMode_Parar")
		self.mdDecisionMovimientoMode_Parar = mdDecisionMovimientoMode_Parar
		prRuedaDer = PORISParam("RuedaDer")
		self.prRuedaDer = prRuedaDer
		mdRuedaDerMode_UNKNOWN = PORISMode("RuedaDerMode_UNKNOWN")
		self.mdRuedaDerMode_UNKNOWN = mdRuedaDerMode_UNKNOWN
		vlRuedaDer_UNKNOWN = PORISValue("RuedaDer_UNKNOWN")
		self.vlRuedaDer_UNKNOWN = vlRuedaDer_UNKNOWN
		mdRuedaDerMode_Parada = PORISMode("RuedaDerMode_Parada")
		self.mdRuedaDerMode_Parada = mdRuedaDerMode_Parada
		mdRuedaDerMode_Avanzar = PORISMode("RuedaDerMode_Avanzar")
		self.mdRuedaDerMode_Avanzar = mdRuedaDerMode_Avanzar
		mdRuedaDerMode_Retroceder = PORISMode("RuedaDerMode_Retroceder")
		self.mdRuedaDerMode_Retroceder = mdRuedaDerMode_Retroceder
		vlRuedaDer_Quieta = PORISValue("RuedaDer_Quieta")
		self.vlRuedaDer_Quieta = vlRuedaDer_Quieta
		vlRuedaDer_Adelante = PORISValue("RuedaDer_Adelante")
		self.vlRuedaDer_Adelante = vlRuedaDer_Adelante
		vlRuedaDer_Atras = PORISValue("RuedaDer_Atras")
		self.vlRuedaDer_Atras = vlRuedaDer_Atras
		prRuedaIzq = PORISParam("RuedaIzq")
		self.prRuedaIzq = prRuedaIzq
		mdRuedaIzqMode_UNKNOWN = PORISMode("RuedaIzqMode_UNKNOWN")
		self.mdRuedaIzqMode_UNKNOWN = mdRuedaIzqMode_UNKNOWN
		vlRuedaIzq_UNKNOWN = PORISValue("RuedaIzq_UNKNOWN")
		self.vlRuedaIzq_UNKNOWN = vlRuedaIzq_UNKNOWN
		mdRuedaIzqMode_Parada = PORISMode("RuedaIzqMode_Parada")
		self.mdRuedaIzqMode_Parada = mdRuedaIzqMode_Parada
		mdRuedaIzqMode_Avanzar = PORISMode("RuedaIzqMode_Avanzar")
		self.mdRuedaIzqMode_Avanzar = mdRuedaIzqMode_Avanzar
		mdRuedaIzqMode_Retroceder = PORISMode("RuedaIzqMode_Retroceder")
		self.mdRuedaIzqMode_Retroceder = mdRuedaIzqMode_Retroceder
		vlRuedaIzq_Quieta = PORISValue("RuedaIzq_Quieta")
		self.vlRuedaIzq_Quieta = vlRuedaIzq_Quieta
		vlRuedaIzq_Adelante = PORISValue("RuedaIzq_Adelante")
		self.vlRuedaIzq_Adelante = vlRuedaIzq_Adelante
		vlRuedaIzq_Atras = PORISValue("RuedaIzq_Atras")
		self.vlRuedaIzq_Atras = vlRuedaIzq_Atras
		sysNuevoPaso = PORISSys("NuevoPaso")
		self.sysNuevoPaso = sysNuevoPaso
		mdNuevoPasoMode_UNKNOWN = PORISMode("NuevoPasoMode_UNKNOWN")
		self.mdNuevoPasoMode_UNKNOWN = mdNuevoPasoMode_UNKNOWN
		mdNuevoPasoMode_Si = PORISMode("NuevoPasoMode_Si")
		self.mdNuevoPasoMode_Si = mdNuevoPasoMode_Si
		sysDecisionSeguidor = PORISSys("DecisionSeguidor")
		self.sysDecisionSeguidor = sysDecisionSeguidor
		mdDecisionSeguidorMode_UNKNOWN = PORISMode("DecisionSeguidorMode_UNKNOWN")
		self.mdDecisionSeguidorMode_UNKNOWN = mdDecisionSeguidorMode_UNKNOWN
		mdDecisionSeguidorMode_BNB = PORISMode("DecisionSeguidorMode_BNB")
		self.mdDecisionSeguidorMode_BNB = mdDecisionSeguidorMode_BNB
		mdDecisionSeguidorMode_VVB = PORISMode("DecisionSeguidorMode_VVB")
		self.mdDecisionSeguidorMode_VVB = mdDecisionSeguidorMode_VVB
		sysDecisionAparejo = PORISSys("DecisionAparejo")
		self.sysDecisionAparejo = sysDecisionAparejo
		mdDecisionAparejoMode_UNKNOWN = PORISMode("DecisionAparejoMode_UNKNOWN")
		self.mdDecisionAparejoMode_UNKNOWN = mdDecisionAparejoMode_UNKNOWN
		mdDecisionAparejoMode_Abierto = PORISMode("DecisionAparejoMode_Abierto")
		self.mdDecisionAparejoMode_Abierto = mdDecisionAparejoMode_Abierto
		mdDecisionAparejoMode_Medio = PORISMode("DecisionAparejoMode_Medio")
		self.mdDecisionAparejoMode_Medio = mdDecisionAparejoMode_Medio
		mdDecisionAparejoMode_Cerrado = PORISMode("DecisionAparejoMode_Cerrado")
		self.mdDecisionAparejoMode_Cerrado = mdDecisionAparejoMode_Cerrado
		mdMisionMode_Engineering = PORISMode("MisionMode_Engineering")
		self.mdMisionMode_Engineering = mdMisionMode_Engineering
		mdTramoMode_Engineering = PORISMode("TramoMode_Engineering")
		self.mdTramoMode_Engineering = mdTramoMode_Engineering
		mdSituacionMode_Engineering = PORISMode("SituacionMode_Engineering")
		self.mdSituacionMode_Engineering = mdSituacionMode_Engineering
		mdDecisionMovimientoMode_Engineering = PORISMode("DecisionMovimientoMode_Engineering")
		self.mdDecisionMovimientoMode_Engineering = mdDecisionMovimientoMode_Engineering

		sysMision.id = identcounter
		identcounter += 1

		mdMisionMode_UNKNOWN.id = identcounter
		identcounter += 1
		sysMision.addMode(mdMisionMode_UNKNOWN);

		mdMisionMode_Normal.id = identcounter
		identcounter += 1
		sysMision.addMode(mdMisionMode_Normal)

		sysTramo.id = identcounter
		identcounter += 1
		sysMision.addSubsystem(sysTramo);

		mdTramoMode_UNKNOWN.id = identcounter
		identcounter += 1
		sysTramo.addMode(mdTramoMode_UNKNOWN);

		mdTramoMode_P00_SituarBNB_finBNB_Avanzar.id = identcounter
		identcounter += 1
		sysTramo.addMode(mdTramoMode_P00_SituarBNB_finBNB_Avanzar)

		mdTramoMode_P01_SeguirBNB_finder_giroder_abrir.id = identcounter
		identcounter += 1
		sysTramo.addMode(mdTramoMode_P01_SeguirBNB_finder_giroder_abrir)

		mdTramoMode_P02_SeguirBNB_finder_giroder.id = identcounter
		identcounter += 1
		sysTramo.addMode(mdTramoMode_P02_SeguirBNB_finder_giroder)

		mdTramoMode_P03_SeguirBNB_finizq_giroizq.id = identcounter
		identcounter += 1
		sysTramo.addMode(mdTramoMode_P03_SeguirBNB_finizq_giroizq)

		mdTramoMode_P04_SeguirBNB_fincruce_rect.id = identcounter
		identcounter += 1
		sysTramo.addMode(mdTramoMode_P04_SeguirBNB_fincruce_rect)

		mdTramoMode_P05_SeguirNNB_finBNB_rect.id = identcounter
		identcounter += 1
		sysTramo.addMode(mdTramoMode_P05_SeguirNNB_finBNB_rect)

		mdTramoMode_P06_SeguirBNB_finizq_giroder.id = identcounter
		identcounter += 1
		sysTramo.addMode(mdTramoMode_P06_SeguirBNB_finizq_giroder)

		mdTramoMode_P07_SituarVVB_finVVB_Avanzar.id = identcounter
		identcounter += 1
		sysTramo.addMode(mdTramoMode_P07_SituarVVB_finVVB_Avanzar)

		mdTramoMode_P08_SeguirVVB_finVVV_giroder.id = identcounter
		identcounter += 1
		sysTramo.addMode(mdTramoMode_P08_SeguirVVB_finVVV_giroder)

		sysSituacion.id = identcounter
		identcounter += 1
		sysTramo.addSubsystem(sysSituacion);

		mdSituacionMode_UNKNOWN.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_UNKNOWN);

		mdSituacionMode_BNN_00.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_BNN_00)

		mdSituacionMode_NBB_00.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_NBB_00)

		mdSituacionMode_BBB_00.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_BBB_00)

		mdSituacionMode_NNB_00.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_NNB_00)

		mdSituacionMode_BNB_00.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_BNB_00)

		mdSituacionMode_NBN_00.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_NBN_00)

		mdSituacionMode_BBN_00.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_BBN_00)

		mdSituacionMode_NNN_00.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_NNN_00)

		mdSituacionMode_NBV_01.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_NBV_01)

		mdSituacionMode_BNB_01.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_BNB_01)

		mdSituacionMode_BBB_01.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_BBB_01)

		mdSituacionMode_BNN_01.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_BNN_01)

		mdSituacionMode_NBB_01.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_NBB_01)

		mdSituacionMode_NNB_01.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_NNB_01)

		mdSituacionMode_VBN_01.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_VBN_01)

		mdSituacionMode_BBN_01.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_BBN_01)

		mdSituacionMode_NNN_01.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_NNN_01)

		mdSituacionMode_NBN_01.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_NBN_01)

		mdSituacionMode_BBB_02.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_BBB_02)

		mdSituacionMode_BBN_02.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_BBN_02)

		mdSituacionMode_BNB_02.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_BNB_02)

		mdSituacionMode_BNN_02.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_BNN_02)

		mdSituacionMode_NBB_02.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_NBB_02)

		mdSituacionMode_NBN_02.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_NBN_02)

		mdSituacionMode_NBV_02.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_NBV_02)

		mdSituacionMode_NNB_02.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_NNB_02)

		mdSituacionMode_NNN_02.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_NNN_02)

		mdSituacionMode_VBN_02.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_VBN_02)

		mdSituacionMode_BBB_03.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_BBB_03)

		mdSituacionMode_BBN_03.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_BBN_03)

		mdSituacionMode_BNB_03.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_BNB_03)

		mdSituacionMode_BNN_03.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_BNN_03)

		mdSituacionMode_NBB_03.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_NBB_03)

		mdSituacionMode_NBN_03.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_NBN_03)

		mdSituacionMode_NBV_03.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_NBV_03)

		mdSituacionMode_NNB_03.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_NNB_03)

		mdSituacionMode_NNN_03.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_NNN_03)

		mdSituacionMode_VBN_03.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_VBN_03)

		mdSituacionMode_BBB_04.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_BBB_04)

		mdSituacionMode_BBN_04.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_BBN_04)

		mdSituacionMode_BNB_04.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_BNB_04)

		mdSituacionMode_BNN_04.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_BNN_04)

		mdSituacionMode_NBB_04.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_NBB_04)

		mdSituacionMode_NBN_04.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_NBN_04)

		mdSituacionMode_NBV_04.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_NBV_04)

		mdSituacionMode_NNB_04.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_NNB_04)

		mdSituacionMode_NNN_04.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_NNN_04)

		mdSituacionMode_VBN_04.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_VBN_04)

		mdSituacionMode_BBB_05.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_BBB_05)

		mdSituacionMode_BBN_05.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_BBN_05)

		mdSituacionMode_BNB_05.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_BNB_05)

		mdSituacionMode_BNN_05.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_BNN_05)

		mdSituacionMode_NBB_05.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_NBB_05)

		mdSituacionMode_NBN_05.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_NBN_05)

		mdSituacionMode_NNB_05.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_NNB_05)

		mdSituacionMode_NNN_05.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_NNN_05)

		mdSituacionMode_VBN_06.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_VBN_06)

		mdSituacionMode_NBB_06.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_NBB_06)

		mdSituacionMode_BNB_06.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_BNB_06)

		mdSituacionMode_NBN_06.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_NBN_06)

		mdSituacionMode_NNN_06.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_NNN_06)

		mdSituacionMode_BNN_06.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_BNN_06)

		mdSituacionMode_BBN_06.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_BBN_06)

		mdSituacionMode_BBB_06.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_BBB_06)

		mdSituacionMode_NBV_06.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_NBV_06)

		mdSituacionMode_NNB_06.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_NNB_06)

		mdSituacionMode_BBB_07.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_BBB_07)

		mdSituacionMode_BBN_07.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_BBN_07)

		mdSituacionMode_BNB_07.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_BNB_07)

		mdSituacionMode_BNN_07.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_BNN_07)

		mdSituacionMode_NBB_07.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_NBB_07)

		mdSituacionMode_NBN_07.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_NBN_07)

		mdSituacionMode_NBV_07.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_NBV_07)

		mdSituacionMode_NNB_07.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_NNB_07)

		mdSituacionMode_NNN_07.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_NNN_07)

		mdSituacionMode_VBN_07.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_VBN_07)

		mdSituacionMode_VVB_07.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_VVB_07)

		mdSituacionMode_VVV_07.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_VVV_07)

		mdSituacionMode_VVV_08.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_VVV_08)

		mdSituacionMode_VBN_08.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_VBN_08)

		mdSituacionMode_VVB_08.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_VVB_08)

		sysDecisionMovimiento.id = identcounter
		identcounter += 1
		sysSituacion.addSubsystem(sysDecisionMovimiento);

		mdDecisionMovimientoMode_UNKNOWN.id = identcounter
		identcounter += 1
		sysDecisionMovimiento.addMode(mdDecisionMovimientoMode_UNKNOWN);

		mdDecisionMovimientoMode_Avanzar.id = identcounter
		identcounter += 1
		sysDecisionMovimiento.addMode(mdDecisionMovimientoMode_Avanzar)

		mdDecisionMovimientoMode_CompasIzq.id = identcounter
		identcounter += 1
		sysDecisionMovimiento.addMode(mdDecisionMovimientoMode_CompasIzq)

		mdDecisionMovimientoMode_CompasDer.id = identcounter
		identcounter += 1
		sysDecisionMovimiento.addMode(mdDecisionMovimientoMode_CompasDer)

		mdDecisionMovimientoMode_GirarDer.id = identcounter
		identcounter += 1
		sysDecisionMovimiento.addMode(mdDecisionMovimientoMode_GirarDer)

		mdDecisionMovimientoMode_GirarIzq.id = identcounter
		identcounter += 1
		sysDecisionMovimiento.addMode(mdDecisionMovimientoMode_GirarIzq)

		mdDecisionMovimientoMode_Parar.id = identcounter
		identcounter += 1
		sysDecisionMovimiento.addMode(mdDecisionMovimientoMode_Parar)

		prRuedaDer.id = identcounter
		identcounter += 1
		sysDecisionMovimiento.addParam(prRuedaDer)
		vlRuedaDer_UNKNOWN.id = identcounter
		identcounter += 1
		prRuedaDer.addValue(vlRuedaDer_UNKNOWN)

		mdRuedaDerMode_UNKNOWN.id = identcounter
		identcounter += 1
		prRuedaDer.addMode(mdRuedaDerMode_UNKNOWN)
		mdRuedaDerMode_UNKNOWN.addValue(vlRuedaDer_UNKNOWN)
		mdDecisionMovimientoMode_UNKNOWN.addSubMode(mdRuedaDerMode_UNKNOWN)

		mdRuedaDerMode_Parada.id = identcounter
		identcounter += 1
		prRuedaDer.addMode(mdRuedaDerMode_Parada)

		mdRuedaDerMode_Avanzar.id = identcounter
		identcounter += 1
		prRuedaDer.addMode(mdRuedaDerMode_Avanzar)

		mdRuedaDerMode_Retroceder.id = identcounter
		identcounter += 1
		prRuedaDer.addMode(mdRuedaDerMode_Retroceder)

		vlRuedaDer_Quieta.id = identcounter
		identcounter += 1
		prRuedaDer.addValue(vlRuedaDer_Quieta)

		vlRuedaDer_Adelante.id = identcounter
		identcounter += 1
		prRuedaDer.addValue(vlRuedaDer_Adelante)

		vlRuedaDer_Atras.id = identcounter
		identcounter += 1
		prRuedaDer.addValue(vlRuedaDer_Atras)

		prRuedaIzq.id = identcounter
		identcounter += 1
		sysDecisionMovimiento.addParam(prRuedaIzq)
		vlRuedaIzq_UNKNOWN.id = identcounter
		identcounter += 1
		prRuedaIzq.addValue(vlRuedaIzq_UNKNOWN)

		mdRuedaIzqMode_UNKNOWN.id = identcounter
		identcounter += 1
		prRuedaIzq.addMode(mdRuedaIzqMode_UNKNOWN)
		mdRuedaIzqMode_UNKNOWN.addValue(vlRuedaIzq_UNKNOWN)
		mdDecisionMovimientoMode_UNKNOWN.addSubMode(mdRuedaIzqMode_UNKNOWN)

		mdRuedaIzqMode_Parada.id = identcounter
		identcounter += 1
		prRuedaIzq.addMode(mdRuedaIzqMode_Parada)

		mdRuedaIzqMode_Avanzar.id = identcounter
		identcounter += 1
		prRuedaIzq.addMode(mdRuedaIzqMode_Avanzar)

		mdRuedaIzqMode_Retroceder.id = identcounter
		identcounter += 1
		prRuedaIzq.addMode(mdRuedaIzqMode_Retroceder)

		vlRuedaIzq_Quieta.id = identcounter
		identcounter += 1
		prRuedaIzq.addValue(vlRuedaIzq_Quieta)

		vlRuedaIzq_Adelante.id = identcounter
		identcounter += 1
		prRuedaIzq.addValue(vlRuedaIzq_Adelante)

		vlRuedaIzq_Atras.id = identcounter
		identcounter += 1
		prRuedaIzq.addValue(vlRuedaIzq_Atras)

		sysNuevoPaso.id = identcounter
		identcounter += 1
		sysSituacion.addSubsystem(sysNuevoPaso);

		mdNuevoPasoMode_UNKNOWN.id = identcounter
		identcounter += 1
		sysNuevoPaso.addMode(mdNuevoPasoMode_UNKNOWN);

		mdNuevoPasoMode_Si.id = identcounter
		identcounter += 1
		sysNuevoPaso.addMode(mdNuevoPasoMode_Si)

		sysDecisionSeguidor.id = identcounter
		identcounter += 1
		sysSituacion.addSubsystem(sysDecisionSeguidor);

		mdDecisionSeguidorMode_UNKNOWN.id = identcounter
		identcounter += 1
		sysDecisionSeguidor.addMode(mdDecisionSeguidorMode_UNKNOWN);

		mdDecisionSeguidorMode_BNB.id = identcounter
		identcounter += 1
		sysDecisionSeguidor.addMode(mdDecisionSeguidorMode_BNB)

		mdDecisionSeguidorMode_VVB.id = identcounter
		identcounter += 1
		sysDecisionSeguidor.addMode(mdDecisionSeguidorMode_VVB)

		sysDecisionAparejo.id = identcounter
		identcounter += 1
		sysTramo.addSubsystem(sysDecisionAparejo);

		mdDecisionAparejoMode_UNKNOWN.id = identcounter
		identcounter += 1
		sysDecisionAparejo.addMode(mdDecisionAparejoMode_UNKNOWN);

		mdDecisionAparejoMode_Abierto.id = identcounter
		identcounter += 1
		sysDecisionAparejo.addMode(mdDecisionAparejoMode_Abierto)

		mdDecisionAparejoMode_Medio.id = identcounter
		identcounter += 1
		sysDecisionAparejo.addMode(mdDecisionAparejoMode_Medio)

		mdDecisionAparejoMode_Cerrado.id = identcounter
		identcounter += 1
		sysDecisionAparejo.addMode(mdDecisionAparejoMode_Cerrado)

		mdMisionMode_Engineering.id = identcounter
		identcounter += 1
		sysMision.addMode(mdMisionMode_Engineering)

		mdTramoMode_Engineering.id = identcounter
		identcounter += 1
		sysTramo.addMode(mdTramoMode_Engineering)

		mdSituacionMode_Engineering.id = identcounter
		identcounter += 1
		sysSituacion.addMode(mdSituacionMode_Engineering)

		mdDecisionMovimientoMode_Engineering.id = identcounter
		identcounter += 1
		sysDecisionMovimiento.addMode(mdDecisionMovimientoMode_Engineering)
		# Marcamos TramoMode_P00_SituarBNB_finBNB_Avanzar como elegible para MisionMode_Normal
		mdMisionMode_Normal.addSubMode(mdTramoMode_P00_SituarBNB_finBNB_Avanzar)
		# Marcamos TramoMode_P01_SeguirBNB_finder_giroder_abrir como elegible para MisionMode_Normal
		mdMisionMode_Normal.addSubMode(mdTramoMode_P01_SeguirBNB_finder_giroder_abrir)
		# Marcamos TramoMode_P02_SeguirBNB_finder_giroder como elegible para MisionMode_Normal
		mdMisionMode_Normal.addSubMode(mdTramoMode_P02_SeguirBNB_finder_giroder)
		# Marcamos TramoMode_P03_SeguirBNB_finizq_giroizq como elegible para MisionMode_Normal
		mdMisionMode_Normal.addSubMode(mdTramoMode_P03_SeguirBNB_finizq_giroizq)
		# Marcamos TramoMode_P04_SeguirBNB_fincruce_rect como elegible para MisionMode_Normal
		mdMisionMode_Normal.addSubMode(mdTramoMode_P04_SeguirBNB_fincruce_rect)
		# Marcamos TramoMode_P05_SeguirNNB_finBNB_rect como elegible para MisionMode_Normal
		mdMisionMode_Normal.addSubMode(mdTramoMode_P05_SeguirNNB_finBNB_rect)
		# Marcamos TramoMode_P06_SeguirBNB_finizq_giroder como elegible para MisionMode_Normal
		mdMisionMode_Normal.addSubMode(mdTramoMode_P06_SeguirBNB_finizq_giroder)
		# Marcamos TramoMode_P07_SituarVVB_finVVB_Avanzar como elegible para MisionMode_Normal
		mdMisionMode_Normal.addSubMode(mdTramoMode_P07_SituarVVB_finVVB_Avanzar)
		# Marcamos TramoMode_P08_SeguirVVB_finVVV_giroder como elegible para MisionMode_Normal
		mdMisionMode_Normal.addSubMode(mdTramoMode_P08_SeguirVVB_finVVV_giroder)
		# Marcamos TramoMode_P00_SituarBNB_finBNB_Avanzar como elegible para MisionMode_Engineering
		mdMisionMode_Engineering.addSubMode(mdTramoMode_P00_SituarBNB_finBNB_Avanzar)
		# Marcamos TramoMode_P01_SeguirBNB_finder_giroder_abrir como elegible para MisionMode_Engineering
		mdMisionMode_Engineering.addSubMode(mdTramoMode_P01_SeguirBNB_finder_giroder_abrir)
		# Marcamos TramoMode_P02_SeguirBNB_finder_giroder como elegible para MisionMode_Engineering
		mdMisionMode_Engineering.addSubMode(mdTramoMode_P02_SeguirBNB_finder_giroder)
		# Marcamos TramoMode_P03_SeguirBNB_finizq_giroizq como elegible para MisionMode_Engineering
		mdMisionMode_Engineering.addSubMode(mdTramoMode_P03_SeguirBNB_finizq_giroizq)
		# Marcamos TramoMode_P04_SeguirBNB_fincruce_rect como elegible para MisionMode_Engineering
		mdMisionMode_Engineering.addSubMode(mdTramoMode_P04_SeguirBNB_fincruce_rect)
		# Marcamos TramoMode_P05_SeguirNNB_finBNB_rect como elegible para MisionMode_Engineering
		mdMisionMode_Engineering.addSubMode(mdTramoMode_P05_SeguirNNB_finBNB_rect)
		# Marcamos TramoMode_P06_SeguirBNB_finizq_giroder como elegible para MisionMode_Engineering
		mdMisionMode_Engineering.addSubMode(mdTramoMode_P06_SeguirBNB_finizq_giroder)
		# Marcamos TramoMode_P07_SituarVVB_finVVB_Avanzar como elegible para MisionMode_Engineering
		mdMisionMode_Engineering.addSubMode(mdTramoMode_P07_SituarVVB_finVVB_Avanzar)
		# Marcamos TramoMode_P08_SeguirVVB_finVVV_giroder como elegible para MisionMode_Engineering
		mdMisionMode_Engineering.addSubMode(mdTramoMode_P08_SeguirVVB_finVVV_giroder)
		# Marcamos TramoMode_Engineering como elegible para MisionMode_Engineering
		mdMisionMode_Engineering.addSubMode(mdTramoMode_Engineering)
		# Marcamos SituacionMode_NNB_00 como elegible para TramoMode_P00_SituarBNB_finBNB_Avanzar
		mdTramoMode_P00_SituarBNB_finBNB_Avanzar.addSubMode(mdSituacionMode_NNB_00)
		# Marcamos SituacionMode_BBB_00 como elegible para TramoMode_P00_SituarBNB_finBNB_Avanzar
		mdTramoMode_P00_SituarBNB_finBNB_Avanzar.addSubMode(mdSituacionMode_BBB_00)
		# Marcamos SituacionMode_BNB_00 como elegible para TramoMode_P00_SituarBNB_finBNB_Avanzar
		mdTramoMode_P00_SituarBNB_finBNB_Avanzar.addSubMode(mdSituacionMode_BNB_00)
		# Marcamos SituacionMode_NNN_00 como elegible para TramoMode_P00_SituarBNB_finBNB_Avanzar
		mdTramoMode_P00_SituarBNB_finBNB_Avanzar.addSubMode(mdSituacionMode_NNN_00)
		# Marcamos SituacionMode_BNN_00 como elegible para TramoMode_P00_SituarBNB_finBNB_Avanzar
		mdTramoMode_P00_SituarBNB_finBNB_Avanzar.addSubMode(mdSituacionMode_BNN_00)
		# Marcamos SituacionMode_BBN_00 como elegible para TramoMode_P00_SituarBNB_finBNB_Avanzar
		mdTramoMode_P00_SituarBNB_finBNB_Avanzar.addSubMode(mdSituacionMode_BBN_00)
		# Marcamos SituacionMode_NBB_00 como elegible para TramoMode_P00_SituarBNB_finBNB_Avanzar
		mdTramoMode_P00_SituarBNB_finBNB_Avanzar.addSubMode(mdSituacionMode_NBB_00)
		# Marcamos SituacionMode_NBN_00 como elegible para TramoMode_P00_SituarBNB_finBNB_Avanzar
		mdTramoMode_P00_SituarBNB_finBNB_Avanzar.addSubMode(mdSituacionMode_NBN_00)
		# Marcamos SituacionMode_NNB_01 como elegible para TramoMode_P01_SeguirBNB_finder_giroder_abrir
		mdTramoMode_P01_SeguirBNB_finder_giroder_abrir.addSubMode(mdSituacionMode_NNB_01)
		# Marcamos SituacionMode_BBB_01 como elegible para TramoMode_P01_SeguirBNB_finder_giroder_abrir
		mdTramoMode_P01_SeguirBNB_finder_giroder_abrir.addSubMode(mdSituacionMode_BBB_01)
		# Marcamos SituacionMode_BNB_01 como elegible para TramoMode_P01_SeguirBNB_finder_giroder_abrir
		mdTramoMode_P01_SeguirBNB_finder_giroder_abrir.addSubMode(mdSituacionMode_BNB_01)
		# Marcamos SituacionMode_NNN_01 como elegible para TramoMode_P01_SeguirBNB_finder_giroder_abrir
		mdTramoMode_P01_SeguirBNB_finder_giroder_abrir.addSubMode(mdSituacionMode_NNN_01)
		# Marcamos SituacionMode_BNN_01 como elegible para TramoMode_P01_SeguirBNB_finder_giroder_abrir
		mdTramoMode_P01_SeguirBNB_finder_giroder_abrir.addSubMode(mdSituacionMode_BNN_01)
		# Marcamos SituacionMode_BBN_01 como elegible para TramoMode_P01_SeguirBNB_finder_giroder_abrir
		mdTramoMode_P01_SeguirBNB_finder_giroder_abrir.addSubMode(mdSituacionMode_BBN_01)
		# Marcamos SituacionMode_NBB_01 como elegible para TramoMode_P01_SeguirBNB_finder_giroder_abrir
		mdTramoMode_P01_SeguirBNB_finder_giroder_abrir.addSubMode(mdSituacionMode_NBB_01)
		# Marcamos SituacionMode_NBN_01 como elegible para TramoMode_P01_SeguirBNB_finder_giroder_abrir
		mdTramoMode_P01_SeguirBNB_finder_giroder_abrir.addSubMode(mdSituacionMode_NBN_01)
		# Marcamos SituacionMode_VBN_01 como elegible para TramoMode_P01_SeguirBNB_finder_giroder_abrir
		mdTramoMode_P01_SeguirBNB_finder_giroder_abrir.addSubMode(mdSituacionMode_VBN_01)
		# Marcamos SituacionMode_NBV_01 como elegible para TramoMode_P01_SeguirBNB_finder_giroder_abrir
		mdTramoMode_P01_SeguirBNB_finder_giroder_abrir.addSubMode(mdSituacionMode_NBV_01)
		# Marcamos SituacionMode_NNB_02 como elegible para TramoMode_P02_SeguirBNB_finder_giroder
		mdTramoMode_P02_SeguirBNB_finder_giroder.addSubMode(mdSituacionMode_NNB_02)
		# Marcamos SituacionMode_BBB_02 como elegible para TramoMode_P02_SeguirBNB_finder_giroder
		mdTramoMode_P02_SeguirBNB_finder_giroder.addSubMode(mdSituacionMode_BBB_02)
		# Marcamos SituacionMode_BNB_02 como elegible para TramoMode_P02_SeguirBNB_finder_giroder
		mdTramoMode_P02_SeguirBNB_finder_giroder.addSubMode(mdSituacionMode_BNB_02)
		# Marcamos SituacionMode_NNN_02 como elegible para TramoMode_P02_SeguirBNB_finder_giroder
		mdTramoMode_P02_SeguirBNB_finder_giroder.addSubMode(mdSituacionMode_NNN_02)
		# Marcamos SituacionMode_BNN_02 como elegible para TramoMode_P02_SeguirBNB_finder_giroder
		mdTramoMode_P02_SeguirBNB_finder_giroder.addSubMode(mdSituacionMode_BNN_02)
		# Marcamos SituacionMode_BBN_02 como elegible para TramoMode_P02_SeguirBNB_finder_giroder
		mdTramoMode_P02_SeguirBNB_finder_giroder.addSubMode(mdSituacionMode_BBN_02)
		# Marcamos SituacionMode_NBB_02 como elegible para TramoMode_P02_SeguirBNB_finder_giroder
		mdTramoMode_P02_SeguirBNB_finder_giroder.addSubMode(mdSituacionMode_NBB_02)
		# Marcamos SituacionMode_NBN_02 como elegible para TramoMode_P02_SeguirBNB_finder_giroder
		mdTramoMode_P02_SeguirBNB_finder_giroder.addSubMode(mdSituacionMode_NBN_02)
		# Marcamos SituacionMode_NBV_02 como elegible para TramoMode_P02_SeguirBNB_finder_giroder
		mdTramoMode_P02_SeguirBNB_finder_giroder.addSubMode(mdSituacionMode_NBV_02)
		# Marcamos SituacionMode_VBN_02 como elegible para TramoMode_P02_SeguirBNB_finder_giroder
		mdTramoMode_P02_SeguirBNB_finder_giroder.addSubMode(mdSituacionMode_VBN_02)
		# Marcamos SituacionMode_BNN_03 como elegible para TramoMode_P03_SeguirBNB_finizq_giroizq
		mdTramoMode_P03_SeguirBNB_finizq_giroizq.addSubMode(mdSituacionMode_BNN_03)
		# Marcamos SituacionMode_BBB_03 como elegible para TramoMode_P03_SeguirBNB_finizq_giroizq
		mdTramoMode_P03_SeguirBNB_finizq_giroizq.addSubMode(mdSituacionMode_BBB_03)
		# Marcamos SituacionMode_BNB_03 como elegible para TramoMode_P03_SeguirBNB_finizq_giroizq
		mdTramoMode_P03_SeguirBNB_finizq_giroizq.addSubMode(mdSituacionMode_BNB_03)
		# Marcamos SituacionMode_NNN_03 como elegible para TramoMode_P03_SeguirBNB_finizq_giroizq
		mdTramoMode_P03_SeguirBNB_finizq_giroizq.addSubMode(mdSituacionMode_NNN_03)
		# Marcamos SituacionMode_NNB_03 como elegible para TramoMode_P03_SeguirBNB_finizq_giroizq
		mdTramoMode_P03_SeguirBNB_finizq_giroizq.addSubMode(mdSituacionMode_NNB_03)
		# Marcamos SituacionMode_BBN_03 como elegible para TramoMode_P03_SeguirBNB_finizq_giroizq
		mdTramoMode_P03_SeguirBNB_finizq_giroizq.addSubMode(mdSituacionMode_BBN_03)
		# Marcamos SituacionMode_NBB_03 como elegible para TramoMode_P03_SeguirBNB_finizq_giroizq
		mdTramoMode_P03_SeguirBNB_finizq_giroizq.addSubMode(mdSituacionMode_NBB_03)
		# Marcamos SituacionMode_NBN_03 como elegible para TramoMode_P03_SeguirBNB_finizq_giroizq
		mdTramoMode_P03_SeguirBNB_finizq_giroizq.addSubMode(mdSituacionMode_NBN_03)
		# Marcamos SituacionMode_NBV_03 como elegible para TramoMode_P03_SeguirBNB_finizq_giroizq
		mdTramoMode_P03_SeguirBNB_finizq_giroizq.addSubMode(mdSituacionMode_NBV_03)
		# Marcamos SituacionMode_VBN_03 como elegible para TramoMode_P03_SeguirBNB_finizq_giroizq
		mdTramoMode_P03_SeguirBNB_finizq_giroizq.addSubMode(mdSituacionMode_VBN_03)
		# Marcamos SituacionMode_BNN_04 como elegible para TramoMode_P04_SeguirBNB_fincruce_rect
		mdTramoMode_P04_SeguirBNB_fincruce_rect.addSubMode(mdSituacionMode_BNN_04)
		# Marcamos SituacionMode_BBB_04 como elegible para TramoMode_P04_SeguirBNB_fincruce_rect
		mdTramoMode_P04_SeguirBNB_fincruce_rect.addSubMode(mdSituacionMode_BBB_04)
		# Marcamos SituacionMode_BNB_04 como elegible para TramoMode_P04_SeguirBNB_fincruce_rect
		mdTramoMode_P04_SeguirBNB_fincruce_rect.addSubMode(mdSituacionMode_BNB_04)
		# Marcamos SituacionMode_NNN_04 como elegible para TramoMode_P04_SeguirBNB_fincruce_rect
		mdTramoMode_P04_SeguirBNB_fincruce_rect.addSubMode(mdSituacionMode_NNN_04)
		# Marcamos SituacionMode_NNB_04 como elegible para TramoMode_P04_SeguirBNB_fincruce_rect
		mdTramoMode_P04_SeguirBNB_fincruce_rect.addSubMode(mdSituacionMode_NNB_04)
		# Marcamos SituacionMode_BBN_04 como elegible para TramoMode_P04_SeguirBNB_fincruce_rect
		mdTramoMode_P04_SeguirBNB_fincruce_rect.addSubMode(mdSituacionMode_BBN_04)
		# Marcamos SituacionMode_NBB_04 como elegible para TramoMode_P04_SeguirBNB_fincruce_rect
		mdTramoMode_P04_SeguirBNB_fincruce_rect.addSubMode(mdSituacionMode_NBB_04)
		# Marcamos SituacionMode_NBN_04 como elegible para TramoMode_P04_SeguirBNB_fincruce_rect
		mdTramoMode_P04_SeguirBNB_fincruce_rect.addSubMode(mdSituacionMode_NBN_04)
		# Marcamos SituacionMode_NBV_04 como elegible para TramoMode_P04_SeguirBNB_fincruce_rect
		mdTramoMode_P04_SeguirBNB_fincruce_rect.addSubMode(mdSituacionMode_NBV_04)
		# Marcamos SituacionMode_VBN_04 como elegible para TramoMode_P04_SeguirBNB_fincruce_rect
		mdTramoMode_P04_SeguirBNB_fincruce_rect.addSubMode(mdSituacionMode_VBN_04)
		# Marcamos SituacionMode_BNN_05 como elegible para TramoMode_P05_SeguirNNB_finBNB_rect
		mdTramoMode_P05_SeguirNNB_finBNB_rect.addSubMode(mdSituacionMode_BNN_05)
		# Marcamos SituacionMode_BBB_05 como elegible para TramoMode_P05_SeguirNNB_finBNB_rect
		mdTramoMode_P05_SeguirNNB_finBNB_rect.addSubMode(mdSituacionMode_BBB_05)
		# Marcamos SituacionMode_BNB_05 como elegible para TramoMode_P05_SeguirNNB_finBNB_rect
		mdTramoMode_P05_SeguirNNB_finBNB_rect.addSubMode(mdSituacionMode_BNB_05)
		# Marcamos SituacionMode_NNN_05 como elegible para TramoMode_P05_SeguirNNB_finBNB_rect
		mdTramoMode_P05_SeguirNNB_finBNB_rect.addSubMode(mdSituacionMode_NNN_05)
		# Marcamos SituacionMode_NNB_05 como elegible para TramoMode_P05_SeguirNNB_finBNB_rect
		mdTramoMode_P05_SeguirNNB_finBNB_rect.addSubMode(mdSituacionMode_NNB_05)
		# Marcamos SituacionMode_BBN_05 como elegible para TramoMode_P05_SeguirNNB_finBNB_rect
		mdTramoMode_P05_SeguirNNB_finBNB_rect.addSubMode(mdSituacionMode_BBN_05)
		# Marcamos SituacionMode_NBB_05 como elegible para TramoMode_P05_SeguirNNB_finBNB_rect
		mdTramoMode_P05_SeguirNNB_finBNB_rect.addSubMode(mdSituacionMode_NBB_05)
		# Marcamos SituacionMode_NBN_05 como elegible para TramoMode_P05_SeguirNNB_finBNB_rect
		mdTramoMode_P05_SeguirNNB_finBNB_rect.addSubMode(mdSituacionMode_NBN_05)
		# Marcamos SituacionMode_BNN_06 como elegible para TramoMode_P06_SeguirBNB_finizq_giroder
		mdTramoMode_P06_SeguirBNB_finizq_giroder.addSubMode(mdSituacionMode_BNN_06)
		# Marcamos SituacionMode_BBB_06 como elegible para TramoMode_P06_SeguirBNB_finizq_giroder
		mdTramoMode_P06_SeguirBNB_finizq_giroder.addSubMode(mdSituacionMode_BBB_06)
		# Marcamos SituacionMode_BNB_06 como elegible para TramoMode_P06_SeguirBNB_finizq_giroder
		mdTramoMode_P06_SeguirBNB_finizq_giroder.addSubMode(mdSituacionMode_BNB_06)
		# Marcamos SituacionMode_NNN_06 como elegible para TramoMode_P06_SeguirBNB_finizq_giroder
		mdTramoMode_P06_SeguirBNB_finizq_giroder.addSubMode(mdSituacionMode_NNN_06)
		# Marcamos SituacionMode_NNB_06 como elegible para TramoMode_P06_SeguirBNB_finizq_giroder
		mdTramoMode_P06_SeguirBNB_finizq_giroder.addSubMode(mdSituacionMode_NNB_06)
		# Marcamos SituacionMode_BBN_06 como elegible para TramoMode_P06_SeguirBNB_finizq_giroder
		mdTramoMode_P06_SeguirBNB_finizq_giroder.addSubMode(mdSituacionMode_BBN_06)
		# Marcamos SituacionMode_NBB_06 como elegible para TramoMode_P06_SeguirBNB_finizq_giroder
		mdTramoMode_P06_SeguirBNB_finizq_giroder.addSubMode(mdSituacionMode_NBB_06)
		# Marcamos SituacionMode_NBN_06 como elegible para TramoMode_P06_SeguirBNB_finizq_giroder
		mdTramoMode_P06_SeguirBNB_finizq_giroder.addSubMode(mdSituacionMode_NBN_06)
		# Marcamos SituacionMode_NBV_06 como elegible para TramoMode_P06_SeguirBNB_finizq_giroder
		mdTramoMode_P06_SeguirBNB_finizq_giroder.addSubMode(mdSituacionMode_NBV_06)
		# Marcamos SituacionMode_BNN_07 como elegible para TramoMode_P07_SituarVVB_finVVB_Avanzar
		mdTramoMode_P07_SituarVVB_finVVB_Avanzar.addSubMode(mdSituacionMode_BNN_07)
		# Marcamos SituacionMode_BBB_07 como elegible para TramoMode_P07_SituarVVB_finVVB_Avanzar
		mdTramoMode_P07_SituarVVB_finVVB_Avanzar.addSubMode(mdSituacionMode_BBB_07)
		# Marcamos SituacionMode_BNB_07 como elegible para TramoMode_P07_SituarVVB_finVVB_Avanzar
		mdTramoMode_P07_SituarVVB_finVVB_Avanzar.addSubMode(mdSituacionMode_BNB_07)
		# Marcamos SituacionMode_NNN_07 como elegible para TramoMode_P07_SituarVVB_finVVB_Avanzar
		mdTramoMode_P07_SituarVVB_finVVB_Avanzar.addSubMode(mdSituacionMode_NNN_07)
		# Marcamos SituacionMode_NNB_07 como elegible para TramoMode_P07_SituarVVB_finVVB_Avanzar
		mdTramoMode_P07_SituarVVB_finVVB_Avanzar.addSubMode(mdSituacionMode_NNB_07)
		# Marcamos SituacionMode_BBN_07 como elegible para TramoMode_P07_SituarVVB_finVVB_Avanzar
		mdTramoMode_P07_SituarVVB_finVVB_Avanzar.addSubMode(mdSituacionMode_BBN_07)
		# Marcamos SituacionMode_NBB_07 como elegible para TramoMode_P07_SituarVVB_finVVB_Avanzar
		mdTramoMode_P07_SituarVVB_finVVB_Avanzar.addSubMode(mdSituacionMode_NBB_07)
		# Marcamos SituacionMode_NBN_07 como elegible para TramoMode_P07_SituarVVB_finVVB_Avanzar
		mdTramoMode_P07_SituarVVB_finVVB_Avanzar.addSubMode(mdSituacionMode_NBN_07)
		# Marcamos SituacionMode_VBN_07 como elegible para TramoMode_P07_SituarVVB_finVVB_Avanzar
		mdTramoMode_P07_SituarVVB_finVVB_Avanzar.addSubMode(mdSituacionMode_VBN_07)
		# Marcamos SituacionMode_VVB_07 como elegible para TramoMode_P07_SituarVVB_finVVB_Avanzar
		mdTramoMode_P07_SituarVVB_finVVB_Avanzar.addSubMode(mdSituacionMode_VVB_07)
		# Marcamos SituacionMode_VVV_07 como elegible para TramoMode_P07_SituarVVB_finVVB_Avanzar
		mdTramoMode_P07_SituarVVB_finVVB_Avanzar.addSubMode(mdSituacionMode_VVV_07)
		# Marcamos SituacionMode_NBV_07 como elegible para TramoMode_P07_SituarVVB_finVVB_Avanzar
		mdTramoMode_P07_SituarVVB_finVVB_Avanzar.addSubMode(mdSituacionMode_NBV_07)
		# Marcamos SituacionMode_VBN_08 como elegible para TramoMode_P08_SeguirVVB_finVVV_giroder
		mdTramoMode_P08_SeguirVVB_finVVV_giroder.addSubMode(mdSituacionMode_VBN_08)
		# Marcamos SituacionMode_VVB_08 como elegible para TramoMode_P08_SeguirVVB_finVVV_giroder
		mdTramoMode_P08_SeguirVVB_finVVV_giroder.addSubMode(mdSituacionMode_VVB_08)
		# Marcamos SituacionMode_VVV_08 como elegible para TramoMode_P08_SeguirVVB_finVVV_giroder
		mdTramoMode_P08_SeguirVVB_finVVV_giroder.addSubMode(mdSituacionMode_VVV_08)
		# Marcamos SituacionMode_BNN_00 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_BNN_00)
		# Marcamos SituacionMode_NBB_00 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_NBB_00)
		# Marcamos SituacionMode_BBB_00 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_BBB_00)
		# Marcamos SituacionMode_NNB_00 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_NNB_00)
		# Marcamos SituacionMode_BNB_00 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_BNB_00)
		# Marcamos SituacionMode_NBN_00 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_NBN_00)
		# Marcamos SituacionMode_BBN_00 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_BBN_00)
		# Marcamos SituacionMode_NNN_00 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_NNN_00)
		# Marcamos SituacionMode_NBV_01 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_NBV_01)
		# Marcamos SituacionMode_BNB_01 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_BNB_01)
		# Marcamos SituacionMode_BBB_01 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_BBB_01)
		# Marcamos SituacionMode_BNN_01 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_BNN_01)
		# Marcamos SituacionMode_NBB_01 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_NBB_01)
		# Marcamos SituacionMode_NNB_01 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_NNB_01)
		# Marcamos SituacionMode_VBN_01 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_VBN_01)
		# Marcamos SituacionMode_BBN_01 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_BBN_01)
		# Marcamos SituacionMode_NNN_01 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_NNN_01)
		# Marcamos SituacionMode_NBN_01 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_NBN_01)
		# Marcamos SituacionMode_BBB_02 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_BBB_02)
		# Marcamos SituacionMode_BBN_02 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_BBN_02)
		# Marcamos SituacionMode_BNB_02 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_BNB_02)
		# Marcamos SituacionMode_BNN_02 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_BNN_02)
		# Marcamos SituacionMode_NBB_02 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_NBB_02)
		# Marcamos SituacionMode_NBN_02 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_NBN_02)
		# Marcamos SituacionMode_NBV_02 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_NBV_02)
		# Marcamos SituacionMode_NNB_02 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_NNB_02)
		# Marcamos SituacionMode_NNN_02 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_NNN_02)
		# Marcamos SituacionMode_VBN_02 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_VBN_02)
		# Marcamos SituacionMode_BBB_03 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_BBB_03)
		# Marcamos SituacionMode_BBN_03 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_BBN_03)
		# Marcamos SituacionMode_BNB_03 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_BNB_03)
		# Marcamos SituacionMode_BNN_03 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_BNN_03)
		# Marcamos SituacionMode_NBB_03 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_NBB_03)
		# Marcamos SituacionMode_NBN_03 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_NBN_03)
		# Marcamos SituacionMode_NBV_03 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_NBV_03)
		# Marcamos SituacionMode_NNB_03 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_NNB_03)
		# Marcamos SituacionMode_NNN_03 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_NNN_03)
		# Marcamos SituacionMode_VBN_03 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_VBN_03)
		# Marcamos SituacionMode_BBB_04 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_BBB_04)
		# Marcamos SituacionMode_BBN_04 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_BBN_04)
		# Marcamos SituacionMode_BNB_04 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_BNB_04)
		# Marcamos SituacionMode_BNN_04 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_BNN_04)
		# Marcamos SituacionMode_NBB_04 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_NBB_04)
		# Marcamos SituacionMode_NBN_04 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_NBN_04)
		# Marcamos SituacionMode_NBV_04 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_NBV_04)
		# Marcamos SituacionMode_NNB_04 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_NNB_04)
		# Marcamos SituacionMode_NNN_04 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_NNN_04)
		# Marcamos SituacionMode_VBN_04 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_VBN_04)
		# Marcamos SituacionMode_BBB_05 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_BBB_05)
		# Marcamos SituacionMode_BBN_05 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_BBN_05)
		# Marcamos SituacionMode_BNB_05 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_BNB_05)
		# Marcamos SituacionMode_BNN_05 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_BNN_05)
		# Marcamos SituacionMode_NBB_05 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_NBB_05)
		# Marcamos SituacionMode_NBN_05 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_NBN_05)
		# Marcamos SituacionMode_NNB_05 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_NNB_05)
		# Marcamos SituacionMode_NNN_05 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_NNN_05)
		# Marcamos SituacionMode_VBN_06 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_VBN_06)
		# Marcamos SituacionMode_NBB_06 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_NBB_06)
		# Marcamos SituacionMode_BNB_06 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_BNB_06)
		# Marcamos SituacionMode_NBN_06 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_NBN_06)
		# Marcamos SituacionMode_NNN_06 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_NNN_06)
		# Marcamos SituacionMode_BNN_06 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_BNN_06)
		# Marcamos SituacionMode_BBN_06 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_BBN_06)
		# Marcamos SituacionMode_BBB_06 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_BBB_06)
		# Marcamos SituacionMode_NBV_06 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_NBV_06)
		# Marcamos SituacionMode_NNB_06 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_NNB_06)
		# Marcamos SituacionMode_BBB_07 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_BBB_07)
		# Marcamos SituacionMode_BBN_07 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_BBN_07)
		# Marcamos SituacionMode_BNB_07 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_BNB_07)
		# Marcamos SituacionMode_BNN_07 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_BNN_07)
		# Marcamos SituacionMode_NBB_07 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_NBB_07)
		# Marcamos SituacionMode_NBN_07 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_NBN_07)
		# Marcamos SituacionMode_NBV_07 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_NBV_07)
		# Marcamos SituacionMode_NNB_07 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_NNB_07)
		# Marcamos SituacionMode_NNN_07 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_NNN_07)
		# Marcamos SituacionMode_VBN_07 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_VBN_07)
		# Marcamos SituacionMode_VVB_07 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_VVB_07)
		# Marcamos SituacionMode_VVV_07 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_VVV_07)
		# Marcamos SituacionMode_VVV_08 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_VVV_08)
		# Marcamos SituacionMode_VBN_08 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_VBN_08)
		# Marcamos SituacionMode_VVB_08 como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_VVB_08)
		# Marcamos SituacionMode_Engineering como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdSituacionMode_Engineering)
		# Marcamos DecisionMovimientoMode_CompasDer como elegible para SituacionMode_BNN_00
		mdSituacionMode_BNN_00.addSubMode(mdDecisionMovimientoMode_CompasDer)
		# Marcamos DecisionMovimientoMode_CompasIzq como elegible para SituacionMode_NBB_00
		mdSituacionMode_NBB_00.addSubMode(mdDecisionMovimientoMode_CompasIzq)
		# Marcamos DecisionMovimientoMode_Avanzar como elegible para SituacionMode_BBB_00
		mdSituacionMode_BBB_00.addSubMode(mdDecisionMovimientoMode_Avanzar)
		# Marcamos DecisionMovimientoMode_CompasIzq como elegible para SituacionMode_NNB_00
		mdSituacionMode_NNB_00.addSubMode(mdDecisionMovimientoMode_CompasIzq)
		# Marcamos DecisionMovimientoMode_Avanzar como elegible para SituacionMode_BNB_00
		mdSituacionMode_BNB_00.addSubMode(mdDecisionMovimientoMode_Avanzar)
		# Marcamos DecisionMovimientoMode_Avanzar como elegible para SituacionMode_NBN_00
		mdSituacionMode_NBN_00.addSubMode(mdDecisionMovimientoMode_Avanzar)
		# Marcamos DecisionMovimientoMode_CompasDer como elegible para SituacionMode_BBN_00
		mdSituacionMode_BBN_00.addSubMode(mdDecisionMovimientoMode_CompasDer)
		# Marcamos DecisionMovimientoMode_Avanzar como elegible para SituacionMode_NNN_00
		mdSituacionMode_NNN_00.addSubMode(mdDecisionMovimientoMode_Avanzar)
		# Marcamos DecisionMovimientoMode_GirarIzq como elegible para SituacionMode_NBV_01
		mdSituacionMode_NBV_01.addSubMode(mdDecisionMovimientoMode_GirarIzq)
		# Marcamos DecisionMovimientoMode_Avanzar como elegible para SituacionMode_BNB_01
		mdSituacionMode_BNB_01.addSubMode(mdDecisionMovimientoMode_Avanzar)
		# Marcamos DecisionMovimientoMode_Parar como elegible para SituacionMode_BBB_01
		mdSituacionMode_BBB_01.addSubMode(mdDecisionMovimientoMode_Parar)
		# Marcamos DecisionMovimientoMode_GirarDer como elegible para SituacionMode_BNN_01
		mdSituacionMode_BNN_01.addSubMode(mdDecisionMovimientoMode_GirarDer)
		# Marcamos DecisionMovimientoMode_CompasIzq como elegible para SituacionMode_NBB_01
		mdSituacionMode_NBB_01.addSubMode(mdDecisionMovimientoMode_CompasIzq)
		# Marcamos DecisionMovimientoMode_CompasIzq como elegible para SituacionMode_NNB_01
		mdSituacionMode_NNB_01.addSubMode(mdDecisionMovimientoMode_CompasIzq)
		# Marcamos DecisionMovimientoMode_GirarDer como elegible para SituacionMode_VBN_01
		mdSituacionMode_VBN_01.addSubMode(mdDecisionMovimientoMode_GirarDer)
		# Marcamos DecisionMovimientoMode_CompasDer como elegible para SituacionMode_BBN_01
		mdSituacionMode_BBN_01.addSubMode(mdDecisionMovimientoMode_CompasDer)
		# Marcamos DecisionMovimientoMode_GirarDer como elegible para SituacionMode_NNN_01
		mdSituacionMode_NNN_01.addSubMode(mdDecisionMovimientoMode_GirarDer)
		# Marcamos DecisionMovimientoMode_Parar como elegible para SituacionMode_NBN_01
		mdSituacionMode_NBN_01.addSubMode(mdDecisionMovimientoMode_Parar)
		# Marcamos DecisionMovimientoMode_Parar como elegible para SituacionMode_BBB_02
		mdSituacionMode_BBB_02.addSubMode(mdDecisionMovimientoMode_Parar)
		# Marcamos DecisionMovimientoMode_CompasDer como elegible para SituacionMode_BBN_02
		mdSituacionMode_BBN_02.addSubMode(mdDecisionMovimientoMode_CompasDer)
		# Marcamos DecisionMovimientoMode_Avanzar como elegible para SituacionMode_BNB_02
		mdSituacionMode_BNB_02.addSubMode(mdDecisionMovimientoMode_Avanzar)
		# Marcamos DecisionMovimientoMode_GirarDer como elegible para SituacionMode_BNN_02
		mdSituacionMode_BNN_02.addSubMode(mdDecisionMovimientoMode_GirarDer)
		# Marcamos DecisionMovimientoMode_CompasIzq como elegible para SituacionMode_NBB_02
		mdSituacionMode_NBB_02.addSubMode(mdDecisionMovimientoMode_CompasIzq)
		# Marcamos DecisionMovimientoMode_Avanzar como elegible para SituacionMode_NBN_02
		mdSituacionMode_NBN_02.addSubMode(mdDecisionMovimientoMode_Avanzar)
		# Marcamos DecisionMovimientoMode_GirarIzq como elegible para SituacionMode_NBV_02
		mdSituacionMode_NBV_02.addSubMode(mdDecisionMovimientoMode_GirarIzq)
		# Marcamos DecisionMovimientoMode_CompasIzq como elegible para SituacionMode_NNB_02
		mdSituacionMode_NNB_02.addSubMode(mdDecisionMovimientoMode_CompasIzq)
		# Marcamos DecisionMovimientoMode_GirarDer como elegible para SituacionMode_NNN_02
		mdSituacionMode_NNN_02.addSubMode(mdDecisionMovimientoMode_GirarDer)
		# Marcamos DecisionMovimientoMode_GirarDer como elegible para SituacionMode_VBN_02
		mdSituacionMode_VBN_02.addSubMode(mdDecisionMovimientoMode_GirarDer)
		# Marcamos DecisionMovimientoMode_Parar como elegible para SituacionMode_BBB_03
		mdSituacionMode_BBB_03.addSubMode(mdDecisionMovimientoMode_Parar)
		# Marcamos DecisionMovimientoMode_CompasDer como elegible para SituacionMode_BBN_03
		mdSituacionMode_BBN_03.addSubMode(mdDecisionMovimientoMode_CompasDer)
		# Marcamos DecisionMovimientoMode_Avanzar como elegible para SituacionMode_BNB_03
		mdSituacionMode_BNB_03.addSubMode(mdDecisionMovimientoMode_Avanzar)
		# Marcamos DecisionMovimientoMode_CompasDer como elegible para SituacionMode_BNN_03
		mdSituacionMode_BNN_03.addSubMode(mdDecisionMovimientoMode_CompasDer)
		# Marcamos DecisionMovimientoMode_CompasIzq como elegible para SituacionMode_NBB_03
		mdSituacionMode_NBB_03.addSubMode(mdDecisionMovimientoMode_CompasIzq)
		# Marcamos DecisionMovimientoMode_Parar como elegible para SituacionMode_NBN_03
		mdSituacionMode_NBN_03.addSubMode(mdDecisionMovimientoMode_Parar)
		# Marcamos DecisionMovimientoMode_GirarIzq como elegible para SituacionMode_NBV_03
		mdSituacionMode_NBV_03.addSubMode(mdDecisionMovimientoMode_GirarIzq)
		# Marcamos DecisionMovimientoMode_GirarIzq como elegible para SituacionMode_NNB_03
		mdSituacionMode_NNB_03.addSubMode(mdDecisionMovimientoMode_GirarIzq)
		# Marcamos DecisionMovimientoMode_GirarIzq como elegible para SituacionMode_NNN_03
		mdSituacionMode_NNN_03.addSubMode(mdDecisionMovimientoMode_GirarIzq)
		# Marcamos DecisionMovimientoMode_GirarDer como elegible para SituacionMode_VBN_03
		mdSituacionMode_VBN_03.addSubMode(mdDecisionMovimientoMode_GirarDer)
		# Marcamos DecisionMovimientoMode_CompasDer como elegible para SituacionMode_BBB_04
		mdSituacionMode_BBB_04.addSubMode(mdDecisionMovimientoMode_CompasDer)
		# Marcamos DecisionMovimientoMode_CompasDer como elegible para SituacionMode_BBN_04
		mdSituacionMode_BBN_04.addSubMode(mdDecisionMovimientoMode_CompasDer)
		# Marcamos DecisionMovimientoMode_Avanzar como elegible para SituacionMode_BNB_04
		mdSituacionMode_BNB_04.addSubMode(mdDecisionMovimientoMode_Avanzar)
		# Marcamos DecisionMovimientoMode_CompasDer como elegible para SituacionMode_BNN_04
		mdSituacionMode_BNN_04.addSubMode(mdDecisionMovimientoMode_CompasDer)
		# Marcamos DecisionMovimientoMode_CompasIzq como elegible para SituacionMode_NBB_04
		mdSituacionMode_NBB_04.addSubMode(mdDecisionMovimientoMode_CompasIzq)
		# Marcamos DecisionMovimientoMode_Parar como elegible para SituacionMode_NBN_04
		mdSituacionMode_NBN_04.addSubMode(mdDecisionMovimientoMode_Parar)
		# Marcamos DecisionMovimientoMode_GirarIzq como elegible para SituacionMode_NBV_04
		mdSituacionMode_NBV_04.addSubMode(mdDecisionMovimientoMode_GirarIzq)
		# Marcamos DecisionMovimientoMode_Avanzar como elegible para SituacionMode_NNB_04
		mdSituacionMode_NNB_04.addSubMode(mdDecisionMovimientoMode_Avanzar)
		# Marcamos DecisionMovimientoMode_CompasDer como elegible para SituacionMode_NNN_04
		mdSituacionMode_NNN_04.addSubMode(mdDecisionMovimientoMode_CompasDer)
		# Marcamos DecisionMovimientoMode_GirarDer como elegible para SituacionMode_VBN_04
		mdSituacionMode_VBN_04.addSubMode(mdDecisionMovimientoMode_GirarDer)
		# Marcamos DecisionMovimientoMode_Parar como elegible para SituacionMode_BBB_05
		mdSituacionMode_BBB_05.addSubMode(mdDecisionMovimientoMode_Parar)
		# Marcamos DecisionMovimientoMode_CompasDer como elegible para SituacionMode_BBN_05
		mdSituacionMode_BBN_05.addSubMode(mdDecisionMovimientoMode_CompasDer)
		# Marcamos DecisionMovimientoMode_Avanzar como elegible para SituacionMode_BNB_05
		mdSituacionMode_BNB_05.addSubMode(mdDecisionMovimientoMode_Avanzar)
		# Marcamos DecisionMovimientoMode_CompasDer como elegible para SituacionMode_BNN_05
		mdSituacionMode_BNN_05.addSubMode(mdDecisionMovimientoMode_CompasDer)
		# Marcamos DecisionMovimientoMode_CompasIzq como elegible para SituacionMode_NBB_05
		mdSituacionMode_NBB_05.addSubMode(mdDecisionMovimientoMode_CompasIzq)
		# Marcamos DecisionMovimientoMode_CompasDer como elegible para SituacionMode_NBN_05
		mdSituacionMode_NBN_05.addSubMode(mdDecisionMovimientoMode_CompasDer)
		# Marcamos DecisionMovimientoMode_Avanzar como elegible para SituacionMode_NNB_05
		mdSituacionMode_NNB_05.addSubMode(mdDecisionMovimientoMode_Avanzar)
		# Marcamos DecisionMovimientoMode_CompasDer como elegible para SituacionMode_NNN_05
		mdSituacionMode_NNN_05.addSubMode(mdDecisionMovimientoMode_CompasDer)
		# Marcamos DecisionMovimientoMode_GirarDer como elegible para SituacionMode_VBN_06
		mdSituacionMode_VBN_06.addSubMode(mdDecisionMovimientoMode_GirarDer)
		# Marcamos DecisionMovimientoMode_CompasIzq como elegible para SituacionMode_NBB_06
		mdSituacionMode_NBB_06.addSubMode(mdDecisionMovimientoMode_CompasIzq)
		# Marcamos DecisionMovimientoMode_Avanzar como elegible para SituacionMode_BNB_06
		mdSituacionMode_BNB_06.addSubMode(mdDecisionMovimientoMode_Avanzar)
		# Marcamos DecisionMovimientoMode_Parar como elegible para SituacionMode_NBN_06
		mdSituacionMode_NBN_06.addSubMode(mdDecisionMovimientoMode_Parar)
		# Marcamos DecisionMovimientoMode_GirarDer como elegible para SituacionMode_NNN_06
		mdSituacionMode_NNN_06.addSubMode(mdDecisionMovimientoMode_GirarDer)
		# Marcamos DecisionMovimientoMode_CompasDer como elegible para SituacionMode_BNN_06
		mdSituacionMode_BNN_06.addSubMode(mdDecisionMovimientoMode_CompasDer)
		# Marcamos DecisionMovimientoMode_CompasDer como elegible para SituacionMode_BBN_06
		mdSituacionMode_BBN_06.addSubMode(mdDecisionMovimientoMode_CompasDer)
		# Marcamos DecisionMovimientoMode_Parar como elegible para SituacionMode_BBB_06
		mdSituacionMode_BBB_06.addSubMode(mdDecisionMovimientoMode_Parar)
		# Marcamos DecisionMovimientoMode_GirarIzq como elegible para SituacionMode_NBV_06
		mdSituacionMode_NBV_06.addSubMode(mdDecisionMovimientoMode_GirarIzq)
		# Marcamos DecisionMovimientoMode_GirarDer como elegible para SituacionMode_NNB_06
		mdSituacionMode_NNB_06.addSubMode(mdDecisionMovimientoMode_GirarDer)
		# Marcamos DecisionMovimientoMode_GirarDer como elegible para SituacionMode_BBB_07
		mdSituacionMode_BBB_07.addSubMode(mdDecisionMovimientoMode_GirarDer)
		# Marcamos DecisionMovimientoMode_GirarDer como elegible para SituacionMode_BBN_07
		mdSituacionMode_BBN_07.addSubMode(mdDecisionMovimientoMode_GirarDer)
		# Marcamos DecisionMovimientoMode_GirarIzq como elegible para SituacionMode_BNB_07
		mdSituacionMode_BNB_07.addSubMode(mdDecisionMovimientoMode_GirarIzq)
		# Marcamos DecisionMovimientoMode_GirarIzq como elegible para SituacionMode_BNN_07
		mdSituacionMode_BNN_07.addSubMode(mdDecisionMovimientoMode_GirarIzq)
		# Marcamos DecisionMovimientoMode_GirarDer como elegible para SituacionMode_NBB_07
		mdSituacionMode_NBB_07.addSubMode(mdDecisionMovimientoMode_GirarDer)
		# Marcamos DecisionMovimientoMode_GirarDer como elegible para SituacionMode_NBN_07
		mdSituacionMode_NBN_07.addSubMode(mdDecisionMovimientoMode_GirarDer)
		# Marcamos DecisionMovimientoMode_Parar como elegible para SituacionMode_NBV_07
		mdSituacionMode_NBV_07.addSubMode(mdDecisionMovimientoMode_Parar)
		# Marcamos DecisionMovimientoMode_GirarDer como elegible para SituacionMode_NNB_07
		mdSituacionMode_NNB_07.addSubMode(mdDecisionMovimientoMode_GirarDer)
		# Marcamos DecisionMovimientoMode_GirarDer como elegible para SituacionMode_NNN_07
		mdSituacionMode_NNN_07.addSubMode(mdDecisionMovimientoMode_GirarDer)
		# Marcamos DecisionMovimientoMode_CompasIzq como elegible para SituacionMode_VBN_07
		mdSituacionMode_VBN_07.addSubMode(mdDecisionMovimientoMode_CompasIzq)
		# Marcamos DecisionMovimientoMode_Avanzar como elegible para SituacionMode_VVB_07
		mdSituacionMode_VVB_07.addSubMode(mdDecisionMovimientoMode_Avanzar)
		# Marcamos DecisionMovimientoMode_GirarDer como elegible para SituacionMode_VVV_07
		mdSituacionMode_VVV_07.addSubMode(mdDecisionMovimientoMode_GirarDer)
		# Marcamos DecisionMovimientoMode_GirarDer como elegible para SituacionMode_VVV_08
		mdSituacionMode_VVV_08.addSubMode(mdDecisionMovimientoMode_GirarDer)
		# Marcamos DecisionMovimientoMode_CompasIzq como elegible para SituacionMode_VBN_08
		mdSituacionMode_VBN_08.addSubMode(mdDecisionMovimientoMode_CompasIzq)
		# Marcamos DecisionMovimientoMode_Avanzar como elegible para SituacionMode_VVB_08
		mdSituacionMode_VVB_08.addSubMode(mdDecisionMovimientoMode_Avanzar)
		# Marcamos DecisionMovimientoMode_Avanzar como elegible para SituacionMode_Engineering
		mdSituacionMode_Engineering.addSubMode(mdDecisionMovimientoMode_Avanzar)
		# Marcamos DecisionMovimientoMode_CompasIzq como elegible para SituacionMode_Engineering
		mdSituacionMode_Engineering.addSubMode(mdDecisionMovimientoMode_CompasIzq)
		# Marcamos DecisionMovimientoMode_CompasDer como elegible para SituacionMode_Engineering
		mdSituacionMode_Engineering.addSubMode(mdDecisionMovimientoMode_CompasDer)
		# Marcamos DecisionMovimientoMode_GirarDer como elegible para SituacionMode_Engineering
		mdSituacionMode_Engineering.addSubMode(mdDecisionMovimientoMode_GirarDer)
		# Marcamos DecisionMovimientoMode_GirarIzq como elegible para SituacionMode_Engineering
		mdSituacionMode_Engineering.addSubMode(mdDecisionMovimientoMode_GirarIzq)
		# Marcamos DecisionMovimientoMode_Parar como elegible para SituacionMode_Engineering
		mdSituacionMode_Engineering.addSubMode(mdDecisionMovimientoMode_Parar)
		# Marcamos DecisionMovimientoMode_Engineering como elegible para SituacionMode_Engineering
		mdSituacionMode_Engineering.addSubMode(mdDecisionMovimientoMode_Engineering)
		# Marcamos RuedaDerMode_Avanzar como elegible para DecisionMovimientoMode_Avanzar
		mdDecisionMovimientoMode_Avanzar.addSubMode(mdRuedaDerMode_Avanzar)
		# Marcamos RuedaDerMode_Avanzar como elegible para DecisionMovimientoMode_CompasIzq
		mdDecisionMovimientoMode_CompasIzq.addSubMode(mdRuedaDerMode_Avanzar)
		# Marcamos RuedaDerMode_Parada como elegible para DecisionMovimientoMode_CompasDer
		mdDecisionMovimientoMode_CompasDer.addSubMode(mdRuedaDerMode_Parada)
		# Marcamos RuedaDerMode_Retroceder como elegible para DecisionMovimientoMode_GirarDer
		mdDecisionMovimientoMode_GirarDer.addSubMode(mdRuedaDerMode_Retroceder)
		# Marcamos RuedaDerMode_Avanzar como elegible para DecisionMovimientoMode_GirarIzq
		mdDecisionMovimientoMode_GirarIzq.addSubMode(mdRuedaDerMode_Avanzar)
		# Marcamos RuedaDerMode_Parada como elegible para DecisionMovimientoMode_Parar
		mdDecisionMovimientoMode_Parar.addSubMode(mdRuedaDerMode_Parada)
		# Marcamos RuedaDerMode_Parada como elegible para DecisionMovimientoMode_Engineering
		mdDecisionMovimientoMode_Engineering.addSubMode(mdRuedaDerMode_Parada)
		# Marcamos RuedaDerMode_Avanzar como elegible para DecisionMovimientoMode_Engineering
		mdDecisionMovimientoMode_Engineering.addSubMode(mdRuedaDerMode_Avanzar)
		# Marcamos RuedaDerMode_Retroceder como elegible para DecisionMovimientoMode_Engineering
		mdDecisionMovimientoMode_Engineering.addSubMode(mdRuedaDerMode_Retroceder)
		# Marcamos RuedaDer_Quieta como elegible para RuedaDerMode_Parada
		mdRuedaDerMode_Parada.addValue(vlRuedaDer_Quieta)
		# Marcamos RuedaDer_Adelante como elegible para RuedaDerMode_Avanzar
		mdRuedaDerMode_Avanzar.addValue(vlRuedaDer_Adelante)
		# Marcamos RuedaDer_Atras como elegible para RuedaDerMode_Retroceder
		mdRuedaDerMode_Retroceder.addValue(vlRuedaDer_Atras)
		# Marcamos RuedaIzqMode_Avanzar como elegible para DecisionMovimientoMode_Avanzar
		mdDecisionMovimientoMode_Avanzar.addSubMode(mdRuedaIzqMode_Avanzar)
		# Marcamos RuedaIzqMode_Parada como elegible para DecisionMovimientoMode_CompasIzq
		mdDecisionMovimientoMode_CompasIzq.addSubMode(mdRuedaIzqMode_Parada)
		# Marcamos RuedaIzqMode_Avanzar como elegible para DecisionMovimientoMode_CompasDer
		mdDecisionMovimientoMode_CompasDer.addSubMode(mdRuedaIzqMode_Avanzar)
		# Marcamos RuedaIzqMode_Avanzar como elegible para DecisionMovimientoMode_GirarDer
		mdDecisionMovimientoMode_GirarDer.addSubMode(mdRuedaIzqMode_Avanzar)
		# Marcamos RuedaIzqMode_Retroceder como elegible para DecisionMovimientoMode_GirarIzq
		mdDecisionMovimientoMode_GirarIzq.addSubMode(mdRuedaIzqMode_Retroceder)
		# Marcamos RuedaIzqMode_Parada como elegible para DecisionMovimientoMode_Parar
		mdDecisionMovimientoMode_Parar.addSubMode(mdRuedaIzqMode_Parada)
		# Marcamos RuedaIzqMode_Parada como elegible para DecisionMovimientoMode_Engineering
		mdDecisionMovimientoMode_Engineering.addSubMode(mdRuedaIzqMode_Parada)
		# Marcamos RuedaIzqMode_Avanzar como elegible para DecisionMovimientoMode_Engineering
		mdDecisionMovimientoMode_Engineering.addSubMode(mdRuedaIzqMode_Avanzar)
		# Marcamos RuedaIzqMode_Retroceder como elegible para DecisionMovimientoMode_Engineering
		mdDecisionMovimientoMode_Engineering.addSubMode(mdRuedaIzqMode_Retroceder)
		# Marcamos RuedaIzq_Quieta como elegible para RuedaIzqMode_Parada
		mdRuedaIzqMode_Parada.addValue(vlRuedaIzq_Quieta)
		# Marcamos RuedaIzq_Adelante como elegible para RuedaIzqMode_Avanzar
		mdRuedaIzqMode_Avanzar.addValue(vlRuedaIzq_Adelante)
		# Marcamos RuedaIzq_Atras como elegible para RuedaIzqMode_Retroceder
		mdRuedaIzqMode_Retroceder.addValue(vlRuedaIzq_Atras)
		# Marcamos NuevoPasoMode_Si como elegible para SituacionMode_BNB_00
		mdSituacionMode_BNB_00.addSubMode(mdNuevoPasoMode_Si)
		# Marcamos NuevoPasoMode_Si como elegible para SituacionMode_BNN_01
		mdSituacionMode_BNN_01.addSubMode(mdNuevoPasoMode_Si)
		# Marcamos NuevoPasoMode_Si como elegible para SituacionMode_NNN_01
		mdSituacionMode_NNN_01.addSubMode(mdNuevoPasoMode_Si)
		# Marcamos NuevoPasoMode_Si como elegible para SituacionMode_BNN_02
		mdSituacionMode_BNN_02.addSubMode(mdNuevoPasoMode_Si)
		# Marcamos NuevoPasoMode_Si como elegible para SituacionMode_NNN_02
		mdSituacionMode_NNN_02.addSubMode(mdNuevoPasoMode_Si)
		# Marcamos NuevoPasoMode_Si como elegible para SituacionMode_NNB_03
		mdSituacionMode_NNB_03.addSubMode(mdNuevoPasoMode_Si)
		# Marcamos NuevoPasoMode_Si como elegible para SituacionMode_NNN_03
		mdSituacionMode_NNN_03.addSubMode(mdNuevoPasoMode_Si)
		# Marcamos NuevoPasoMode_Si como elegible para SituacionMode_NNB_04
		mdSituacionMode_NNB_04.addSubMode(mdNuevoPasoMode_Si)
		# Marcamos NuevoPasoMode_Si como elegible para SituacionMode_NNN_04
		mdSituacionMode_NNN_04.addSubMode(mdNuevoPasoMode_Si)
		# Marcamos NuevoPasoMode_Si como elegible para SituacionMode_BNB_05
		mdSituacionMode_BNB_05.addSubMode(mdNuevoPasoMode_Si)
		# Marcamos NuevoPasoMode_Si como elegible para SituacionMode_NNN_06
		mdSituacionMode_NNN_06.addSubMode(mdNuevoPasoMode_Si)
		# Marcamos NuevoPasoMode_Si como elegible para SituacionMode_NNB_06
		mdSituacionMode_NNB_06.addSubMode(mdNuevoPasoMode_Si)
		# Marcamos NuevoPasoMode_Si como elegible para SituacionMode_VVB_07
		mdSituacionMode_VVB_07.addSubMode(mdNuevoPasoMode_Si)
		# Marcamos NuevoPasoMode_Si como elegible para SituacionMode_VVV_08
		mdSituacionMode_VVV_08.addSubMode(mdNuevoPasoMode_Si)
		# Marcamos NuevoPasoMode_Si como elegible para SituacionMode_Engineering
		mdSituacionMode_Engineering.addSubMode(mdNuevoPasoMode_Si)
		# Marcamos DecisionSeguidorMode_BNB como elegible para SituacionMode_BNB_01
		mdSituacionMode_BNB_01.addSubMode(mdDecisionSeguidorMode_BNB)
		# Marcamos DecisionSeguidorMode_BNB como elegible para SituacionMode_BNB_02
		mdSituacionMode_BNB_02.addSubMode(mdDecisionSeguidorMode_BNB)
		# Marcamos DecisionSeguidorMode_BNB como elegible para SituacionMode_BNB_03
		mdSituacionMode_BNB_03.addSubMode(mdDecisionSeguidorMode_BNB)
		# Marcamos DecisionSeguidorMode_BNB como elegible para SituacionMode_BNB_04
		mdSituacionMode_BNB_04.addSubMode(mdDecisionSeguidorMode_BNB)
		# Marcamos DecisionSeguidorMode_BNB como elegible para SituacionMode_BNB_05
		mdSituacionMode_BNB_05.addSubMode(mdDecisionSeguidorMode_BNB)
		# Marcamos DecisionSeguidorMode_BNB como elegible para SituacionMode_BNB_06
		mdSituacionMode_BNB_06.addSubMode(mdDecisionSeguidorMode_BNB)
		# Marcamos DecisionSeguidorMode_VVB como elegible para SituacionMode_VVB_07
		mdSituacionMode_VVB_07.addSubMode(mdDecisionSeguidorMode_VVB)
		# Marcamos DecisionSeguidorMode_VVB como elegible para SituacionMode_VVB_08
		mdSituacionMode_VVB_08.addSubMode(mdDecisionSeguidorMode_VVB)
		# Marcamos DecisionSeguidorMode_BNB como elegible para SituacionMode_Engineering
		mdSituacionMode_Engineering.addSubMode(mdDecisionSeguidorMode_BNB)
		# Marcamos DecisionSeguidorMode_VVB como elegible para SituacionMode_Engineering
		mdSituacionMode_Engineering.addSubMode(mdDecisionSeguidorMode_VVB)
		# Marcamos DecisionAparejoMode_Cerrado como elegible para TramoMode_P00_SituarBNB_finBNB_Avanzar
		mdTramoMode_P00_SituarBNB_finBNB_Avanzar.addSubMode(mdDecisionAparejoMode_Cerrado)
		# Marcamos DecisionAparejoMode_Cerrado como elegible para TramoMode_P01_SeguirBNB_finder_giroder_abrir
		mdTramoMode_P01_SeguirBNB_finder_giroder_abrir.addSubMode(mdDecisionAparejoMode_Cerrado)
		# Marcamos DecisionAparejoMode_Abierto como elegible para TramoMode_P02_SeguirBNB_finder_giroder
		mdTramoMode_P02_SeguirBNB_finder_giroder.addSubMode(mdDecisionAparejoMode_Abierto)
		# Marcamos DecisionAparejoMode_Abierto como elegible para TramoMode_P03_SeguirBNB_finizq_giroizq
		mdTramoMode_P03_SeguirBNB_finizq_giroizq.addSubMode(mdDecisionAparejoMode_Abierto)
		# Marcamos DecisionAparejoMode_Abierto como elegible para TramoMode_P04_SeguirBNB_fincruce_rect
		mdTramoMode_P04_SeguirBNB_fincruce_rect.addSubMode(mdDecisionAparejoMode_Abierto)
		# Marcamos DecisionAparejoMode_Abierto como elegible para TramoMode_P05_SeguirNNB_finBNB_rect
		mdTramoMode_P05_SeguirNNB_finBNB_rect.addSubMode(mdDecisionAparejoMode_Abierto)
		# Marcamos DecisionAparejoMode_Abierto como elegible para TramoMode_P06_SeguirBNB_finizq_giroder
		mdTramoMode_P06_SeguirBNB_finizq_giroder.addSubMode(mdDecisionAparejoMode_Abierto)
		# Marcamos DecisionAparejoMode_Abierto como elegible para TramoMode_P07_SituarVVB_finVVB_Avanzar
		mdTramoMode_P07_SituarVVB_finVVB_Avanzar.addSubMode(mdDecisionAparejoMode_Abierto)
		# Marcamos DecisionAparejoMode_Abierto como elegible para TramoMode_P08_SeguirVVB_finVVV_giroder
		mdTramoMode_P08_SeguirVVB_finVVV_giroder.addSubMode(mdDecisionAparejoMode_Abierto)
		# Marcamos DecisionAparejoMode_Abierto como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdDecisionAparejoMode_Abierto)
		# Marcamos DecisionAparejoMode_Medio como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdDecisionAparejoMode_Medio)
		# Marcamos DecisionAparejoMode_Cerrado como elegible para TramoMode_Engineering
		mdTramoMode_Engineering.addSubMode(mdDecisionAparejoMode_Cerrado)

