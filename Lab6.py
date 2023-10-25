#Mollie Brewer

def display_menu():
    print("\n\nMenu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

def encode_password(password):
    stored_password = password
    print("Your password has been encoded and stored!")
    return stored_password

def decode_password():
    pass




def main():
    while input != 0:
        display_menu()
        op_choice = input("\nPlease enter an option: ")
        try:
            op_choice = int(op_choice)
        except ValueError:
            print("Option must be a value 1-3. Try again!")

        if op_choice == 0:
            break

        elif op_choice == 1:
            password = input("Please enter your password to encode: ")
            encode_password(password)
            try:
                op_choice = int(op_choice)
            except ValueError as error1:
                print("Password must be number. Try again!")
            except ValueError as error2:

                print()

        elif op_choice == 2:
            pass





if __name__ == '__main__':
    main()