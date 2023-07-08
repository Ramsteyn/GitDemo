credentials = ["Firstname", "Surname", "Mail ID", "Password", "Date of Birth", "Month of Birth", "Born Year", "Gender"]
user_Details = []

for i in credentials:
    user_Details.append(input("Please enter the" + i))

print(user_Details)