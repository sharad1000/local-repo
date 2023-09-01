import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time

# Email configuration
sender_email = "sharad.baghel100@gmail.com"
sender_password = "s2742974"
recipient_email = "sharad.baghel50@gmail.com"
subject = "Daily Report"
message = "automation"

# Read the daily report content from a file
with open("daily_report.txt", "r") as report_file:
    message = report_file.read()

def send_daily_report():
    try:
        # Set up the SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)

        # Create the email message
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = recipient_email
        msg["Subject"] = subject
        msg.attach(MIMEText(message, "plain"))

        # Send the email
        server.sendmail(sender_email, recipient_email, msg.as_string())
        print("Daily report sent successfully!")

        # Close the SMTP server
        server.quit()

    except Exception as e:
        print(f"Error: {str(e)}")

# Schedule the script to run daily at a specific time (e.g., 8:00 AM)
schedule.every().day.at("08:00").do(send_daily_report)

while True:
    schedule.run_pending()
    time.sleep(1)
