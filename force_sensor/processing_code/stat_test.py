import numpy as np
from scipy.stats import ttest_rel, f_oneway
import pandas as pd

def agg_data(file):
    df = pd.read_csv(file)
    agg_all = np.array([df['ave0'],df['ave1'],df['ave2']])
    agg_final = []

    for i in range(len(df['ave1'])):
        agg = np.mean(agg_all[:,i])
        agg_final.append(agg)
    return agg_final

# Sample data for two paired groups
ct = agg_data("processing_code/CT.csv")
corset = agg_data("processing_code/corset10_data.csv")

# Perform paired t-test
t_statistic, p_value = ttest_rel(ct, corset)

# Display the results
print("Paired t-test results:")
print(f"T-statistic: {t_statistic}")
print(f"P-value: {p_value}")

# Check the significance level (commonly 0.05)
alpha = 0.05
if p_value < alpha:
    print("The difference between the groups is statistically significant.")
else:
    print("There is no significant difference between the groups.")


# 1 way anova across trials
corset_df = pd.read_csv("processing_code/corset10_data.csv")
# columns into arrays
all_trials = []
for i in range(10):
    trial = np.array(corset_df[f'ave{i}'])
    all_trials.append(trial)
all_trials = np.array(all_trials)
f_statistic, p_value = f_oneway(*all_trials)

# Display the results
print("One-way ANOVA results:")
print(f"F-statistic: {f_statistic}")
print(f"P-value: {p_value}")

# Check the significance level (commonly 0.05)
alpha = 0.05
if p_value < alpha:
    print("There is a significant difference among the groups.")
else:
    print("There is no significant difference among the groups.")
