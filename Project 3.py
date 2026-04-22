import pandas as pd


# --- 1. The Class Definition ---
class RescuePet:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
        self.is_adopted = False

    def process_adoption(self):
        self.is_adopted = True
        print(f"Success! {self.name} has been adopted.")


# --- 2. Combining Data ---
df_a = pd.read_csv('shelter_A.csv')
df_b = pd.read_csv('shelter_B.csv')

# Combine and ignore index to prevent duplicate row numbers
df_combined = pd.concat([df_a, df_b], ignore_index=True)

# --- 3. Data Cleaning ---
# Drop missing values
df_cleaned = df_combined.dropna().copy()

# Filter to show only dogs
df_dogs = df_cleaned[df_cleaned['Animal_Type'] == 'Dog'].copy()

# --- 4. Integration ---
# Pick the first dog from the filtered list
if not df_dogs.empty:
    first_dog_row = df_dogs.iloc[0]

    # Instantiate the object
    adopted_pet = RescuePet(
        name=first_dog_row['Pet_Name'],
        species=first_dog_row['Animal_Type'],
        age=first_dog_row['Age_Years']
    )

    # Process adoption
    adopted_pet.process_adoption()

    # --- 5. Exporting ---
    # Create a small DataFrame for the adopted dog
    adoption_data = pd.DataFrame([{
        'Pet_Name': adopted_pet.name,
        'Animal_Type': adopted_pet.species,
        'Age_Years': adopted_pet.age,
        'is_adopted': adopted_pet.is_adopted
    }])

    # Append to file. header=False if file already exists to avoid double headers
    file_exists = os.path.isfile('successful_adoptions.csv')
    adoption_data.to_csv('successful_adoptions.csv', mode='a', index=False, header=not file_exists)

    print("Adoption record appended to successful_adoptions.csv")
else:
    print("No dogs found in the database.")

print("\nFinal Cleaned Dog List:")
print(df_dogs)