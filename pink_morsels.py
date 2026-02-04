import pandas as pd
import glob

# Get all CSV files from the data folder
files = glob.glob("data/*.csv")

all_data = []

for file in files:
    df = pd.read_csv(file)

    # Keep only Pink Morsels
    df = df[df["product"] == "Pink Morsels"]

    # Create Sales column
    df["Sales"] = df["quantity"] * df["price"]

    # Keep required columns
    df = df[["Sales", "date", "region"]]

    # Rename columns
    df.columns = ["Sales", "Date", "Region"]

    all_data.append(df)

# Combine all data into one file
final_df = pd.concat(all_data)

# Save output
final_df.to_csv("final_output.csv", index=False)

print("Final output file created!")
