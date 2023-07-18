users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

# Recreate the 1st result
disney_users_A = {}
for i, user in enumerate(users):
    disney_users_A[user] = i
print(disney_users_A)

# Recreate the 2nd result
disney_users_B = {}
for i, user in enumerate(users):
    disney_users_B[i] = user
print(disney_users_B)

# Recreate the 3rd result
disney_users_C = dict(sorted(disney_users_A.items()))
print(disney_users_C)

# Recreate the 1st result for characters with names containing the letter "i"
disney_users_A_filtered = {}
for i, user in enumerate(users):
    if 'i' in user:
        disney_users_A_filtered[user] = i
print(disney_users_A_filtered)

# Recreate the 1st result for characters with names starting with "m" or "p"
disney_users_A_filtered2 = {}
for i, user in enumerate(users):
    if user.startswith('m') or user.startswith('p'):
        disney_users_A_filtered2[user] = i
print(disney_users_A_filtered2)
