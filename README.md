# statistical-simulation-confidence-intervals

## Project Overview

This project simulates and analyzes **confidence intervals** for the mean of a normally distributed population using repeated sampling and interval construction via the Student's t-distribution. The goal is to empirically verify the coverage probability of confidence intervals under a variety of assumptions.

## Folder Structure
```
project-root/
├── scripts/
│   ├── 01_generate_data.py
│   ├── 02_confidence_interval.py
│   ├── 03_simulation_analysis.py
│   └── 04_visualization.py
├── outputs/
│   ├── generated_data.csv
│   ├── confidence_interval.csv
│   ├── simulation_results.csv
│   └── simulation_plot.png
├── requirements.txt
└── README.md
```

## Usage

### 1. Setup the Project:
Clone the repository.  
Ensure you have Python installed.  
Install required dependencies using the requirements.txt file:
```bash
pip install -r requirements.txt
```

### 2. Generate Synthetic Data
Generates one sample dataset from a normal distribution:
```bash
python scripts/01_generate_data.py
```

### 3. Compute a Confidence Interval for the Sample
Calculates a confidence interval using the t-distribution:
```bash
python scripts/02_confidence_interval.py --input outputs/generated_data.csv --confidence 0.95
```

### 4. Run Confidence Interval Simulation
Simulates many confidence intervals to empirically determine coverage:
```bash
python scripts/03_simulation_analysis.py --simulations 1000 --sample_size 50 --true_mean 50 --true_std 10 --confidence 0.95
```

### 5. Visualize the Simulation Results
Plots a histogram of sample means and shows empirical coverage:
```bash
python scripts/04_visualization.py --input outputs/simulation_results.csv --output simulation_plot.png
```

## Requirements

The project uses the following Python libraries:
- numpy
- pandas
- scipy
- matplotlib
- argparse