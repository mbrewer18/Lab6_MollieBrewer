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

def decode_password(stored_password):
    for i in range(len(stored_password)):
        i +=3
        return i




def main():
    while input != 0:
        display_menu()
        op_choice = input("\nPlease enter an option: ")
        try:
            op_choice = int(op_choice)
        except ValueError:
            print("Option must be a value 1-3. Try again!")
            #fix this

        if op_choice == 0:
            break

        elif op_choice == 1:
            password = input("Please enter your password to encode: ")
            try:
                password = int(password)
                if len(str(password)) != 8:
                    print("Password must be 8 digits. Try again!")
                else:
                    encode_password(password)
            except ValueError:
                print("Password must be all numbers. Try again!")


        elif op_choice == 2:
            pass






if __name__ == '__main__':
    main()