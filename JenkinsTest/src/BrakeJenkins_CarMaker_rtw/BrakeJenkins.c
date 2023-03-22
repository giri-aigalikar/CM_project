/*
 * BrakeJenkins.c
 *
 * Sponsored Third Party Support License -- for use only to support
 * products interfaced to MathWorks software under terms specified in your
 * company's restricted use license agreement.
 *
 * Code generation for model "BrakeJenkins".
 *
 * Model version              : 1.18
 * Simulink Coder version : 9.4 (R2020b) 29-Jul-2020
 * C source code generated on : Wed Mar 22 13:12:37 2023
 *
 * Target selection: CarMaker.tlc
 * Note: GRT includes extra infrastructure and instrumentation for prototyping
 * Embedded hardware selection: Intel->x86-64 (Windows64)
 * Code generation objectives: Unspecified
 * Validation result: Not run
 */

#include <infoc.h>
#include <Log.h>
#include <InfoParam.h>
#include <DataDict.h>
#include <MatSupp.h>
#include "BrakeJenkins.h"
#include "BrakeJenkins_private.h"
#include "BrakeJenkins_wrap.h"

/* CarMaker: Compile- and link-time checks for the right Matlab version. */
#if MATSUPP_NUMVER == 90900

/* The following statement will cause an "unresolved symbol" error when
   linking with a MatSupp library built for the wrong Matlab version. */
extern int MATSUPP_VARNAME(MatSupp, MATSUPP_NUMVER);
void *MATSUPP_VARNAME(MODEL, MATSUPP_NUMVER) = &MATSUPP_VARNAME(MatSupp,
  MATSUPP_NUMVER);

#else
# error Compiler options unsuitable for C code created with Matlab 9.9
#endif

const cmBrakeOut BrakeJenkins_rtZcmBrakeOut = {
  {
    {
      0.0,                             /* Trq_WB */
      0.0,                             /* Trq_PB */
      0.0                              /* Trq_BrakeReg_trg */
    },                                 /* FL */

    {
      0.0,                             /* Trq_WB */
      0.0,                             /* Trq_PB */
      0.0                              /* Trq_BrakeReg_trg */
    },                                 /* FR */

    {
      0.0,                             /* Trq_WB */
      0.0,                             /* Trq_PB */
      0.0                              /* Trq_BrakeReg_trg */
    },                                 /* RL */

    {
      0.0,                             /* Trq_WB */
      0.0,                             /* Trq_PB */
      0.0                              /* Trq_BrakeReg_trg */
    }                                  /* RR */
  },                                   /* WheelOut */

  {
    0.0,                               /* d0 */
    0.0,                               /* d1 */
    0.0,                               /* d2 */
    0.0                                /* d3 */
  }                                    /* Trq_DriveSrc_trg */
} ;                                    /* cmBrakeOut ground */

/* Block parameters (default storage) */
P_BrakeJenkins_T BrakeJenkins_P = {
  /* Expression: 15
   * Referenced by: '<Root>/Gain'
   */
  15.0,

  /* Expression: 0
   * Referenced by: '<S1>/Trq_DriveSrc_trg.d0'
   */
  0.0,

  /* Expression: 0
   * Referenced by: '<S1>/Trq_DriveSrc_trg.d1'
   */
  0.0,

  /* Expression: 0
   * Referenced by: '<S1>/Trq_DriveSrc_trg.d2'
   */
  0.0,

  /* Expression: 0
   * Referenced by: '<S1>/Trq_DriveSrc_trg.d3'
   */
  0.0
};

