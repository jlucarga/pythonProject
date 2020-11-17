from pymongo import MongoClient
client = MongoClient("mongodb+srv://jlgarrido:DB2021@cluster0.jbcth.mongodb.net/<COVID19_Tracking_App>?retryWrites=true&w=majority")


db = client.get_database("COVID19_Tracking_App")

usernameRecords = db.UserDb #imports the list of all the users of the app
passwordRecords = db.UserDb #imports the list of all the users of the app
managerList = db.UserManagerDb #imports the list of managers user of the app
employeeList = db.UserEmployeeDb #imports the list of employee users in the app
healthRecords = db.HealthRecordsDb #import the list of health records that contains the badges and the date for all the users

def save_badge(username, badge_color, date):
    string_username = str(username)
    string_badge_color = str(badge_color)
    healthRecords.insert_one({"username": string_username, "badge_color": string_badge_color, "date": date})

