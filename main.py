import smtplib
from email.message import EmailMessage
import time

sender_email = "" #Enter your email
rec_email = "" #Receiver email
password = '' #Email password (or google app passwd"
msg = EmailMessage()
msg.set_content('Body') #Email body
msg['Subject'] = f'Subject' #Change subject
msg['From'] = sender_email 
msg['To'] = rec_email

#This three lines attach a pdf to the message, if not needed , comment it
with open("/Path/to/file.pdf", 'rb') as fp: #Change path
        pdf_data = fp.read()
        msg.add_attachment(pdf_data, maintype='application', subtype='octet-stream', filename='file.pdf') #change file name
#-----------------------------------------------------------------------

def main():
    server = smtplib.SMTP('smtp.gmail.com', 587) #Mail server and port are set by default for gmail
    server.starttls()    
    server.login(sender_email, password)
    print('Login success!')
    while True:
        now = time.gmtime()
        if now[3] == 17 and now[4] == 10 and now[5] == 0: #now[3] = hour , now[4] = minutes , now[5] = seconds
            server.send_message(msg)
            print("The email has been sent to " + rec_email)
            time.sleep(1)
        else:
            print('Waiting... ' + time.asctime())
            time.sleep(1)

if __name__ == "__main__":
    main()

#Coded by NewtonHead <3
