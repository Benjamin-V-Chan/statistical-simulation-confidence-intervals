import numpy as np
import pandas as pd
import os

def main():
    np.random.seed(42)
    sample_size = 100
    true_mean = 50
    true_std = 10
    data = np.random.normal(loc=true_mean, scale=true_std, size=sample_size)
    df = pd.DataFrame({'value': data})
    os.makedirs('outputs', exist_ok=True)
    df.to_csv(os.path.join('outputs', 'generated_data.csv'), index=False)

if __name__ == "__main__":
    main()