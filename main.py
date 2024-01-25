import pandas as pd
import numpy as np
import pandas as pd

# Create a synthetic healthcare dataset
np.random.seed(42)

# Generate synthetic patient data
num_patients = 500
age = np.random.randint(18, 80, size=num_patients)
gender = np.random.choice(['Male', 'Female'], size=num_patients)
conditions = np.random.choice(['Diabetes', 'Heart Disease', 'Asthma', 'None'], size=num_patients)
hospital_visits = np.random.randint(1, 10, size=num_patients)
length_of_stay = np.random.randint(1, 15, size=num_patients)

# Create a DataFrame
df = pd.DataFrame({
    'Age': age,
    'Gender': gender,
    'Condition': conditions,
    'HospitalVisits': hospital_visits,
    'LengthOfStay': length_of_stay
})

# Save the synthetic dataset to a CSV file
df.to_csv('healthcare_dataset.csv', index=False)
