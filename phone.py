def validate_phone_number(phone_number):
    # Remove any spaces or dashes from the phone number
    phone_number = phone_number.replace(" ", "").replace("-", "")
    
    # Check if the phone number consists of exactly 10 digits
    if phone_number.isdigit() and len(phone_number) == 10:
        print("Valid phone number!")
    else:
        print("Invalid phone number. Please enter a 10-digit number without spaces or dashes.")

# Taking phone number input from the user
phone_number = input("Enter your phone number (10 digits only): ")
validate_phone_number(phone_number)
