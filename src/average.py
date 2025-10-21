import pandas as pd

data = pd.read_csv('data/measurements.csv')
avg_weight = data['weight'].mean()

with open('results.txt', 'w') as f:
    f.write(f'Average weight: {avg_weight:.2f}\n')

print("Average weight written to results.txt")