import numpy as np
import pandas as pd
import argparse
import os
from scipy import stats

def simulate_experiment(sample_size, true_mean, true_std, confidence):
    data = np.random.normal(loc=true_mean, scale=true_std, size=sample_size)
    sample_mean = np.mean(data)
    n = len(data)
    se = stats.sem(data)
    t_critical = stats.t.ppf((1 + confidence) / 2.0, df=n-1)
    margin = t_critical * se
    ci_lower = sample_mean - margin
    ci_upper = sample_mean + margin
    coverage = (ci_lower <= true_mean) and (true_mean <= ci_upper)
    return sample_mean, ci_lower, ci_upper, coverage

def main():
    parser = argparse.ArgumentParser(description="Run simulation experiments for confidence intervals")
    parser.add_argument("--simulations", type=int, default=1000, help="Number of simulations")
    parser.add_argument("--sample_size", type=int, default=50, help="Sample size for each experiment")
    parser.add_argument("--true_mean", type=float, default=50, help="True mean of the distribution")
    parser.add_argument("--true_std", type=float, default=10, help="True standard deviation of the distribution")
    parser.add_argument("--confidence", type=float, default=0.95, help="Confidence level")
    args = parser.parse_args()
    
    results = []
    for i in range(args.simulations):
        sample_mean, ci_lower, ci_upper, coverage = simulate_experiment(args.sample_size, args.true_mean, args.true_std, args.confidence)
        results.append([i+1, sample_mean, ci_lower, ci_upper, coverage])
    
    sim_df = pd.DataFrame(results, columns=["trial", "sample_mean", "ci_lower", "ci_upper", "coverage"])
    os.makedirs('outputs', exist_ok=True)
    sim_df.to_csv(os.path.join('outputs', 'simulation_results.csv'), index=False)

if __name__ == "__main__":
    main()