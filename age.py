def check_voting_eligibility(age):
    if age >= 18:
        print("You are eligible to vote!")
    else:
        print("You are not eligible to vote yet.")

# Taking age input from the user
try:
    age = int(input("Enter your age: "))
    check_voting_eligibility(age)
except ValueError:
    print("Please enter a valid age as a number.")
