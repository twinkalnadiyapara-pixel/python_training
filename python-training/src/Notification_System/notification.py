import smtplib 
import logging
import tkinter
from tkinter import messagebox

logging.basicConfig(filename="D:/python-training/logs/notification.log",
                    level=logging.ERROR , filemode="w",
                    format="{message}={asctime}:{name}:{levelname}:{process}:{lineno}",
                    datefmt="%d-%b-%y %H:%M:%S",
                    style="{")

class ISEMAILSENDVALID:
    def is_email_send_valid(self):
        while True:
            try :
                SEND_Email_Address : int | float = input("Enter your Email Address : ")

                if "@" in SEND_Email_Address and "." in SEND_Email_Address :
                    return SEND_Email_Address
                    break
            except :
                logging.error("Please Enter Valid Email Adress")
isemailsendvalid = ISEMAILSENDVALID()

class ISEMAILRECEIVEVALID:
    def is_email_recieve_valid(self):
        while True:
            try :
                Receive_Email_Address : int | float = input("Enter your Email Address : ")

                if "@" in Receive_Email_Address and "." in Receive_Email_Address :
                    return Receive_Email_Address
                    break
            except :
                logging.error("Please Enter Valid Email Adress")
isemailrecievevalid = ISEMAILRECEIVEVALID()


class EMAILNOTIFICATION:
    def email_notification(self): 
        try:  
            SEND_Email_Address = isemailsendvalid.is_email_send_valid()
            Receive_Email_Address = isemailrecievevalid.is_email_recieve_valid()
            Subject : str | int = input("Enter Your Subject : ")
            Message : str | int = input("Enter Your Message : ")
            Text = f"Subject:{Subject}\n\n{Message}"

            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()

            server.login(SEND_Email_Address,"dnil tcqz fhvg fkwy")

            server.sendmail(SEND_Email_Address, Receive_Email_Address , Text)

            logging.info("Email Send Successfully")

        except :
            raise ValueError("The email was not sent.")

emailnotification = EMAILNOTIFICATION()


class APPNOTIFICATION():
    def app_notification(self):

        root =tkinter.Tk()
        root.withdraw()

        messagebox.showerror("ERROR","This is the error message")
        messagebox.showwarning("Warning","This is the warning message")
        messagebox.showinfo("Information","This is the information")
        messagebox.askquestion("Question","This is the question")
        messagebox.askokcancel("AskOkCancel","This is the askokcancel")
        messagebox.askretrycancel("AskTryCancel","This is the askretrycancel")

        logging.info("Application Notification Successfully")

        root.destroy()

appnotification = APPNOTIFICATION()

class EXITNOTIFICATION:
    @staticmethod
    def exit_notification():
        logging.info("Notification Exit Succesfully....")
        print("Notification Exit Successfully....")

exitnotification = EXITNOTIFICATION()







