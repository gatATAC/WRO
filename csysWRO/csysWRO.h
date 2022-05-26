// Created with PORIS @ which is Copyright (c) 2022 cosmoBots.eu
// Do ethically correct things. Do not use our tools to do evil stuff
// Think about enriching all humanity, besides yourself

#include "PORIS.h"

class csysWRO {
	private:

//Including fragment for PORIS support
#include "_csysWROPORIS.h"

	//----------------------------------------------------------------------
	//  Device Magnitudes
	//----------------------------------------------------------------------

	// --------- prSys Misión -----------------
	/**
	* Enum MisiónMode
	* @description Enum [Mode]
	* @maximum     MisiónNormal
	* @minimum     MisiónUNKNOWN
	* @values      MisiónUNKNOWN,MisiónNormal
	*/
	enum class enum_MisiónMode {MisiónUNKNOWN,MisiónNormal}
	enum_MisiónMode enumMisiónMode

	// --------- prSys Tramo -----------------
	/**
	* Enum TramoMode
	* @description Enum [Mode]
	* @maximum     TramoP08_SeguirVVB_finVVV_giroder
	* @minimum     TramoUNKNOWN
	* @values      TramoUNKNOWN,TramoP00_SituarBNB_finBNB_Avanzar,TramoP01_SeguirBNB_finder_giroder_abrir,TramoP02_SeguirBNB_finder_giroder,TramoP03_SeguirBNB_finizq_giroizq,TramoP04_SeguirBNB_fincruce_rect,TramoP05_SeguirNNB_finBNB_rect,TramoP06_SeguirBNB_finizq_giroder,TramoP07_SituarVVB_finVVB_Avanzar,TramoP08_SeguirVVB_finVVV_giroder
	*/
	enum class enum_TramoMode {TramoUNKNOWN,TramoP00_SituarBNB_finBNB_Avanzar,TramoP01_SeguirBNB_finder_giroder_abrir,TramoP02_SeguirBNB_finder_giroder,TramoP03_SeguirBNB_finizq_giroizq,TramoP04_SeguirBNB_fincruce_rect,TramoP05_SeguirNNB_finBNB_rect,TramoP06_SeguirBNB_finizq_giroder,TramoP07_SituarVVB_finVVB_Avanzar,TramoP08_SeguirVVB_finVVV_giroder}
	enum_TramoMode enumTramoMode

	// --------- prSys Situacion -----------------
	/**
	* Enum SituacionMode
	* @description Enum [Mode]
	* @maximum     SituacionVVB_08
	* @minimum     SituacionUNKNOWN
	* @values      SituacionUNKNOWN,SituacionBNN_00,SituacionNBB_00,SituacionBBB_00,SituacionNNB_00,SituacionBNB_00,SituacionNBN_00,SituacionBBN_00,SituacionNNN_00,SituacionNBV_01,SituacionBNB_01,SituacionBBB_01,SituacionBNN_01,SituacionNBB_01,SituacionNNB_01,SituacionVBN_01,SituacionBBN_01,SituacionNNN_01,SituacionNBN_01,SituacionBBB_02,SituacionBBN_02,SituacionBNB_02,SituacionBNN_02,SituacionNBB_02,SituacionNBN_02,SituacionNBV_02,SituacionNNB_02,SituacionNNN_02,SituacionVBN_02,SituacionBBB_03,SituacionBBN_03,SituacionBNB_03,SituacionBNN_03,SituacionNBB_03,SituacionNBN_03,SituacionNBV_03,SituacionNNB_03,SituacionNNN_03,SituacionVBN_03,SituacionBBB_04,SituacionBBN_04,SituacionBNB_04,SituacionBNN_04,SituacionNBB_04,SituacionNBN_04,SituacionNBV_04,SituacionNNB_04,SituacionNNN_04,SituacionVBN_04,SituacionBBB_05,SituacionBBN_05,SituacionBNB_05,SituacionBNN_05,SituacionNBB_05,SituacionNBN_05,SituacionNNB_05,SituacionNNN_05,SituacionVBN_06,SituacionNBB_06,SituacionBNB_06,SituacionNBN_06,SituacionNNN_06,SituacionBNN_06,SituacionBBN_06,SituacionBBB_06,SituacionNBV_06,SituacionNNB_06,SituacionBBB_07,SituacionBBN_07,SituacionBNB_07,SituacionBNN_07,SituacionNBB_07,SituacionNBN_07,SituacionNBV_07,SituacionNNB_07,SituacionNNN_07,SituacionVBN_07,SituacionVVB_07,SituacionVVV_07,SituacionVVV_08,SituacionVBN_08,SituacionVVB_08
	*/
	enum class enum_SituacionMode {SituacionUNKNOWN,SituacionBNN_00,SituacionNBB_00,SituacionBBB_00,SituacionNNB_00,SituacionBNB_00,SituacionNBN_00,SituacionBBN_00,SituacionNNN_00,SituacionNBV_01,SituacionBNB_01,SituacionBBB_01,SituacionBNN_01,SituacionNBB_01,SituacionNNB_01,SituacionVBN_01,SituacionBBN_01,SituacionNNN_01,SituacionNBN_01,SituacionBBB_02,SituacionBBN_02,SituacionBNB_02,SituacionBNN_02,SituacionNBB_02,SituacionNBN_02,SituacionNBV_02,SituacionNNB_02,SituacionNNN_02,SituacionVBN_02,SituacionBBB_03,SituacionBBN_03,SituacionBNB_03,SituacionBNN_03,SituacionNBB_03,SituacionNBN_03,SituacionNBV_03,SituacionNNB_03,SituacionNNN_03,SituacionVBN_03,SituacionBBB_04,SituacionBBN_04,SituacionBNB_04,SituacionBNN_04,SituacionNBB_04,SituacionNBN_04,SituacionNBV_04,SituacionNNB_04,SituacionNNN_04,SituacionVBN_04,SituacionBBB_05,SituacionBBN_05,SituacionBNB_05,SituacionBNN_05,SituacionNBB_05,SituacionNBN_05,SituacionNNB_05,SituacionNNN_05,SituacionVBN_06,SituacionNBB_06,SituacionBNB_06,SituacionNBN_06,SituacionNNN_06,SituacionBNN_06,SituacionBBN_06,SituacionBBB_06,SituacionNBV_06,SituacionNNB_06,SituacionBBB_07,SituacionBBN_07,SituacionBNB_07,SituacionBNN_07,SituacionNBB_07,SituacionNBN_07,SituacionNBV_07,SituacionNNB_07,SituacionNNN_07,SituacionVBN_07,SituacionVVB_07,SituacionVVV_07,SituacionVVV_08,SituacionVBN_08,SituacionVVB_08}
	enum_SituacionMode enumSituacionMode

