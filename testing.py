import email
import json
from models.availability import Availability
from models.room import Room
from models.rooms import Rooms
from models.credentials import Credentials
from cryptography.fernet import Fernet
from models.users import Users
from models.email import Email
import requests

def main():

    # url = "https://prod-15.canadacentral.logic.azure.com:443/workflows/d72fb653f1734f0d838a4b96e6239068/triggers/manual/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=VeSm7g3ly7vfi4Mja6hPyp1wj_Zy-tPxRQk1MY8y8rI"
    # obj = {"message":"hi from python2","email":"goutamthukral@gmail.com","subject":"Test"}

    email = Email()
    # email.send_request("goutamthukral@gmail.com","Testing from python", "Testing")


if __name__ == "__main__":
    main()