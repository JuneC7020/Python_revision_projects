import smtplib, ssl

port = 465  # For SSL
sender_email = input("Enter your email address: ")
password = input("Enter your password: ")
receiver_emails = []
while True:
    r_email = input("Enter the email address of the receiver: ")
    message = """\
        Subject: Hi there
        
        This message is sent from Python."""
    print("This is the message: ", message)
    receiver_emails.append(r_email)
    more = input("Is there more receiver?(y/n): ")
    if more =="y" or more == "Y":
        continue
    else:
        break
    
context = ssl.create_default_context()


smtp_server = "smtp.gmail.com"
# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    for r in receiver_emails:
        server.sendmail(sender_email, r, message)
