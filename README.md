# TFM Black Hole Singularity & Evaporation Codebase  
**Paper #12 in the Time Field Model (TFM) Series**  
*Repository for "Black Holes as High-Density Space Quanta: Singularity Avoidance and Modified Evaporation"*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.XXXX/zenodo.XXXXXXX)

## Key Features
- 🕳️ **Singularity-free black hole collapse simulations**  
- ⚡ **Modified evaporation rates with wave-lump decoherence**  
- 📡 **Observational predictions for LIGO/Virgo & Event Horizon Telescope**  
- 🖥️ **HPC-ready Einstein Toolkit modifications**  

---

## Quick Start

### Installation
```bash
# Clone repository
git clone https://github.com/alifayyazmalik/tfm-paper12-blackhole-singularity-evaporation.git
cd tfm-paper12-blackhole-singularity-evaporation

# Install Python dependencies
pip install -r requirements.txt

# Setup Einstein Toolkit (HPC simulations)
sudo apt-get install einstein-toolkit
```

### Basic Usage
#### Run a black hole collapse simulation:
```bash
cd hpc_simulations
einstein-toolkit planc_core_collapse.par
```
#### Generate gravitational wave predictions:
```bash
python observational_tests/gw_ringdown.py --mass 10 --lambda 1.2e-5 --beta 14.8
```
#### Calculate shadow radius for M87*:
```python
from observational_tests.shadow_raytracing import tfm_shadow_radius
print(tfm_shadow_radius(6.5e9, 1.2e-5, 14.8))  # 25.3 μas
```

## Key Components
| Directory                | Contents                                      |
|--------------------------|-----------------------------------------------|
| `einstein_toolkit_mods/` | Modified GRHydro/McLachlan code               |
| `hpc_simulations/`       | Collapse parameter files & scripts           |
| `observational_tests/`   | GW/shadow prediction scripts                  |
| `data/`                  | Sample LIGO/EHT datasets                      |

## Validation & Testing
### Validation Status
Follow our step-by-step validation guide:
📘 [Validation Instructions](./validation_guide.md)

### Expected First-Run Results:
```
[COLLAPSE SIMULATION] Stable Planck-core formed at t=153ms  
[GW PREDICTION] TFM: 168Hz vs GR: 154Hz (+9.1% deviation)  
[SHADOW PREDICTION] 25.3 μas vs GR: 25.0 μas (+1.2%)
```

## Cite This Work
```bibtex
@software{tfm_blackhole_code,
  author = {Malik, Ali Fayyaz},
  title = {TFM Black Hole Singularity & Evaporation Codebase},
  year = {2025},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/alifayyazmalik/tfm-paper12-blackhole-singularity-evaporation}}
}
```

### Full Citation Info
