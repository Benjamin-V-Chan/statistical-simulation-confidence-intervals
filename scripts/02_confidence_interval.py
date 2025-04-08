import numpy as np
import pandas as pd
import os
import argparse
from scipy import stats

def compute_confidence_interval(data, confidence):
    n = len(data)
    mean = np.mean(data)
    se = stats.sem(data)
    t_critical = stats.t.ppf((1 + confidence) / 2.0, df=n-1)
    margin = t_critical * se
    return mean - margin, mean + margin

def main():
    parser = argparse.ArgumentParser(description="Calculate confidence interval from data")
    parser.add_argument("--input", type=str, default="../outputs/generated_data.csv", help="Input CSV file with data")
    parser.add_argument("--confidence", type=float, default=0.95, help="Confidence level")
    args = parser.parse_args()
    
    df = pd.read_csv(args.input)
    lower, upper = compute_confidence_interval(df['value'], args.confidence)
    
    results = pd.DataFrame({
        'confidence_level': [args.confidence],
        'ci_lower': [lower],
        'ci_upper': [upper],
        'sample_mean': [np.mean(df['value'])]
    })
    os.makedirs('outputs', exist_ok=True)
    results.to_csv(os.path.join('outputs', 'confidence_interval.csv'), index=False)

if __name__ == "__main__":
    main()