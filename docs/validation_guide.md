# Validating TFM Black Hole Predictions

## Gravitational Wave Ringdowns
1. Generate waveforms:
   ```bash
   python observational_tests/gw_ringdown.py --mass 10 --lambda 1.2e-5 --beta 14.8
2. Compare to LIGO/Virgo events using pycbc_inference.
   from observational_tests.shadow_raytracing import tfm_shadow_radius
radius = tfm_shadow_radius(6.5e9, 1.2e-5, 14.8)

**Shadow Imaging**
1. Run raytracing:
from observational_tests.shadow_raytracing import tfm_shadow_radius
radius = tfm_shadow_radius(6.5e9, 1.2e-5, 14.8)
2. Compare to EHT M87* data in data/eht_m87.csv.
3. 
