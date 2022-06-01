attempts = 3
print(f"Your card has been accepted by the ATM. You have {attempts} attempts left.")
while attempts != 0:
    try:
        enter_pass = int(input("Please enter your PIN code: "))
    except ValueError:
        print("Oops, you entered something wrong! Enter only numbers. Repeat one more time.")
        continue
    else:
        if enter_pass == 1234:
            print ("\nYou have entered the correct pin-code. The card has been unlocked!")
            break
        elif attempts == 0:
            continue
        else:
            attempts -= 1
            print(f"\nInvalid pin code. Please try again. You have {attempts} attempts left.")
            print("--------------------------------------------------")
else:
    print ("\nThe card is blocked. You have 0 attempts left.")