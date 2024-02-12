import numpy as np  # Import NumPy library
from datasets import load_dataset  # Import load_dataset function from datasets

# Load the heart failure dataset
dataset = load_dataset("mstz/heart_failure")

# Access the "train" partition of the dataset
data = dataset["train"]

# Extract the list of ages from the dataset
ages = data["age"]

# Convert the list of ages to a NumPy array
ages_array = np.array(ages)

# Calculate the average age using NumPy's mean function
average_age = np.mean(ages_array)

print("Average age of the study participants:", average_age)