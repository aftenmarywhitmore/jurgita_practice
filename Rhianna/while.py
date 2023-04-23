# Start with users that need to be verified,
# and an empty list to hold confirmed users.

unconfirmed_users= ['alice', 'brian', 'candace']
confirmed_users= []

# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.

while unconfirmed_users:
    current_user= unconfirmed_users.pop()

    print("verifying user: " + current_user.title())
    confirmed_users.append(current_user)
# Display all confirmed users.

print("\nThe following users have been confirmed")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


age = int(input("What is your age?: "))
while age:
    age += 1
    if age < 3:
        print("You're ticket is free")
        continue
    if age > 12:
        print("ticket is $15")
    elif age < 12:
            print("you pay $10")
    break
else:
    print("ticket is free")
   
        