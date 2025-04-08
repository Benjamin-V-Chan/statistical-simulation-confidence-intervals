import pandas as pd
import matplotlib.pyplot as plt
import argparse
import os

def main():
    parser = argparse.ArgumentParser(description="Visualize simulation results")
    parser.add_argument("--input", type=str, default="../outputs/simulation_results.csv", help="Input CSV file with simulation results")
    parser.add_argument("--output", type=str, default="simulation_plot.png", help="Output image file name")
    args = parser.parse_args()
    
    df = pd.read_csv(args.input)
    coverage_prob = df['coverage'].mean()
    plt.figure(figsize=(10,6))
    plt.hist(df['sample_mean'], bins=30, alpha=0.7, edgecolor='black')
    plt.axvline(df['sample_mean'].mean(), color='red', linestyle='dashed', linewidth=2)
    plt.title(f"Histogram of Sample Means\nCoverage Probability: {coverage_prob:.2f}")
    plt.xlabel("Sample Mean")
    plt.ylabel("Frequency")
    os.makedirs('outputs', exist_ok=True)
    plt.savefig(os.path.join('outputs', args.output))
    plt.close()

if __name__ == "__main__":
    main()