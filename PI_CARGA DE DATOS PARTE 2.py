import pandas as pd  # Import Pandas library
from datasets import load_dataset  # Import load_dataset function from datasets

# Load the heart failure dataset
dataset = load_dataset("mstz/heart_failure")

# Access the "train" partition of the dataset
data = dataset["train"]

# Convert the Dataset to a Pandas DataFrame
df = pd.DataFrame(data)

# Separate the DataFrame into two based on the "is_dead" column
dead_df = df[df["is_dead"] == 1]
alive_df = df[df["is_dead"] == 0]

# Calculate the average ages for each dataset
average_age_dead = dead_df["age"].mean()
average_age_alive = alive_df["age"].mean()

print("Average age of deceased individuals:", average_age_dead)
print("Average age of surviving individuals:", average_age_alive)

# Verify the data types of each column in the DataFrame
data_types = df.dtypes
print("Data types of each column:")
print(data_types)

# Calculate the number of male and female smokers using Pandas aggregations
smoker_counts = df.groupby(["is_male", "is_smoker"]).size().unstack(fill_value=0)
print("\nNumber of male and female smokers:")
print(smoker_counts)