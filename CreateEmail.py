import os
from dotenv import load_dotenv


load_dotenv()

# need to update manually
# how about .json?
BOOKING_TYPE = os.getenv('BOOKING_TYPE')
CLIENT_NAME = os.getenv('CLIENT_NAME')
CLEANING_DATE = os.getenv('CLEANING_DATE')
CLEANER_NAME = os.getenv('CLEANER_NAME')
CLEANER_CONTACT = os.getenv('CLEANER_CONTACT')
LOCATION = os.getenv('LOCATION')
SERVICE_TYPE = os.getenv('SERVICE_TYPE')
SERVICE_DETAIL = os.getenv('SERVICE_DETAIL')
SERVICE_PAYMENT = os.getenv('SERVICE_PAYMENT')
SERVICE_NOTE = os.getenv('SERVICE_NOTE')
SERVICE_DDMMHHmm = os.getenv('SERVICE_DDMMHHmm')
ATTACHMENT_iCAL = os.getenv('ATTACHMENT_iCAL')

def main():
    with open('template.html') as f:
        content = f.read()
        content = content.replace('{BOOKING_TYPE}', BOOKING_TYPE)
        content = content.replace('{CLIENT_NAME}', CLIENT_NAME)
        content = content.replace('{CLEANING_DATE}', CLEANING_DATE)
        content = content.replace('{CLEANER_NAME}', CLEANER_NAME)
        content = content.replace('{CLEANER_CONTACT}', CLEANER_CONTACT)
        content = content.replace('{LOCATION}', LOCATION)
        content = content.replace('{SERVICE_TYPE}', SERVICE_TYPE)
        content = content.replace('{SERVICE_DETAIL}', SERVICE_DETAIL)
        content = content.replace('{SERVICE_PAYMENT}', SERVICE_PAYMENT)
        content = content.replace('{SERVICE_NOTE}', SERVICE_NOTE)
        content = content.replace('{SERVICE_DDMMHHmm}', SERVICE_DDMMHHmm)
        content = content.replace('{ATTACHMENT_iCAL}', ATTACHMENT_iCAL)
        email = open("OutputEmail/Email.html", "w")
        email.write(content)
        email.close()

if __name__ == '__main__':
    main()
