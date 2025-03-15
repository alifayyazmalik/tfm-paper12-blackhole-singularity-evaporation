import numpy as np
from astropy import constants as const

def tfm_shadow_radius(M, lambda_param, beta):
    """
    Calculates TFM shadow radius (Eq. 3.2)
    """
    rs = 2 * const.G.value * M / const.c.value**2
    delta_r = lambda_param * beta**2 * rs
    return 2.6 * (rs + delta_r)  # 2.6 factor from photon orbit

# Example: M87* (6.5e9 solar masses)
M_m87 = 6.5e9 * const.M_sun.value
shadow_tfm = tfm_shadow_radius(M_m87, 1.2e-5, 14.8)
shadow_gr = 2.6 * 2 * const.G.value * M_m87 / const.c.value**2
print(f"TFM shadow: {shadow_tfm:.2e} m vs GR: {shadow_gr:.2e} m")
