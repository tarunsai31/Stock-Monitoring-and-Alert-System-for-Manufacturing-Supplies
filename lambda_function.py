import json
import boto3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket = 'aws-project-inventory-bucket'
    key = 'inventory.json'

    sender_email = "tarunsai2124@gmail.com"
    sender_password = "abc123xyz@lambda"
    receiver_email = "factoryalerts2025@gmail.com"

    response = s3.get_object(Bucket=bucket, Key=key)
    inventory = json.loads(response['Body'].read().decode('utf-8'))

    alerts = []
    for item in inventory:
        if item['quantity'] < 10:
            alerts.append(f"- {item['name']} (ID: {item['product_id']}): Only {item['quantity']} left")

    if alerts:
        subject = "Stock Alert: Low Inventory Items"
        body = "The following manufacturing supplies are running low:\n\n" + "\n".join(alerts)

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            server.quit()
        except Exception as e:
            return {
                'statusCode': 500,
                'body': json.dumps(f"Email failed: {str(e)}")
            }

    return {
        'statusCode': 200,
        'body': json.dumps('Inventory checked and alerts sent if needed.')
    }
