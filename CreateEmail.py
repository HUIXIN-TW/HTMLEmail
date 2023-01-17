import os
import sys
from Client import Client as C


def main():
    ClientName = sys.argv[1]
    PATH = f'Client/{ClientName}.json'
    Client = C(PATH)
    with open('template.html') as f:
        content = f.read()
        content = content.replace('{BOOKING_TYPE}', Client.BOOKING_TYPE)
        content = content.replace('{CLIENT_NAME}', Client.CLIENT_NAME)
        content = content.replace('{CLEANING_DATE}', Client.CLEANING_DATE)
        content = content.replace('{CLEANER_NAME}', Client.CLEANER_NAME)
        content = content.replace('{CLEANER_CONTACT}', Client.CLEANER_CONTACT)
        content = content.replace('{LOCATION}', Client.LOCATION)
        content = content.replace('{SERVICE_TYPE}', Client.SERVICE_TYPE)
        content = content.replace('<!-- {SERVICE_DETAIL} -->', Client.SERVICE_DETAIL)
        content = content.replace('{SERVICE_PAYMENT}', Client.SERVICE_PAYMENT)
        content = content.replace('{SERVICE_NOTE}', Client.SERVICE_NOTE)
        content = content.replace('{SERVICE_DDMMHHmm}', Client.SERVICE_DDMMHHmm)
        content = content.replace('{ATTACHMENT_iCAL}', Client.ATTACHMENT_iCAL)
        email = open("OutputEmail/Email.html", "w")
        email.write(content)
        email.close()

if __name__ == '__main__':
    main()
