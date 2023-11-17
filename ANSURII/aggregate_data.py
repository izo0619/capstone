import pandas as pd

def summarize_csv_with_pandas(input_file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(input_file, encoding='latin-1')

    select_columns = ["abdominalextensiondepthsitting", "chestbreadth",
    "chestcircumference", "chestdepth", "chestheight", "verticaltrunkcircumferenceusa", 
    "waistbacklength", "waistbreadth", "waistcircumference", "waistdepth", "waistfrontlengthsitting",
    "waistheightomphalion", "weightkg", "Heightin", "Weightlbs"]
    df = df[select_columns].astype(int)
    # Filter rows where the specified column's value is less than or equal to the threshold
    filtered_df = df[(df["weightkg"] <= 2000) & (df["weightkg"] >= 550)]
    # Calculate summary statistics for the filtered DataFrame
    summaries = filtered_df.describe(include="all", percentiles=[0.05, .25, .5, .75, 0.95])
    summaries.to_csv(f"{input_file}_aggregate.csv")
    return summaries

# Usage example
input_file = 'ANSUR II FEMALE Public.csv'  # Replace with the actual file name

result = summarize_csv_with_pandas(input_file)

# Print the summaries
print(result)