import json

class Client:
    def __init__(self, fileName) -> None:
        with open(fileName) as f:
            data = json.load(f)
        self.BOOKING_TYPE=data['BOOKING_TYPE']
        self.CLIENT_NAME=data['CLIENT_NAME']
        self.CLEANING_DATE=data['CLEANING_DATE']
        self.CLEANER_NAME=data['CLEANER_NAME']
        self.CLEANER_CONTACT=data['CLEANER_CONTACT']
        self.LOCATION=data['LOCATION']
        self.SERVICE_TYPE=data['SERVICE_TYPE']
        self.SERVICE_DETAIL=data['SERVICE_DETAIL']
        self.SERVICE_PAYMENT=data['SERVICE_PAYMENT']
        self.SERVICE_NOTE=data['SERVICE_NOTE']
        self.SERVICE_DDMMHHmm=data['SERVICE_DDMMHHmm']
        self.ATTACHMENT_iCAL=data['ATTACHMENT_iCAL']

    def __str__(self):
        return f'This object belongs to {Client.CLIENT_NAME}'
