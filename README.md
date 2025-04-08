# statistical-simulation-confidence-intervals

## Project Overview

This project simulates and analyzes **confidence intervals** for the mean of a normally distributed population using repeated sampling and interval construction via the Student's t-distribution. The goal is to empirically verify the coverage probability of confidence intervals under a variety of assumptions.

### Mathematical Background
Let $\( X_1, X_2, ..., X_n \sim \mathcal{N}(\mu, \sigma^2) \)$ be a random sample of size $\( n \)$ from a normal distribution with unknown mean $\( \mu \)$ and known variance $\( \sigma^2 \)$. If $\( \sigma^2 \)$ is unknown, we estimate it using the sample standard deviation:

$$\bar{X} = \frac{1}{n} \sum_{i=1}^n X_i, \quad s^2 = \frac{1}{n-1} \sum_{i=1}^n (X_i - \bar{X})^2$$

Then, the pivotal quantity

$$T = \frac{\bar{X} - \mu}{s / \sqrt{n}} \sim t_{n-1}$$

follows a t-distribution with $\( n-1 \)$ degrees of freedom. Therefore, a two-sided $\( (1 - \alpha) \)$ confidence interval for $\( \mu \)$ is given by:

$$\left[ \bar{X} - t_{\alpha/2, n-1} \cdot \frac{s}{\sqrt{n}}, \; \bar{X} + t_{\alpha/2, n-1} \cdot \frac{s}{\sqrt{n}} \right]$$

We simulate this interval repeatedly, each time generating a new sample, and then check the proportion of intervals that contain the true mean $\( \mu \)$. This observed coverage should converge to the nominal confidence level as the number of trials increases, due to the **Law of Large Numbers**.

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