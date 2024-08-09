"""
Q10. Wap to read age of 15 people and find the number of adults, babies and school age students.
"""
num_adults = 0
num_babies = 0
num_school_age = 0

# Input ages of 15 people using a for loop
print("Enter ages of 15 people:")
for i in range(1, 16):  # Loop runs from 1 to 15 inclusive
    age = int(input(f"Enter age of person {i}: "))

    # Categorize based on age
    if age >= 18:
        num_adults += 1
    elif 0 <= age <= 4:
        num_babies += 1
    elif 5 <= age <= 17:
        num_school_age += 1
    else:
        print(f"Invalid age entered for person {i}: {age}")

# Print results
print(f"Number of adults: {num_adults}")
print(f"Number of babies: {num_babies}")
print(f"Number of school: {num_school}")