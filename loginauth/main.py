import bcrypt
import webbrowser


user_credentials = {}
def main():
    while True:
        print("1 : login, 2 : Register, 3:Exit")
        choice = int(input("Enter you Choice :" ))
    
        if choice == 1:
            login()
        elif choice == 2:
            register()
        elif choice == 3:
            print("Exit...")
            break
        else:
            print("Invalid input")
def login():
    print("⚠️----Make sure you have an account----⚠️")
    userName = input("Enter the USERNAME : ")

    if userName not in user_credentials:
        print("User Not Found Do Register First!!!🔄️")
        return

    password = input("Enter the secret password 🫣: ")
    stored_hashed_password = user_credentials[userName]

    if bcrypt.checkpw(password.encode('utf-8'), stored_hashed_password):
        print("You logged successfully 🤠")
        html_file_path = 'D:/OIBSIP/loginauth/index.html'

        webbrowser.open(html_file_path)


    else:
        print("Ummm..🫤..Incorrect Password")

def register():
    print("It may take ONLY a few minutes to register ")
    userName = input("Enter the your user name : ")

    if userName in user_credentials:
        print("You already REGISTERED please DO check once")
    password = input("Create a strong password🤫 : ")

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    user_credentials[userName] = hashed_password

    print("You registered successfully")
main()