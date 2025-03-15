#include "cctk.h"
#include "GRHydro_TFM.h"

// TFM wave-lump density profile (Eq. 2)
void TFM_Density(CCTK_REAL *rho, CCTK_REAL r, CCTK_REAL lambda, CCTK_REAL beta) {
    CCTK_REAL l_planck = 1.616255e-35; // meters
    *rho = 1.0 / (pow(r,2) + pow(l_planck,2)) * lambda * pow(beta,2);
}

// Modified Schwarzschild metric (Eq. 2)
void TFM_Metric(CCTK_REAL *gtt, CCTK_REAL *grr, CCTK_REAL r, CCTK_REAL M) {
    CCTK_REAL rs = 2 * GRAVITY_CONSTANT * M / (SPEED_OF_LIGHT * SPEED_OF_LIGHT);
    CCTK_REAL cutoff = exp(-pow(r,2)/pow(l_planck,2));
    *gtt = -(1 - rs/r * cutoff);
    *grr = 1 / (1 - rs/r * cutoff);
}
