import smtplib
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#server = smtplib.SMTP()
server.login("mylanhackathon12345@gmail.com", "vybhav123")

#Send the mail
msg = "Hello!" # The /n separates the message from the headers
server.sendmail("mylanhackathon12345@gmail.com", "vybhavjain6@gmail.com", msg)
