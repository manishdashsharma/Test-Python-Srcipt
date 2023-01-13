import mysql.connector
from ToMail import mail
# database connection
mydb = mysql.connector.connect(
  host="localhost",
  user="Manish",
  password="123456789",
  database="studentdatabase"
)
# connect to db
mycursor = mydb.cursor()
# query
mycursor.execute("SELECT * FROM student")
# get all the data
myresult = mycursor.fetchall()

# creating a blank list to leep the rows
DataforMail = []
for data in myresult:
  DataforMail.append(data)

# finding the row which has error
for i in range(len(DataforMail)):
    if DataforMail[i][2] == "Error":
        message = f"There some error {DataforMail[i][0]}"
        status = mail("Error Reported",["mdashsharma95@gmail.com"],message)
        print(status)