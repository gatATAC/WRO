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

	// --------- prSys Mision -----------------
	/**
	* Enum MisionMode
	* @description Enum [Mode]
	* @maximum     MisionMode_Engineering
	* @minimum     MisionMode_UNKNOWN
	* @values      MisionMode_UNKNOWN,MisionMode_Normal,MisionMode_Engineering
	*/
	enum class enum_MisionMode {MisionMode_UNKNOWN,MisionMode_Normal,MisionMode_Engineering};
	enum_MisionMode enumMisionMode;

	// --------- prSys Tramo -----------------
	/**
	* Enum TramoMode
	* @description Enum [Mode]
	* @maximum     TramoMode_Engineering
	* @minimum     TramoMode_UNKNOWN
	* @values      TramoMode_UNKNOWN,TramoMode_P00_SituarBNB_finBNB_Avanzar,TramoMode_P01_SeguirBNB_finder_giroder_abrir,TramoMode_P02_SeguirBNB_finder_giroder,TramoMode_P03_SeguirBNB_finizq_giroizq,TramoMode_P04_SeguirBNB_fincruce_rect,TramoMode_P05_SeguirNNB_finBNB_rect,TramoMode_P06_SeguirBNB_finizq_giroder,TramoMode_P07_SituarVVB_finVVB_Avanzar,TramoMode_P08_SeguirVVB_finVVV_giroder,TramoMode_Engineering
	*/
	enum class enum_TramoMode {TramoMode_UNKNOWN,TramoMode_P00_SituarBNB_finBNB_Avanzar,TramoMode_P01_SeguirBNB_finder_giroder_abrir,TramoMode_P02_SeguirBNB_finder_giroder,TramoMode_P03_SeguirBNB_finizq_giroizq,TramoMode_P04_SeguirBNB_fincruce_rect,TramoMode_P05_SeguirNNB_finBNB_rect,TramoMode_P06_SeguirBNB_finizq_giroder,TramoMode_P07_SituarVVB_finVVB_Avanzar,TramoMode_P08_SeguirVVB_finVVV_giroder,TramoMode_Engineering};
	enum_TramoMode enumTramoMode;

	// --------- prSys Situacion -----------------
	/**
	* Enum SituacionMode
	* @description Enum [Mode]
	* @maximum     SituacionMode_Engineering
	* @minimum     SituacionMode_UNKNOWN
	* @values      SituacionMode_UNKNOWN,SituacionMode_BNN_00,SituacionMode_NBB_00,SituacionMode_BBB_00,SituacionMode_NNB_00,SituacionMode_BNB_00,SituacionMode_NBN_00,SituacionMode_BBN_00,SituacionMode_NNN_00,SituacionMode_NBV_01,SituacionMode_BNB_01,SituacionMode_BBB_01,SituacionMode_BNN_01,SituacionMode_NBB_01,SituacionMode_NNB_01,SituacionMode_VBN_01,SituacionMode_BBN_01,SituacionMode_NNN_01,SituacionMode_NBN_01,SituacionMode_BBB_02,SituacionMode_BBN_02,SituacionMode_BNB_02,SituacionMode_BNN_02,SituacionMode_NBB_02,SituacionMode_NBN_02,SituacionMode_NBV_02,SituacionMode_NNB_02,SituacionMode_NNN_02,SituacionMode_VBN_02,SituacionMode_BBB_03,SituacionMode_BBN_03,SituacionMode_BNB_03,SituacionMode_BNN_03,SituacionMode_NBB_03,SituacionMode_NBN_03,SituacionMode_NBV_03,SituacionMode_NNB_03,SituacionMode_NNN_03,SituacionMode_VBN_03,SituacionMode_BBB_04,SituacionMode_BBN_04,SituacionMode_BNB_04,SituacionMode_BNN_04,SituacionMode_NBB_04,SituacionMode_NBN_04,SituacionMode_NBV_04,SituacionMode_NNB_04,SituacionMode_NNN_04,SituacionMode_VBN_04,SituacionMode_BBB_05,SituacionMode_BBN_05,SituacionMode_BNB_05,SituacionMode_BNN_05,SituacionMode_NBB_05,SituacionMode_NBN_05,SituacionMode_NNB_05,SituacionMode_NNN_05,SituacionMode_VBN_06,SituacionMode_NBB_06,SituacionMode_BNB_06,SituacionMode_NBN_06,SituacionMode_NNN_06,SituacionMode_BNN_06,SituacionMode_BBN_06,SituacionMode_BBB_06,SituacionMode_NBV_06,SituacionMode_NNB_06,SituacionMode_BBB_07,SituacionMode_BBN_07,SituacionMode_BNB_07,SituacionMode_BNN_07,SituacionMode_NBB_07,SituacionMode_NBN_07,SituacionMode_NBV_07,SituacionMode_NNB_07,SituacionMode_NNN_07,SituacionMode_VBN_07,SituacionMode_VVB_07,SituacionMode_VVV_07,SituacionMode_VVV_08,SituacionMode_VBN_08,SituacionMode_VVB_08,SituacionMode_Engineering
	*/
	enum class enum_SituacionMode {SituacionMode_UNKNOWN,SituacionMode_BNN_00,SituacionMode_NBB_00,SituacionMode_BBB_00,SituacionMode_NNB_00,SituacionMode_BNB_00,SituacionMode_NBN_00,SituacionMode_BBN_00,SituacionMode_NNN_00,SituacionMode_NBV_01,SituacionMode_BNB_01,SituacionMode_BBB_01,SituacionMode_BNN_01,SituacionMode_NBB_01,SituacionMode_NNB_01,SituacionMode_VBN_01,SituacionMode_BBN_01,SituacionMode_NNN_01,SituacionMode_NBN_01,SituacionMode_BBB_02,SituacionMode_BBN_02,SituacionMode_BNB_02,SituacionMode_BNN_02,SituacionMode_NBB_02,SituacionMode_NBN_02,SituacionMode_NBV_02,SituacionMode_NNB_02,SituacionMode_NNN_02,SituacionMode_VBN_02,SituacionMode_BBB_03,SituacionMode_BBN_03,SituacionMode_BNB_03,SituacionMode_BNN_03,SituacionMode_NBB_03,SituacionMode_NBN_03,SituacionMode_NBV_03,SituacionMode_NNB_03,SituacionMode_NNN_03,SituacionMode_VBN_03,SituacionMode_BBB_04,SituacionMode_BBN_04,SituacionMode_BNB_04,SituacionMode_BNN_04,SituacionMode_NBB_04,SituacionMode_NBN_04,SituacionMode_NBV_04,SituacionMode_NNB_04,SituacionMode_NNN_04,SituacionMode_VBN_04,SituacionMode_BBB_05,SituacionMode_BBN_05,SituacionMode_BNB_05,SituacionMode_BNN_05,SituacionMode_NBB_05,SituacionMode_NBN_05,SituacionMode_NNB_05,SituacionMode_NNN_05,SituacionMode_VBN_06,SituacionMode_NBB_06,SituacionMode_BNB_06,SituacionMode_NBN_06,SituacionMode_NNN_06,SituacionMode_BNN_06,SituacionMode_BBN_06,SituacionMode_BBB_06,SituacionMode_NBV_06,SituacionMode_NNB_06,SituacionMode_BBB_07,SituacionMode_BBN_07,SituacionMode_BNB_07,SituacionMode_BNN_07,SituacionMode_NBB_07,SituacionMode_NBN_07,SituacionMode_NBV_07,SituacionMode_NNB_07,SituacionMode_NNN_07,SituacionMode_VBN_07,SituacionMode_VVB_07,SituacionMode_VVV_07,SituacionMode_VVV_08,SituacionMode_VBN_08,SituacionMode_VVB_08,SituacionMode_Engineering};
	enum_SituacionMode enumSituacionMode;

	// --------- prSys DecisionMovimiento -----------------
	/**
	* Enum DecisionMovimientoMode
	* @description Enum [Mode]
	* @maximum     DecisionMovimientoMode_Engineering
	* @minimum     DecisionMovimientoMode_UNKNOWN
	* @values      DecisionMovimientoMode_UNKNOWN,DecisionMovimientoMode_Avanzar,DecisionMovimientoMode_CompasIzq,DecisionMovimientoMode_CompasDer,DecisionMovimientoMode_GirarDer,DecisionMovimientoMode_GirarIzq,DecisionMovimientoMode_Parar,DecisionMovimientoMode_Engineering
	*/
	enum class enum_DecisionMovimientoMode {DecisionMovimientoMode_UNKNOWN,DecisionMovimientoMode_Avanzar,DecisionMovimientoMode_CompasIzq,DecisionMovimientoMode_CompasDer,DecisionMovimientoMode_GirarDer,DecisionMovimientoMode_GirarIzq,DecisionMovimientoMode_Parar,DecisionMovimientoMode_Engineering};
	enum_DecisionMovimientoMode enumDecisionMovimientoMode;

	// --------- prParam RuedaDer -----------------
	/**
	* Enum RuedaDer
	* @description Enum 
	* @maximum     RuedaDer_Atras
	* @minimum     RuedaDer_UNKNOWN
	* @values      RuedaDer_UNKNOWN,RuedaDer_Quieta,RuedaDer_Adelante,RuedaDer_Atras
	*/
	enum class enum_RuedaDer {RuedaDer_UNKNOWN,RuedaDer_Quieta,RuedaDer_Adelante,RuedaDer_Atras};
	enum_RuedaDer enumRuedaDer;

	/**
	* Enum RuedaDerMode
	* @description Enum [Mode]
	* @maximum     RuedaDerMode_Retroceder
	* @minimum     RuedaDerMode_UNKNOWN
	* @values      RuedaDerMode_UNKNOWN,RuedaDerMode_Parada,RuedaDerMode_Avanzar,RuedaDerMode_Retroceder
	*/
	enum class enum_RuedaDerMode {RuedaDerMode_UNKNOWN,RuedaDerMode_Parada,RuedaDerMode_Avanzar,RuedaDerMode_Retroceder};
	enum_RuedaDerMode enumRuedaDerMode;

	// --------- prParam RuedaIzq -----------------
	/**
	* Enum RuedaIzq
	* @description Enum 
	* @maximum     RuedaIzq_Atras
	* @minimum     RuedaIzq_UNKNOWN
	* @values      RuedaIzq_UNKNOWN,RuedaIzq_Quieta,RuedaIzq_Adelante,RuedaIzq_Atras
	*/
	enum class enum_RuedaIzq {RuedaIzq_UNKNOWN,RuedaIzq_Quieta,RuedaIzq_Adelante,RuedaIzq_Atras};
	enum_RuedaIzq enumRuedaIzq;

	/**
	* Enum RuedaIzqMode
	* @description Enum [Mode]
	* @maximum     RuedaIzqMode_Retroceder
	* @minimum     RuedaIzqMode_UNKNOWN
	* @values      RuedaIzqMode_UNKNOWN,RuedaIzqMode_Parada,RuedaIzqMode_Avanzar,RuedaIzqMode_Retroceder
	*/
	enum class enum_RuedaIzqMode {RuedaIzqMode_UNKNOWN,RuedaIzqMode_Parada,RuedaIzqMode_Avanzar,RuedaIzqMode_Retroceder};
	enum_RuedaIzqMode enumRuedaIzqMode;

	// --------- prSys NuevoPaso -----------------
	/**
	* Enum NuevoPasoMode
	* @description Enum [Mode]
	* @maximum     NuevoPasoMode_Si
	* @minimum     NuevoPasoMode_UNKNOWN
	* @values      NuevoPasoMode_UNKNOWN,NuevoPasoMode_Si
	*/
	enum class enum_NuevoPasoMode {NuevoPasoMode_UNKNOWN,NuevoPasoMode_Si};
	enum_NuevoPasoMode enumNuevoPasoMode;

	// --------- prSys DecisionSeguidor -----------------
	/**
	* Enum DecisionSeguidorMode
	* @description Enum [Mode]
	* @maximum     DecisionSeguidorMode_VVB
	* @minimum     DecisionSeguidorMode_UNKNOWN
	* @values      DecisionSeguidorMode_UNKNOWN,DecisionSeguidorMode_BNB,DecisionSeguidorMode_VVB
	*/
	enum class enum_DecisionSeguidorMode {DecisionSeguidorMode_UNKNOWN,DecisionSeguidorMode_BNB,DecisionSeguidorMode_VVB};
	enum_DecisionSeguidorMode enumDecisionSeguidorMode;

	// --------- prSys DecisionAparejo -----------------
	/**
	* Enum DecisionAparejoMode
	* @description Enum [Mode]
	* @maximum     DecisionAparejoMode_Cerrado
	* @minimum     DecisionAparejoMode_UNKNOWN
	* @values      DecisionAparejoMode_UNKNOWN,DecisionAparejoMode_Abierto,DecisionAparejoMode_Medio,DecisionAparejoMode_Cerrado
	*/
	enum class enum_DecisionAparejoMode {DecisionAparejoMode_UNKNOWN,DecisionAparejoMode_Abierto,DecisionAparejoMode_Medio,DecisionAparejoMode_Cerrado};
	enum_DecisionAparejoMode enumDecisionAparejoMode;


	//----------------------------------------------------------------------
	//  Specific methods
	//----------------------------------------------------------------------

	public:

	/* MisionMode */
	enum_MisionMode get_MisionMode(void);
	enum_MisionMode set_MisionMode(enum_MisionMode value);

	/* TramoMode */
	enum_TramoMode get_TramoMode(void);
	enum_TramoMode set_TramoMode(enum_TramoMode value);

	/* SituacionMode */
	enum_SituacionMode get_SituacionMode(void);
	enum_SituacionMode set_SituacionMode(enum_SituacionMode value);

	/* DecisionMovimientoMode */
	enum_DecisionMovimientoMode get_DecisionMovimientoMode(void);
	enum_DecisionMovimientoMode set_DecisionMovimientoMode(enum_DecisionMovimientoMode value);

	// --------- prParam RuedaDer -----------------
	/* RuedaDer */
	enum_RuedaDer get_RuedaDer(void);
	enum_RuedaDer set_RuedaDer(enum_RuedaDer value);
	/* RuedaDerMode */
	enum_RuedaDerMode get_RuedaDerMode(void);
	enum_RuedaDerMode set_RuedaDerMode(enum_RuedaDerMode value);

	// --------- prParam RuedaIzq -----------------
	/* RuedaIzq */
	enum_RuedaIzq get_RuedaIzq(void);
	enum_RuedaIzq set_RuedaIzq(enum_RuedaIzq value);
	/* RuedaIzqMode */
	enum_RuedaIzqMode get_RuedaIzqMode(void);
	enum_RuedaIzqMode set_RuedaIzqMode(enum_RuedaIzqMode value);

	/* NuevoPasoMode */
	enum_NuevoPasoMode get_NuevoPasoMode(void);
	enum_NuevoPasoMode set_NuevoPasoMode(enum_NuevoPasoMode value);

	/* DecisionSeguidorMode */
	enum_DecisionSeguidorMode get_DecisionSeguidorMode(void);
	enum_DecisionSeguidorMode set_DecisionSeguidorMode(enum_DecisionSeguidorMode value);

	/* DecisionAparejoMode */
	enum_DecisionAparejoMode get_DecisionAparejoMode(void);
	enum_DecisionAparejoMode set_DecisionAparejoMode(enum_DecisionAparejoMode value);


}

