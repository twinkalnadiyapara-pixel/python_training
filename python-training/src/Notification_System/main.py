import notification
print("===== Notification System=====")


print("1. Email")
print("2. SMS")
print("3. Application")
print("4. Exit")
while True :
    choice = int(input("Enter your notification choice : "))

    match choice:
        case 1:
            notification.emailnotification.email_notification()
        case 2:
            notification.smsnotification.sms_notification()
            print("SMS Notofication....")
        case 3:
            notification.appnotification.app_notification()
        case 4:
            notification.exitnotification.exit_notification()
            break
        case _:
            print("selected correct notification choice")