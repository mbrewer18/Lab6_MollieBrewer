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

def decode_password:



def main():
    while input != 0:
        display_menu()
        op_choice = input("\nPlease enter an option: ")
        try:
            op_choice = int(op_choice)
        except ValueError:
            op_choice = -1

        if op_choice == 0:
            break

        elif op_choice == 1:
            password = input("Please enter your password to encode: ")
            encode_password(password)
            #input a valueerror for password not integar or 8 digits

        elif op_choice == 2:



if __name__ == '__main__':
    main()