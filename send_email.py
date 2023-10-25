import smtplib
my_email = "myemail@example.org"
password = "mysecretpassword"

connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user=my_email, password=password)

connection.sendmail(from_addr=my_email, to_addrs="receipentemail@gmail.com", msg="Hello World")

connection.close()