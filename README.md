Stock Monitoring and Alert System for Manufacturing Supplies
A backend automation system that monitors manufacturing supply inventory stored in DynamoDB and sends real-time email alerts when stock falls below the minimum threshold. Built using AWS Lambda, CloudWatch, and Gmail SMTP for notifications.

Team Members
3 people

My Role
I was the team lead and backend automation developer for this project.

Designed the DynamoDB table to store item details such as name, quantity, and minimum threshold.

Developed the Lambda function to automate stock checks.

Configured CloudWatch Events to schedule periodic execution.

Integrated Gmail SMTP using Python’s smtplib to send alert emails.

Ensured alert messages were formatted clearly and triggered only when necessary.

Project Overview
Inventory items (e.g., lubricants, paints, machine parts) are stored in a DynamoDB table.

A scheduled Lambda function scans this table for items whose quantity has dropped below the defined threshold.

When such items are found, the function sends an email alert to the concerned personnel.

The system records the timestamp of alerts to avoid repeated notifications for the same item.

Why This Project Was Done
Manual stock checking on the factory floor caused delays and errors. This project aimed to automate the process and reduce confusion in restocking.
It also provided an opportunity to use AWS services in a real-world scenario and develop cloud automation skills.

Results
Delivered a working system that monitors inventory and sends timely alerts.

Reduced the need for manual verification and enabled faster restocking.

Improved workflow efficiency and minimized material-related delays.

The system is lightweight, scalable, and adaptable for other inventory tracking scenarios.

Problems Faced
Configuring Gmail SMTP securely and avoiding blocks or spam filters.

Handling multiple item alerts in one execution without overwhelming the recipients.

Formatting email content for clarity and professionalism.
