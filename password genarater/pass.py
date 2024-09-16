from itertools import combinations, product

# Define the list of passwords
passwords = [
    "agaga", "lawrence", ".",
    "a", "b", "c",
    "12345", "123",
     "0788080524"
]

# Generate possible case variations
def generate_case_variations(password):
    return [
        password.lower(),
        password.upper(),
        password.title()
    ]

# Combine each pair of passwords
def combine_passwords(pw1, pw2):
    pw1_variations = generate_case_variations(pw1)
    pw2_variations = generate_case_variations(pw2)
    combined = []
    for var1 in pw1_variations:
        for var2 in pw2_variations:
            combined.append(var1 + var2)
            combined.append(var2 + var1)
    return combined

# Create a list to store all possible combined passwords
all_combinations = []

# Generate all combinations of two different passwords
for pw1, pw2 in combinations(passwords, 2):
    all_combinations.extend(combine_passwords(pw1, pw2))

# Output all possible combined passwords
for pw in all_combinations:
    print(pw)
