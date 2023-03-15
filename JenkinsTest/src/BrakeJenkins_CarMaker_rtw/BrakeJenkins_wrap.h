/***************************************************** target specific file ***/
/*  Wrapper module for Simulink models                                        */
/*  ------------------------------------------------------------------------  */
/*  (c) IPG Automotive GmbH    www.ipg-automotive.com   Fon: +49.721.98520-0  */
/*  Bannwaldallee 60      D-76185 Karlsruhe   Germany   Fax: +49.721.98520-99 */
/******************************************************************************/
#ifndef __BRAKEJENKINS_WRAP_H__
#define __BRAKEJENKINS_WRAP_H__
#ifndef IS_CAR
# define IS_CAR
#endif

#ifdef __cplusplus

extern "C" {

#endif

  struct tInfos;
  struct tMdlBdyFrame;
  struct tMatSuppDictDef;
  struct tMatSuppTunables;

#ifdef CLASSIC_INTERFACE
# define rtModel_BrakeJenkins          RT_MODEL_BrakeJenkins_T
#else
# define rtModel_BrakeJenkins          tag_RTM_BrakeJenkins_T
#endif                                 //CLASSIC_INTERFACE

#define ExternalInputs_BrakeJenkins    ExtU_BrakeJenkins_T
#define ExternalOutputs_BrakeJenkins   ExtY_BrakeJenkins_T
#ifndef BrakeJenkins_rtModel

  typedef struct rtModel_BrakeJenkins rtModel_BrakeJenkins;

#endif

  /* Model registration function */
  rtModel_BrakeJenkins *BrakeJenkins (struct tInfos *Inf);

#if defined(CLASSIC_INTERFACE) && !defined(CM4SLDS)

  void rt_ODECreateIntegrationData (RTWSolverInfo *si);
  void rt_ODEUpdateContinuousStates(RTWSolverInfo *si);
  void rt_ODEDestroyIntegrationData(RTWSolverInfo *si);

#endif

  /* Dictionary variables and other items of the model */
  extern struct tMatSuppDictDef *BrakeJenkins_DictDefines;
  extern struct tMdlBdyFrame *BrakeJenkins_BdyFrameDefines;

  /* Wrapper functions */
  void BrakeJenkins_SetParams (rtModel_BrakeJenkins *rtm,
      struct tMatSuppTunables *tuns,
      struct tInfos *Inf);
  int BrakeJenkins_Register (void);

#ifdef __cplusplus

}
#endif
#endif                                 /* __BRAKEJENKINS_WRAP_H__ */