/* Model step function */
void BrakeJenkins_step(RT_MODEL_BrakeJenkins_T *const BrakeJenkins_M)
{
  ExtU_BrakeJenkins_T *BrakeJenkins_U = (ExtU_BrakeJenkins_T *)
    BrakeJenkins_M->inputs;
  ExtY_BrakeJenkins_T *BrakeJenkins_Y = (ExtY_BrakeJenkins_T *)
    BrakeJenkins_M->outputs;

  /* Gain: '<Root>/Gain' incorporates:
   *  Inport: '<Root>/FromCM'
   */
  BrakeJenkins_Y->ToCM.WheelOut.FL.Trq_WB = BrakeJenkins_P.Gain_Gain *
    BrakeJenkins_U->FromCM.Pedal;

  /* BusCreator generated from: '<Root>/ToCM' incorporates:
   *  Inport: '<Root>/FromCM'
   */
  BrakeJenkins_Y->ToCM.WheelOut.FL.Trq_PB =
    BrakeJenkins_U->FromCM.WheelIn.FL.Trq_BrakeReg_max;
  BrakeJenkins_Y->ToCM.WheelOut.FL.Trq_BrakeReg_trg =
    BrakeJenkins_U->FromCM.WheelIn.FL.Trq_BrakeReg;

  /* BusCreator generated from: '<Root>/ToCM' incorporates:
   *  Inport: '<Root>/FromCM'
   */
  BrakeJenkins_Y->ToCM.WheelOut.FR.Trq_WB =
    BrakeJenkins_U->FromCM.WheelIn.FR.Trq_BrakeReg_max;
  BrakeJenkins_Y->ToCM.WheelOut.FR.Trq_PB =
    BrakeJenkins_U->FromCM.WheelIn.FR.Trq_BrakeReg;
  BrakeJenkins_Y->ToCM.WheelOut.FR.Trq_BrakeReg_trg = 0.0;

  /* BusCreator generated from: '<Root>/ToCM' incorporates:
   *  Inport: '<Root>/FromCM'
   */
  BrakeJenkins_Y->ToCM.WheelOut.RL.Trq_WB =
    BrakeJenkins_U->FromCM.WheelIn.RL.Trq_BrakeReg_max;
  BrakeJenkins_Y->ToCM.WheelOut.RL.Trq_PB =
    BrakeJenkins_U->FromCM.WheelIn.RL.Trq_BrakeReg;
  BrakeJenkins_Y->ToCM.WheelOut.RL.Trq_BrakeReg_trg =
    BrakeJenkins_U->FromCM.WheelIn.RR.Trq_BrakeReg_max;

  /* BusCreator generated from: '<Root>/ToCM' incorporates:
   *  Inport: '<Root>/FromCM'
   */
  BrakeJenkins_Y->ToCM.WheelOut.RR.Trq_WB =
    BrakeJenkins_U->FromCM.WheelIn.RR.Trq_BrakeReg;
  BrakeJenkins_Y->ToCM.WheelOut.RR.Trq_PB = BrakeJenkins_U->FromCM.Park;
  BrakeJenkins_Y->ToCM.WheelOut.RR.Trq_BrakeReg_trg =
    BrakeJenkins_U->FromCM.T_env;

  /* BusCreator generated from: '<Root>/ToCM' incorporates:
   *  Constant: '<S1>/Trq_DriveSrc_trg.d0'
   *  Constant: '<S1>/Trq_DriveSrc_trg.d1'
   *  Constant: '<S1>/Trq_DriveSrc_trg.d2'
   *  Constant: '<S1>/Trq_DriveSrc_trg.d3'
   */
  BrakeJenkins_Y->ToCM.Trq_DriveSrc_trg.d0 =
    BrakeJenkins_P.Trq_DriveSrc_trgd0_Value;
  BrakeJenkins_Y->ToCM.Trq_DriveSrc_trg.d1 =
    BrakeJenkins_P.Trq_DriveSrc_trgd1_Value;
  BrakeJenkins_Y->ToCM.Trq_DriveSrc_trg.d2 =
    BrakeJenkins_P.Trq_DriveSrc_trgd2_Value;
  BrakeJenkins_Y->ToCM.Trq_DriveSrc_trg.d3 =
    BrakeJenkins_P.Trq_DriveSrc_trgd3_Value;
}

/* Model initialize function */
void BrakeJenkins_initialize(RT_MODEL_BrakeJenkins_T *const BrakeJenkins_M)
{
  UNUSED_PARAMETER(BrakeJenkins_M);
}

