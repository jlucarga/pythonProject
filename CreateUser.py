from mongodb import checkCredentials
from mongodb import add_new_employee_user

def main(username, password):
    if checkCredentials(username, password) == True:
        print("This username or password already exist")
        return
    else:
        add_new_employee_user(username, password)
    print("Successful account created")
    return #-----redirect to login page-----##

if __name__ == '__main__':
    main()
