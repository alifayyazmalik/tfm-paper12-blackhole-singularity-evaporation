# TFM Paper #12: Black Hole Singularity & Evaporation Codebase

Reproduce results from:  
*"Black Holes as High-Density Space Quanta: Singularity Avoidance and Modified Evaporation in the Time Field Model"*

## Quick Start
1. Install Einstein Toolkit dependencies:  
   ```bash
   sudo apt-get install einstein-toolkit
2. Run HPC collapse simulation:
cd hpc_simulations  
einstein-toolkit planc_core_collapse.par
3. Generate observational predictions:
python observational_tests/shadow_raytracing.py  
python observational_tests/gw_ringdown.py
