from pymongo import MongoClient
client = MongoClient("mongodb+srv://jlgarrido:DB2021@cluster0.jbcth.mongodb.net/<COVID19_Tracking_App>?retryWrites=true&w=majority")


db = client.get_database("COVID19_Tracking_App")

usernameRecords = db.UserDb #imports the list of all the users of the app
passwordRecords = db.UserDb #imports the list of all the users of the app
managerList = db.UserManagerDb #imports the list of managers user of the app
employeeList = db.UserEmployeeDb #imports the list of employee users in the app

#check credential exist in the database
def checkCredentials(username, password):
    string_username = str(username)
    string_password = str(password)
    checkUsername = usernameRecords.count({string_username})
    checkPassword = passwordRecords.count({string_password})
    if checkUsername == 1:
        #print("This username already exist")
        return True
    elif checkPassword == 1:
        #print("This password already exist")
        return True
    else:
        return False

#add a new employee user in the the user database and in the employee user database
def add_new_employee_user(username, password):
    string_username = str(username)
    string_password = str(password)

    new_user = {
        "username": string_username,
        "password": string_password,
        "user_manager": False
    }
    usernameRecords.insert_one(new_user)
    employeeList.insert_one(new_user)

#add a new user to the user database and the manager user database
def add_new_manager_user(username, password):
    string_username = str(username)
    string_password = str(password)
    new_user = {
        "username": string_username,
        "password": string_password,
        "user_manager": True
    }
    usernameRecords.insert_one(new_user)
    managerList.insert_one(new_user)

#verifies the username entered matches the password for the username
def credentialMatch(username, password):
    string_username = str(username)
    string_password = str(password)
    if (string_username, string_password) == (usernameRecords.find_one({string_username})[1],
                                              usernameRecords.find_one({string_username})[2]):
        return True
    else:
        return False

