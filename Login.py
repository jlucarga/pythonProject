from mongodb import credentialMatch
from pymongo import MongoClient

client = MongoClient("mongodb+srv://<jlgarrido>:<DB2021>@cluster0.jbcth.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = client.get_database("COVID19_Tracking_App")
usernameRecords = db.UserDb #imports the list of all the users of the app

def main(username, password):

    string_username = str(username)
    string_password = str(password)

    if credentialMatch(username,password) == False:
        print("username or password do not match pur records")
        return
    else:
        user_type = usernameRecords.find_one({"username": string_username}["user_type"])

        if user_type == False:
            return  # redirect to manager home
        elif user_type == True:
            return  # redirect to employee home


if __name__ == '__main__':
    main(username, password)

