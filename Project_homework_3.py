new_dict = {}
while True:
    try:
        elements = int(input("Please, enter the desired number of dictionary items: "))
    except ValueError:
        print("You entered something incorrectly! Enter only whole numbers, and please try again!\n")
    else:
        break
    
for a in range(elements):    
    user_key = input("Please, enter keys: ")
    new_dict[user_key] = input("Please, enter values: ")
print("\nYou have created a dictionary: ", new_dict)

while True:
    try:
        correction = int(input("\nHow would you like to do with the dictionary? \n(1 - save and exit; 2 - remove dictionary element): "))
    except:
        print("Enter the number from the options provided!")
        continue
    if correction == 1:
        print ("Уour dictionary is saved. Bye!")
        break
    elif correction == 2:
        if len(new_dict) != 0:
            while True:
                remove = input(f"\nPlease enter the element you wish to remove? \n{list(new_dict.items())}: ")
                try:
                    del new_dict[remove]        
                except KeyError:
                    print(f"Enter the name of the key whose value you wish to remove:{list(new_dict.keys())}")
                    continue
                else:
                    print (f"\nDictionary element {remove} removed \nNew dictionary: {new_dict}")
                    break
        else:
            print("Your dictionary is empty! Bye!")
            break

    else:
        print("\nEnter the number from the options provided!")