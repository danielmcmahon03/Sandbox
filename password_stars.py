MINIMUM = 10
password = input("Password: ")
while len(password) < MINIMUM:
    print(f"Password must have a length greater or equal to {MINIMUM}.")
    password = input("Password: ")
print("*" * len(password))
