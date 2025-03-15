# Validating TFM Black Hole Predictions

## Prerequisites
1. Install required Python packages:
   ```bash
   pip install -r ../requirements.txt  # Installs numpy, matplotlib, astropy, pandas, pycbc
   ```
2. Install Einstein Toolkit (for HPC simulations):
   ```bash
   sudo apt-get install einstein-toolkit
   ```

## 1. Gravitational Wave Analysis
### Generate TFM Ringdown Predictions
```bash
# For a 10 solar mass black hole
python ../observational_tests/gw_ringdown.py --mass 10 --lambda 1.2e-5 --beta 14.8

# Expected output:
# TFM ringdown frequency: 168.23 Hz
# GR prediction: 154.12 Hz
# Deviation: +9.15%
```

### Compare with LIGO Observations
#### Download sample LIGO data:
```bash
wget https://example.com/ligo_sample_data.hdf5 -O data/ligo_sample.hdf5
```
#### Run comparison:
```bash
pycbc_inference --config-file ../configs/gw_comparison.ini \
                --output-file results/tfm_ligo_comparison.hdf
```

## 2. Black Hole Shadow Analysis
### Calculate Shadow Radius
```python
from observational_tests.shadow_raytracing import tfm_shadow_radius

# For M87* (6.5 billion solar masses)
radius = tfm_shadow_radius(6.5e9, 1.2e-5, 14.8)
print(f"TFM Shadow Radius: {radius:.2f} μas")  # Expected: 25.3 μas
```

### Generate Shadow Image
```python
from observational_tests.shadow_raytracing import plot_shadow_image
plot_shadow_image(radius, "results/m87_shadow.png")
```

### Compare with EHT Data
```python
import pandas as pd

eht_data = pd.read_csv("../data/eht_m87.csv")
gr_prediction = 25.0  # μas
difference = ((radius - gr_prediction)/gr_prediction) * 100
print(f"TFM vs GR difference: {difference:.2f}%")  # Expected: +1.2%
```

## Expected Results
| Prediction Type        | TFM Result | GR Prediction | Allowed Deviation |
|------------------------|------------|--------------|------------------|
| Ringdown Frequency     | 168.23 Hz  | 154.12 Hz    | ±10%             |
| Shadow Radius (M87*)   | 25.3 μas   | 25.0 μas     | ±1%              |
| Evaporation Rate       | 1.3× Hawking | 1.0× Hawking | ±0.5×           |

## Troubleshooting
### Common Issues
#### Missing Data Files:
```bash
wget https://example.com/tfm_sample_data.zip
unzip tfm_sample_data.zip -d data/
```

#### Dependency Errors:
```bash
pip install --upgrade -r ../requirements.txt
```

#### HPC Simulation Failures:
##### Verify Einstein Toolkit installation:
```bash
einstein-toolkit --version
```
##### Check memory requirements:
```bash
free -h
```

## Support
For additional help, open an issue at:
[GitHub Issues](https://github.com/yourusername/tfm-blackhole-repo/issues)