	// --------- prSys DecisionMovimiento -----------------
	/**
	* Enum DecisionMovimientoMode
	* @description Enum [Mode]
	* @maximum     DecisionMovimientoParar
	* @minimum     DecisionMovimientoUNKNOWN
	* @values      DecisionMovimientoUNKNOWN,DecisionMovimientoAvanzar,DecisionMovimientoCompasIzq,DecisionMovimientoCompasDer,DecisionMovimientoGirarDer,DecisionMovimientoGirarIzq,DecisionMovimientoParar
	*/
	enum class enum_DecisionMovimientoMode {DecisionMovimientoUNKNOWN,DecisionMovimientoAvanzar,DecisionMovimientoCompasIzq,DecisionMovimientoCompasDer,DecisionMovimientoGirarDer,DecisionMovimientoGirarIzq,DecisionMovimientoParar}
	enum_DecisionMovimientoMode enumDecisionMovimientoMode

	// --------- prParam RuedaDer -----------------
	/**
	* Enum RuedaDer
	* @description Enum 
	* @maximum     RuedaDer_Atrás
	* @minimum     RuedaDer_UNKNOWN
	* @values      RuedaDer_UNKNOWN,RuedaDer_Quieta,RuedaDer_Adelante,RuedaDer_Atrás
	*/
	enum class enum_RuedaDer {RuedaDer_UNKNOWN,RuedaDer_Quieta,RuedaDer_Adelante,RuedaDer_Atrás}
	enum_RuedaDer enumRuedaDer

	/**
	* Enum RuedaDerMode
	* @description Enum [Mode]
	* @maximum     RuedaDerRetroceder
	* @minimum     RuedaDerUNKNOWN
	* @values      RuedaDerUNKNOWN,RuedaDerParada,RuedaDerAvanzar,RuedaDerRetroceder
	*/
	enum class enum_RuedaDerMode {RuedaDerUNKNOWN,RuedaDerParada,RuedaDerAvanzar,RuedaDerRetroceder}
	enum_RuedaDerMode enumRuedaDerMode

	// --------- prParam RuedaIzq -----------------
	/**
	* Enum RuedaIzq
	* @description Enum 
	* @maximum     RuedaIzq_Atrás
	* @minimum     RuedaIzq_UNKNOWN
	* @values      RuedaIzq_UNKNOWN,RuedaIzq_Quieta,RuedaIzq_Adelante,RuedaIzq_Atrás
	*/
	enum class enum_RuedaIzq {RuedaIzq_UNKNOWN,RuedaIzq_Quieta,RuedaIzq_Adelante,RuedaIzq_Atrás}
	enum_RuedaIzq enumRuedaIzq

