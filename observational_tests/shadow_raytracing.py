import numpy as np
import matplotlib.pyplot as plt
from astropy import constants as const

def tfm_shadow_radius(M, lambda_param, beta):
    """
    Calculates TFM shadow radius (Eq. 3.2)
    """
    rs = 2 * const.G.value * M / const.c.value**2
    delta_r = lambda_param * (beta * 3.086e19)**2 * rs  # beta in kpc → meters
    return 2.6 * (rs + delta_r)

def plot_shadow_image(radius, save_path="shadow_image.png"):
    """
    Generates a mock shadow image using Gaussian blur
    """
    x, y = np.mgrid[-2:2:100j, -2:2:100j]
    intensity = np.exp(-(x**2 + y**2)/(0.5*radius)**2)
    plt.imshow(intensity, cmap='inferno', extent=(-2, 2, -2, 2))
    plt.xlabel("Relative RA (μas)"); plt.ylabel("Relative Dec (μas)")
    plt.title(f"TFM Black Hole Shadow (R = {radius:.2f} μas)")
    plt.savefig(save_path)
    plt.close()

# Example: M87* (6.5e9 solar masses)
M_m87 = 6.5e9 * const.M_sun.value
shadow_tfm = tfm_shadow_radius(M_m87, 1.2e-5, 14.8)
shadow_gr = 2.6 * 2 * const.G.value * M_m87 / const.c.value**2

# Convert to microarcseconds for EHT comparison
parsec_to_meter = 3.086e16
distance_m87 = 16.8e6 * parsec_to_meter  # 16.8 Mpc
shadow_tfm_muas = (shadow_tfm / distance_m87) * (180/np.pi) * 3.6e9  # rad → μas
plot_shadow_image(shadow_tfm_muas)
