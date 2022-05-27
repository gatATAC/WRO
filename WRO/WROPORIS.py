from PORIS import *

class WROPORIS:
	def __init__(self):
		idcounter = 1
		self.sysMision = PORISSys("Mision")
		self.mdMisionUNKNOWN = PORISMode("UNKNOWN")
		self.root = self.sysMision
		self.sysTramo = PORISSys("Tramo")
		self.mdTramoUNKNOWN = PORISMode("UNKNOWN")
		self.sysSituacion = PORISSys("Situacion")
		self.mdSituacionUNKNOWN = PORISMode("UNKNOWN")
		self.sysDecisionMovimiento = PORISSys("DecisionMovimiento")
		self.mdDecisionMovimientoUNKNOWN = PORISMode("UNKNOWN")
		self.prRuedaDer = PORISParam("RuedaDer")
		self.mdRuedaDerUNKNOWN = PORISMode("UNKNOWN")
		self.vlRuedaDer_UNKNOWN = PORISValue("UNKNOWN")
		self.prRuedaIzq = PORISParam("RuedaIzq")
		self.mdRuedaIzqUNKNOWN = PORISMode("UNKNOWN")
		self.vlRuedaIzq_UNKNOWN = PORISValue("UNKNOWN")
		self.sysNuevoPaso = PORISSys("NuevoPaso")
		self.mdNuevoPasoUNKNOWN = PORISMode("UNKNOWN")
		self.sysDecisionSeguidor = PORISSys("DecisionSeguidor")
		self.mdDecisionSeguidorUNKNOWN = PORISMode("UNKNOWN")
		self.sysDecisionAparejo = PORISSys("DecisionAparejo")
		self.mdDecisionAparejoUNKNOWN = PORISMode("UNKNOWN")
		self.mdRuedaDerParada = PORISMode("Parada")
		self.mdRuedaDerAvanzar = PORISMode("Avanzar")
		self.mdRuedaDerRetroceder = PORISMode("Retroceder")
		self.vlRuedaDer_Quieta = PORISValue("Quieta")
		self.vlRuedaDer_Adelante = PORISValue("Adelante")
		self.vlRuedaDer_Atras = PORISValue("Atras")
		self.mdRuedaIzqParada = PORISMode("Parada")
		self.mdRuedaIzqAvanzar = PORISMode("Avanzar")
		self.mdRuedaIzqRetroceder = PORISMode("Retroceder")
		self.vlRuedaIzq_Quieta = PORISValue("Quieta")
		self.vlRuedaIzq_Adelante = PORISValue("Adelante")
		self.vlRuedaIzq_Atras = PORISValue("Atras")
		self.mdDecisionMovimientoAvanzar = PORISMode("Avanzar")
		self.mdDecisionMovimientoCompasIzq = PORISMode("CompasIzq")
		self.mdDecisionMovimientoCompasDer = PORISMode("CompasDer")
		self.mdDecisionMovimientoGirarDer = PORISMode("GirarDer")
		self.mdDecisionMovimientoGirarIzq = PORISMode("GirarIzq")
		self.mdDecisionMovimientoParar = PORISMode("Parar")
		self.mdSituacionBNN_00 = PORISMode("BNN_00")
		self.mdSituacionNBB_00 = PORISMode("NBB_00")
		self.mdSituacionBBB_00 = PORISMode("BBB_00")
		self.mdSituacionNNB_00 = PORISMode("NNB_00")
		self.mdSituacionBNB_00 = PORISMode("BNB_00")
		self.mdSituacionNBN_00 = PORISMode("NBN_00")
		self.mdNuevoPasoSi = PORISMode("Si")
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
		self.mdDecisionSeguidorBNB = PORISMode("BNB")
		self.mdDecisionSeguidorVVB = PORISMode("VVB")
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
		self.mdTramoP00 = PORISMode("P00")
		self.mdTramoP01 = PORISMode("P01")
		self.mdTramoP02 = PORISMode("P02")
		self.mdTramoP03 = PORISMode("P03")
		self.mdTramoP04 = PORISMode("P04")
		self.mdTramoP05 = PORISMode("P05")
		self.mdTramoP06 = PORISMode("P06")
		self.mdTramoP07 = PORISMode("P07")
		self.mdTramoP08 = PORISMode("P08")
		self.mdDecisionAparejoCerrado = PORISMode("Cerrado")
		self.mdDecisionAparejoAbierto = PORISMode("Abierto")
		self.mdDecisionAparejoMedio = PORISMode("Medio")
		self.mdMisionNormal = PORISMode("Normal")

		self.sysMision.id = idcounter
		idcounter += 1

		self.mdMisionUNKNOWN.id = idcounter
		idcounter += 1
		self.sysMision.addMode(self.mdMisionUNKNOWN)

		self.sysTramo.id = idcounter
		idcounter += 1
		self.sysMision.addSubsystem(self.sysTramo)

		self.mdTramoUNKNOWN.id = idcounter
		idcounter += 1
		self.sysTramo.addMode(self.mdTramoUNKNOWN)

		self.sysSituacion.id = idcounter
		idcounter += 1
		self.sysTramo.addSubsystem(self.sysSituacion)

		self.mdSituacionUNKNOWN.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionUNKNOWN)

		self.sysDecisionMovimiento.id = idcounter
		idcounter += 1
		self.sysSituacion.addSubsystem(self.sysDecisionMovimiento)

		self.mdDecisionMovimientoUNKNOWN.id = idcounter
		idcounter += 1
		self.sysDecisionMovimiento.addMode(self.mdDecisionMovimientoUNKNOWN)

		self.prRuedaDer.id = idcounter
		idcounter += 1
		self.sysDecisionMovimiento.addParam(self.prRuedaDer)
		idcounter += 1
		self.prRuedaDer.addValue(self.vlRuedaDer_UNKNOWN)

		self.mdRuedaDerUNKNOWN.id = idcounter
		idcounter += 1
		self.prRuedaDer.addMode(self.mdRuedaDerUNKNOWN)
		self.mdRuedaDerUNKNOWN.addValue(self.vlRuedaDer_UNKNOWN)
		self.mdDecisionMovimientoUNKNOWN.addSubMode(self.mdRuedaDerUNKNOWN)

		self.prRuedaIzq.id = idcounter
		idcounter += 1
		self.sysDecisionMovimiento.addParam(self.prRuedaIzq)
		idcounter += 1
		self.prRuedaIzq.addValue(self.vlRuedaIzq_UNKNOWN)

		self.mdRuedaIzqUNKNOWN.id = idcounter
		idcounter += 1
		self.prRuedaIzq.addMode(self.mdRuedaIzqUNKNOWN)
		self.mdRuedaIzqUNKNOWN.addValue(self.vlRuedaIzq_UNKNOWN)
		self.mdDecisionMovimientoUNKNOWN.addSubMode(self.mdRuedaIzqUNKNOWN)

		self.sysNuevoPaso.id = idcounter
		idcounter += 1
		self.sysSituacion.addSubsystem(self.sysNuevoPaso)

		self.mdNuevoPasoUNKNOWN.id = idcounter
		idcounter += 1
		self.sysNuevoPaso.addMode(self.mdNuevoPasoUNKNOWN)

		self.sysDecisionSeguidor.id = idcounter
		idcounter += 1
		self.sysSituacion.addSubsystem(self.sysDecisionSeguidor)

		self.mdDecisionSeguidorUNKNOWN.id = idcounter
		idcounter += 1
		self.sysDecisionSeguidor.addMode(self.mdDecisionSeguidorUNKNOWN)

		self.sysDecisionAparejo.id = idcounter
		idcounter += 1
		self.sysTramo.addSubsystem(self.sysDecisionAparejo)

		self.mdDecisionAparejoUNKNOWN.id = idcounter
		idcounter += 1
		self.sysDecisionAparejo.addMode(self.mdDecisionAparejoUNKNOWN)

		self.mdRuedaDerParada.id = idcounter
		idcounter += 1
		self.prRuedaDer.addMode(self.mdRuedaDerParada)

		self.mdRuedaDerAvanzar.id = idcounter
		idcounter += 1
		self.prRuedaDer.addMode(self.mdRuedaDerAvanzar)

		self.mdRuedaDerRetroceder.id = idcounter
		idcounter += 1
		self.prRuedaDer.addMode(self.mdRuedaDerRetroceder)

		self.vlRuedaDer_Quieta.id = idcounter
		idcounter += 1
		self.prRuedaDer.addValue(self.vlRuedaDer_Quieta)

		self.vlRuedaDer_Adelante.id = idcounter
		idcounter += 1
		self.prRuedaDer.addValue(self.vlRuedaDer_Adelante)

		self.vlRuedaDer_Atras.id = idcounter
		idcounter += 1
		self.prRuedaDer.addValue(self.vlRuedaDer_Atras)

		self.mdRuedaIzqParada.id = idcounter
		idcounter += 1
		self.prRuedaIzq.addMode(self.mdRuedaIzqParada)

		self.mdRuedaIzqAvanzar.id = idcounter
		idcounter += 1
		self.prRuedaIzq.addMode(self.mdRuedaIzqAvanzar)

		self.mdRuedaIzqRetroceder.id = idcounter
		idcounter += 1
		self.prRuedaIzq.addMode(self.mdRuedaIzqRetroceder)

		self.vlRuedaIzq_Quieta.id = idcounter
		idcounter += 1
		self.prRuedaIzq.addValue(self.vlRuedaIzq_Quieta)

		self.vlRuedaIzq_Adelante.id = idcounter
		idcounter += 1
		self.prRuedaIzq.addValue(self.vlRuedaIzq_Adelante)

		self.vlRuedaIzq_Atras.id = idcounter
		idcounter += 1
		self.prRuedaIzq.addValue(self.vlRuedaIzq_Atras)

		self.mdDecisionMovimientoAvanzar.id = idcounter
		idcounter += 1
		self.sysDecisionMovimiento.addMode(self.mdDecisionMovimientoAvanzar)

		self.mdDecisionMovimientoCompasIzq.id = idcounter
		idcounter += 1
		self.sysDecisionMovimiento.addMode(self.mdDecisionMovimientoCompasIzq)

		self.mdDecisionMovimientoCompasDer.id = idcounter
		idcounter += 1
		self.sysDecisionMovimiento.addMode(self.mdDecisionMovimientoCompasDer)

		self.mdDecisionMovimientoGirarDer.id = idcounter
		idcounter += 1
		self.sysDecisionMovimiento.addMode(self.mdDecisionMovimientoGirarDer)

		self.mdDecisionMovimientoGirarIzq.id = idcounter
		idcounter += 1
		self.sysDecisionMovimiento.addMode(self.mdDecisionMovimientoGirarIzq)

		self.mdDecisionMovimientoParar.id = idcounter
		idcounter += 1
		self.sysDecisionMovimiento.addMode(self.mdDecisionMovimientoParar)

		self.mdSituacionBNN_00.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionBNN_00)

		self.mdSituacionNBB_00.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionNBB_00)

		self.mdSituacionBBB_00.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionBBB_00)

		self.mdSituacionNNB_00.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionNNB_00)

		self.mdSituacionBNB_00.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionBNB_00)

		self.mdSituacionNBN_00.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionNBN_00)

		self.mdNuevoPasoSi.id = idcounter
		idcounter += 1
		self.sysNuevoPaso.addMode(self.mdNuevoPasoSi)

		self.mdSituacionBBN_00.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionBBN_00)

		self.mdSituacionNNN_00.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionNNN_00)

		self.mdSituacionNBV_01.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionNBV_01)

		self.mdSituacionBNB_01.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionBNB_01)

		self.mdSituacionBBB_01.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionBBB_01)

		self.mdSituacionBNN_01.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionBNN_01)

		self.mdSituacionNBB_01.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionNBB_01)

		self.mdSituacionNNB_01.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionNNB_01)

		self.mdSituacionVBN_01.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionVBN_01)

		self.mdSituacionBBN_01.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionBBN_01)

		self.mdSituacionNNN_01.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionNNN_01)

		self.mdSituacionNBN_01.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionNBN_01)

		self.mdDecisionSeguidorBNB.id = idcounter
		idcounter += 1
		self.sysDecisionSeguidor.addMode(self.mdDecisionSeguidorBNB)

		self.mdDecisionSeguidorVVB.id = idcounter
		idcounter += 1
		self.sysDecisionSeguidor.addMode(self.mdDecisionSeguidorVVB)

		self.mdSituacionBBB_02.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionBBB_02)

		self.mdSituacionBBN_02.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionBBN_02)

		self.mdSituacionBNB_02.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionBNB_02)

		self.mdSituacionBNN_02.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionBNN_02)

		self.mdSituacionNBB_02.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionNBB_02)

		self.mdSituacionNBN_02.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionNBN_02)

		self.mdSituacionNBV_02.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionNBV_02)

		self.mdSituacionNNB_02.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionNNB_02)

		self.mdSituacionNNN_02.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionNNN_02)

		self.mdSituacionVBN_02.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionVBN_02)

		self.mdSituacionBBB_03.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionBBB_03)

		self.mdSituacionBBN_03.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionBBN_03)

		self.mdSituacionBNB_03.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionBNB_03)

		self.mdSituacionBNN_03.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionBNN_03)

		self.mdSituacionNBB_03.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionNBB_03)

		self.mdSituacionNBN_03.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionNBN_03)

		self.mdSituacionNBV_03.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionNBV_03)

		self.mdSituacionNNB_03.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionNNB_03)

		self.mdSituacionNNN_03.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionNNN_03)

		self.mdSituacionVBN_03.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionVBN_03)

		self.mdSituacionBBB_04.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionBBB_04)

		self.mdSituacionBBN_04.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionBBN_04)

		self.mdSituacionBNB_04.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionBNB_04)

		self.mdSituacionBNN_04.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionBNN_04)

		self.mdSituacionNBB_04.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionNBB_04)

		self.mdSituacionNBN_04.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionNBN_04)

		self.mdSituacionNBV_04.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionNBV_04)

		self.mdSituacionNNB_04.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionNNB_04)

		self.mdSituacionNNN_04.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionNNN_04)

		self.mdSituacionVBN_04.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionVBN_04)

		self.mdSituacionBBB_05.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionBBB_05)

		self.mdSituacionBBN_05.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionBBN_05)

		self.mdSituacionBNB_05.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionBNB_05)

		self.mdSituacionBNN_05.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionBNN_05)

		self.mdSituacionNBB_05.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionNBB_05)

		self.mdSituacionNBN_05.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionNBN_05)

		self.mdSituacionNNB_05.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionNNB_05)

		self.mdSituacionNNN_05.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionNNN_05)

		self.mdSituacionVBN_06.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionVBN_06)

		self.mdSituacionNBB_06.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionNBB_06)

		self.mdSituacionBNB_06.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionBNB_06)

		self.mdSituacionNBN_06.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionNBN_06)

		self.mdSituacionNNN_06.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionNNN_06)

		self.mdSituacionBNN_06.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionBNN_06)

		self.mdSituacionBBN_06.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionBBN_06)

		self.mdSituacionBBB_06.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionBBB_06)

		self.mdSituacionNBV_06.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionNBV_06)

		self.mdSituacionNNB_06.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionNNB_06)

		self.mdSituacionBBB_07.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionBBB_07)

		self.mdSituacionBBN_07.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionBBN_07)

		self.mdSituacionBNB_07.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionBNB_07)

		self.mdSituacionBNN_07.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionBNN_07)

		self.mdSituacionNBB_07.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionNBB_07)

		self.mdSituacionNBN_07.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionNBN_07)

		self.mdSituacionNBV_07.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionNBV_07)

		self.mdSituacionNNB_07.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionNNB_07)

		self.mdSituacionNNN_07.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionNNN_07)

		self.mdSituacionVBN_07.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionVBN_07)

		self.mdSituacionVVB_07.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionVVB_07)

		self.mdSituacionVVV_07.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionVVV_07)

		self.mdSituacionVVV_08.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionVVV_08)

		self.mdSituacionVBN_08.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionVBN_08)

		self.mdSituacionVVB_08.id = idcounter
		idcounter += 1
		self.sysSituacion.addMode(self.mdSituacionVVB_08)

		self.mdTramoP00.id = idcounter
		idcounter += 1
		self.sysTramo.addMode(self.mdTramoP00)

		self.mdTramoP01.id = idcounter
		idcounter += 1
		self.sysTramo.addMode(self.mdTramoP01)

		self.mdTramoP02.id = idcounter
		idcounter += 1
		self.sysTramo.addMode(self.mdTramoP02)

		self.mdTramoP03.id = idcounter
		idcounter += 1
		self.sysTramo.addMode(self.mdTramoP03)

		self.mdTramoP04.id = idcounter
		idcounter += 1
		self.sysTramo.addMode(self.mdTramoP04)

		self.mdTramoP05.id = idcounter
		idcounter += 1
		self.sysTramo.addMode(self.mdTramoP05)

		self.mdTramoP06.id = idcounter
		idcounter += 1
		self.sysTramo.addMode(self.mdTramoP06)

		self.mdTramoP07.id = idcounter
		idcounter += 1
		self.sysTramo.addMode(self.mdTramoP07)

		self.mdTramoP08.id = idcounter
		idcounter += 1
		self.sysTramo.addMode(self.mdTramoP08)

		self.mdDecisionAparejoCerrado.id = idcounter
		idcounter += 1
		self.sysDecisionAparejo.addMode(self.mdDecisionAparejoCerrado)

		self.mdDecisionAparejoAbierto.id = idcounter
		idcounter += 1
		self.sysDecisionAparejo.addMode(self.mdDecisionAparejoAbierto)

		self.mdDecisionAparejoMedio.id = idcounter
		idcounter += 1
		self.sysDecisionAparejo.addMode(self.mdDecisionAparejoMedio)

		self.mdMisionNormal.id = idcounter
		idcounter += 1
		self.sysMision.addMode(self.mdMisionNormal)
		self.mdMisionNormal.addSubMode(self.mdTramoP00)
		self.mdMisionNormal.addSubMode(self.mdTramoP01)
		self.mdMisionNormal.addSubMode(self.mdTramoP02)
		self.mdMisionNormal.addSubMode(self.mdTramoP03)
		self.mdMisionNormal.addSubMode(self.mdTramoP04)
		self.mdMisionNormal.addSubMode(self.mdTramoP05)
		self.mdMisionNormal.addSubMode(self.mdTramoP06)
		self.mdMisionNormal.addSubMode(self.mdTramoP07)
		self.mdMisionNormal.addSubMode(self.mdTramoP08)
		self.mdTramoP00.addSubMode(self.mdSituacionNNB_00)
		self.mdTramoP00.addSubMode(self.mdSituacionBBB_00)
		self.mdTramoP00.addSubMode(self.mdSituacionBNB_00)
		self.mdTramoP00.addSubMode(self.mdSituacionNNN_00)
		self.mdTramoP00.addSubMode(self.mdSituacionBNN_00)
		self.mdTramoP00.addSubMode(self.mdSituacionBBN_00)
		self.mdTramoP00.addSubMode(self.mdSituacionNBB_00)
		self.mdTramoP00.addSubMode(self.mdSituacionNBN_00)
		self.mdTramoP01.addSubMode(self.mdSituacionNNB_01)
		self.mdTramoP01.addSubMode(self.mdSituacionBBB_01)
		self.mdTramoP01.addSubMode(self.mdSituacionBNB_01)
		self.mdTramoP01.addSubMode(self.mdSituacionNNN_01)
		self.mdTramoP01.addSubMode(self.mdSituacionBNN_01)
		self.mdTramoP01.addSubMode(self.mdSituacionBBN_01)
		self.mdTramoP01.addSubMode(self.mdSituacionNBB_01)
		self.mdTramoP01.addSubMode(self.mdSituacionNBN_01)
		self.mdTramoP01.addSubMode(self.mdSituacionVBN_01)
		self.mdTramoP01.addSubMode(self.mdSituacionNBV_01)
		self.mdTramoP02.addSubMode(self.mdSituacionNNB_02)
		self.mdTramoP02.addSubMode(self.mdSituacionBBB_02)
		self.mdTramoP02.addSubMode(self.mdSituacionBNB_02)
		self.mdTramoP02.addSubMode(self.mdSituacionNNN_02)
		self.mdTramoP02.addSubMode(self.mdSituacionBNN_02)
		self.mdTramoP02.addSubMode(self.mdSituacionBBN_02)
		self.mdTramoP02.addSubMode(self.mdSituacionNBB_02)
		self.mdTramoP02.addSubMode(self.mdSituacionNBN_02)
		self.mdTramoP02.addSubMode(self.mdSituacionNBV_02)
		self.mdTramoP02.addSubMode(self.mdSituacionVBN_02)
		self.mdTramoP03.addSubMode(self.mdSituacionBNN_03)
		self.mdTramoP03.addSubMode(self.mdSituacionBBB_03)
		self.mdTramoP03.addSubMode(self.mdSituacionBNB_03)
		self.mdTramoP03.addSubMode(self.mdSituacionNNN_03)
		self.mdTramoP03.addSubMode(self.mdSituacionNNB_03)
		self.mdTramoP03.addSubMode(self.mdSituacionBBN_03)
		self.mdTramoP03.addSubMode(self.mdSituacionNBB_03)
		self.mdTramoP03.addSubMode(self.mdSituacionNBN_03)
		self.mdTramoP03.addSubMode(self.mdSituacionNBV_03)
		self.mdTramoP03.addSubMode(self.mdSituacionVBN_03)
		self.mdTramoP04.addSubMode(self.mdSituacionBNN_04)
		self.mdTramoP04.addSubMode(self.mdSituacionBBB_04)
		self.mdTramoP04.addSubMode(self.mdSituacionBNB_04)
		self.mdTramoP04.addSubMode(self.mdSituacionNNN_04)
		self.mdTramoP04.addSubMode(self.mdSituacionNNB_04)
		self.mdTramoP04.addSubMode(self.mdSituacionBBN_04)
		self.mdTramoP04.addSubMode(self.mdSituacionNBB_04)
		self.mdTramoP04.addSubMode(self.mdSituacionNBN_04)
		self.mdTramoP04.addSubMode(self.mdSituacionNBV_04)
		self.mdTramoP04.addSubMode(self.mdSituacionVBN_04)
		self.mdTramoP05.addSubMode(self.mdSituacionBNN_05)
		self.mdTramoP05.addSubMode(self.mdSituacionBBB_05)
		self.mdTramoP05.addSubMode(self.mdSituacionBNB_05)
		self.mdTramoP05.addSubMode(self.mdSituacionNNN_05)
		self.mdTramoP05.addSubMode(self.mdSituacionNNB_05)
		self.mdTramoP05.addSubMode(self.mdSituacionBBN_05)
		self.mdTramoP05.addSubMode(self.mdSituacionNBB_05)
		self.mdTramoP05.addSubMode(self.mdSituacionNBN_05)
		self.mdTramoP06.addSubMode(self.mdSituacionBNN_06)
		self.mdTramoP06.addSubMode(self.mdSituacionBBB_06)
		self.mdTramoP06.addSubMode(self.mdSituacionBNB_06)
		self.mdTramoP06.addSubMode(self.mdSituacionNNN_06)
		self.mdTramoP06.addSubMode(self.mdSituacionNNB_06)
		self.mdTramoP06.addSubMode(self.mdSituacionBBN_06)
		self.mdTramoP06.addSubMode(self.mdSituacionNBB_06)
		self.mdTramoP06.addSubMode(self.mdSituacionNBN_06)
		self.mdTramoP06.addSubMode(self.mdSituacionNBV_06)
		self.mdTramoP07.addSubMode(self.mdSituacionBNN_07)
		self.mdTramoP07.addSubMode(self.mdSituacionBBB_07)
		self.mdTramoP07.addSubMode(self.mdSituacionBNB_07)
		self.mdTramoP07.addSubMode(self.mdSituacionNNN_07)
		self.mdTramoP07.addSubMode(self.mdSituacionNNB_07)
		self.mdTramoP07.addSubMode(self.mdSituacionBBN_07)
		self.mdTramoP07.addSubMode(self.mdSituacionNBB_07)
		self.mdTramoP07.addSubMode(self.mdSituacionNBN_07)
		self.mdTramoP07.addSubMode(self.mdSituacionVBN_07)
		self.mdTramoP07.addSubMode(self.mdSituacionVVB_07)
		self.mdTramoP07.addSubMode(self.mdSituacionVVV_07)
		self.mdTramoP07.addSubMode(self.mdSituacionNBV_07)
		self.mdTramoP08.addSubMode(self.mdSituacionVBN_08)
		self.mdTramoP08.addSubMode(self.mdSituacionVVB_08)
		self.mdTramoP08.addSubMode(self.mdSituacionVVV_08)
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
		self.mdSituacionBNB_00.addSubMode(self.mdNuevoPasoSi)
		self.mdSituacionBNN_01.addSubMode(self.mdNuevoPasoSi)
		self.mdSituacionNNN_01.addSubMode(self.mdNuevoPasoSi)
		self.mdSituacionBNN_02.addSubMode(self.mdNuevoPasoSi)
		self.mdSituacionNNN_02.addSubMode(self.mdNuevoPasoSi)
		self.mdSituacionNNB_03.addSubMode(self.mdNuevoPasoSi)
		self.mdSituacionNNN_03.addSubMode(self.mdNuevoPasoSi)
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
		self.mdTramoP00.addSubMode(self.mdDecisionAparejoCerrado)
		self.mdTramoP01.addSubMode(self.mdDecisionAparejoCerrado)
		self.mdTramoP02.addSubMode(self.mdDecisionAparejoAbierto)
		self.mdTramoP03.addSubMode(self.mdDecisionAparejoAbierto)
		self.mdTramoP04.addSubMode(self.mdDecisionAparejoAbierto)
		self.mdTramoP05.addSubMode(self.mdDecisionAparejoAbierto)
		self.mdTramoP06.addSubMode(self.mdDecisionAparejoAbierto)
		self.mdTramoP07.addSubMode(self.mdDecisionAparejoAbierto)
		self.mdTramoP08.addSubMode(self.mdDecisionAparejoAbierto)

