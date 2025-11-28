import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

print("------ PYTHON EMAIL SENDER ------")

sender_email = input("Enter your Gmail address: ")
app_password = input("Enter your App Password: ")
receiver_email = input("Enter receiver email: ")
subject = input("Enter subject: ")
message_body = input("Enter message body: ")

# Create message
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = subject

msg.attach(MIMEText(message_body, "plain"))

try:
    # Gmail SMTP server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    # Login using App Password
    server.login(sender_email, yqoq jglm senq tffp)

    # Send email
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()

    print("\nEmail sent successfully!")

except Exception as e:
    print("Error:", str(e))