	/**
	* Enum RuedaIzqMode
	* @description Enum [Mode]
	* @maximum     RuedaIzqRetroceder
	* @minimum     RuedaIzqUNKNOWN
	* @values      RuedaIzqUNKNOWN,RuedaIzqParada,RuedaIzqAvanzar,RuedaIzqRetroceder
	*/
	enum class enum_RuedaIzqMode {RuedaIzqUNKNOWN,RuedaIzqParada,RuedaIzqAvanzar,RuedaIzqRetroceder}
	enum_RuedaIzqMode enumRuedaIzqMode

	// --------- prSys NuevoPaso -----------------
	/**
	* Enum NuevoPasoMode
	* @description Enum [Mode]
	* @maximum     NuevoPasoSí
	* @minimum     NuevoPasoUNKNOWN
	* @values      NuevoPasoUNKNOWN,NuevoPasoNo,NuevoPasoSí
	*/
	enum class enum_NuevoPasoMode {NuevoPasoUNKNOWN,NuevoPasoNo,NuevoPasoSí}
	enum_NuevoPasoMode enumNuevoPasoMode

	// --------- prSys DecisionSeguidor -----------------
	/**
	* Enum DecisionSeguidorMode
	* @description Enum [Mode]
	* @maximum     DecisionSeguidorVVB
	* @minimum     DecisionSeguidorUNKNOWN
	* @values      DecisionSeguidorUNKNOWN,DecisionSeguidorBNB,DecisionSeguidorVVB
	*/
	enum class enum_DecisionSeguidorMode {DecisionSeguidorUNKNOWN,DecisionSeguidorBNB,DecisionSeguidorVVB}
	enum_DecisionSeguidorMode enumDecisionSeguidorMode

	// --------- prSys DecisionAparejo -----------------
	/**
	* Enum DecisionAparejoMode
	* @description Enum [Mode]
	* @maximum     DecisionAparejoCerrado
	* @minimum     DecisionAparejoUNKNOWN
	* @values      DecisionAparejoUNKNOWN,DecisionAparejoAbierto,DecisionAparejoMedio,DecisionAparejoCerrado
	*/
	enum class enum_DecisionAparejoMode {DecisionAparejoUNKNOWN,DecisionAparejoAbierto,DecisionAparejoMedio,DecisionAparejoCerrado}
	enum_DecisionAparejoMode enumDecisionAparejoMode


	//----------------------------------------------------------------------
	//  Specific methods
	//----------------------------------------------------------------------

	public:

	/* MisiónMode */
	enum_MisiónMode get_MisiónMode(void)
	enum_MisiónMode set_MisiónMode(enum_MisiónMode value)

	/* TramoMode */
	enum_TramoMode get_TramoMode(void)
	enum_TramoMode set_TramoMode(enum_TramoMode value)

	/* SituacionMode */
	enum_SituacionMode get_SituacionMode(void)
	enum_SituacionMode set_SituacionMode(enum_SituacionMode value)

	/* DecisionMovimientoMode */
	enum_DecisionMovimientoMode get_DecisionMovimientoMode(void)
	enum_DecisionMovimientoMode set_DecisionMovimientoMode(enum_DecisionMovimientoMode value)

	// --------- prParam RuedaDer -----------------
	/* RuedaDer */
	enum_RuedaDer get_RuedaDer(void)
	enum_RuedaDer set_RuedaDer(enum_RuedaDer value)
	/* RuedaDerMode */
	enum_RuedaDerMode get_RuedaDerMode(void)
	enum_RuedaDerMode set_RuedaDerMode(enum_RuedaDerMode value)

	// --------- prParam RuedaIzq -----------------
	/* RuedaIzq */
	enum_RuedaIzq get_RuedaIzq(void)
	enum_RuedaIzq set_RuedaIzq(enum_RuedaIzq value)
	/* RuedaIzqMode */
	enum_RuedaIzqMode get_RuedaIzqMode(void)
	enum_RuedaIzqMode set_RuedaIzqMode(enum_RuedaIzqMode value)

	/* NuevoPasoMode */
	enum_NuevoPasoMode get_NuevoPasoMode(void)
	enum_NuevoPasoMode set_NuevoPasoMode(enum_NuevoPasoMode value)

	/* DecisionSeguidorMode */
	enum_DecisionSeguidorMode get_DecisionSeguidorMode(void)
	enum_DecisionSeguidorMode set_DecisionSeguidorMode(enum_DecisionSeguidorMode value)

	/* DecisionAparejoMode */
	enum_DecisionAparejoMode get_DecisionAparejoMode(void)
	enum_DecisionAparejoMode set_DecisionAparejoMode(enum_DecisionAparejoMode value)


}

