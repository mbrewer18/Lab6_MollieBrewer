
# Lab 6
# Owner: Mollie Brewer
# Collaborator: Wesly Menard

def display_menu():
    print("\n\nMenu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

def encode_password(password):
    stored_password = str(password)  # Convert passwrd to a string so it can work in my DECODE function
    print("Your password has been encoded and stored!")
    return stored_password


def decode_password(password):
    decoded_password = []
    for i in password:
        if i == "0":
            decoded_password.append("3")
        elif i == "1":
            decoded_password.append("4")
        elif i == "2":
            decoded_password.append("5")
        elif i == "3":
            decoded_password.append("6")
        elif i == "4":
            decoded_password.append("7")
        elif i == "5":
            decoded_password.append("8")
        elif i == "6":
            decoded_password.append("9")
        elif i == "7":
            decoded_password.append("0")
        elif i == "8":
            decoded_password.append("1")
        elif i == "9":
            decoded_password.append("2")
        else:
            decoded_password.append(i)
    return ''.join(decoded_password)

# password = "123434224"
# decoded_password = decode_password(password)
# print(decoded_password)





def main():
    password = ""
    while input != 3:
        display_menu()
        op_choice = input("\nPlease enter an option: ")
        try:
            op_choice = int(op_choice)
            if op_choice > 3 or op_choice < 1:
                raise ValueError

        except ValueError:
            print("Invaild Option. Try again!")

        if op_choice == 1:
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
            decoded_password = decode_password(password)
            print(f'The encoded password is {decoded_password} and the original password is {password}')


        elif op_choice == 3:  # Exit program if user inputs 3
            break

if __name__ == '__main__':
    main()