/* Model terminate function */
void BrakeJenkins_terminate(RT_MODEL_BrakeJenkins_T * BrakeJenkins_M)
{
  /* model code */
  rt_FREE(BrakeJenkins_M->inputs);
  rt_FREE(BrakeJenkins_M->outputs);
  rt_FREE(BrakeJenkins_M);
}

/* Model data allocation function */
RT_MODEL_BrakeJenkins_T *BrakeJenkins(struct tInfos *inf)
{
  RT_MODEL_BrakeJenkins_T *BrakeJenkins_M;
  BrakeJenkins_M = (RT_MODEL_BrakeJenkins_T *) malloc(sizeof
    (RT_MODEL_BrakeJenkins_T));
  if (BrakeJenkins_M == NULL) {
    return NULL;
  }

  (void) memset((char *)BrakeJenkins_M, 0,
                sizeof(RT_MODEL_BrakeJenkins_T));
  MatSupp_Init();

  /* external inputs */
  {
    ExtU_BrakeJenkins_T *BrakeJenkins_U = (ExtU_BrakeJenkins_T *) malloc(sizeof
      (ExtU_BrakeJenkins_T));
    rt_VALIDATE_MEMORY(BrakeJenkins_M,BrakeJenkins_U);
    BrakeJenkins_M->inputs = (((ExtU_BrakeJenkins_T *) BrakeJenkins_U));
  }

  /* external outputs */
  {
    ExtY_BrakeJenkins_T *BrakeJenkins_Y = (ExtY_BrakeJenkins_T *) malloc(sizeof
      (ExtY_BrakeJenkins_T));
    rt_VALIDATE_MEMORY(BrakeJenkins_M,BrakeJenkins_Y);
    BrakeJenkins_M->outputs = (BrakeJenkins_Y);
  }

  /* CarMaker parameter tuning */
  {
    BrakeJenkins_SetParams(BrakeJenkins_M, NULL, inf);
  }

  {
    ExtU_BrakeJenkins_T *BrakeJenkins_U = (ExtU_BrakeJenkins_T *)
      BrakeJenkins_M->inputs;
    ExtY_BrakeJenkins_T *BrakeJenkins_Y = (ExtY_BrakeJenkins_T *)
      BrakeJenkins_M->outputs;

    /* external inputs */
    (void)memset(BrakeJenkins_U, 0, sizeof(ExtU_BrakeJenkins_T));

    /* external outputs */
    BrakeJenkins_Y->ToCM = BrakeJenkins_rtZcmBrakeOut;
  }

  return BrakeJenkins_M;
}

/* CarMaker dictionary definitions. */
extern tQuantEntry *BrakeJenkins_main_DictDefines[];
static tQuantEntry DictDefines[] = {
  { (void*)0x01234567, (void*)0x89ABCDEF, NULL, 0, 0, 0, "", 0.0, 0.0 },

  { (void*)BrakeJenkins_main_DictDefines, NULL, NULL, 0, 0, 0, "", 0.0, 0.0 },

  { NULL, NULL, NULL, 0, 0, 0, "", 0.0, 0.0 }
};

tQuantEntry *BrakeJenkins_DictDefines = DictDefines;
tQuantEntry *BrakeJenkins_main_DictDefines[] = {
  DictDefines,
  NULL
};

/* CarMaker bodyframe definitions. */
#ifndef RTMAKER

extern tMdlBdyFrame *BrakeJenkins_main_BdyFrameDefines[];
static tMdlBdyFrame BdyFrameDefines[] = {
  { (void*)0x01234567 },

  { (void*)0x89ABCDEF },

  { (void*)BrakeJenkins_main_BdyFrameDefines },

  { NULL }
};

tMdlBdyFrame *BrakeJenkins_BdyFrameDefines = BdyFrameDefines;
tMdlBdyFrame *BrakeJenkins_main_BdyFrameDefines[] = {
  BdyFrameDefines,
  NULL
};

#endif
