import cgi
import cgitb
import mysql.connector
import sys

cgitb.enable()

try:
    conn = mysql.connector.connect(host='localhost', user='root', password='root', database='form_db')
    cursor = conn.cursor()

    form = cgi.FieldStorage(environ={'REQUEST_METHOD': 'POST'})
    option = form.getvalue("SelectPartner")
    name = form.getvalue("name")
    email = form.getvalue("email")
    number = form.getvalue("number")
    pan = form.getvalue("pan")
    pincode = form.getvalue("pincode")
    kyc = form.getvalue("kyc") 
    file = form.getvalue("file") 
    password = form.getvalue("password")

    query = "INSERT INTO form (Partner, Name, Email, Number, Pan, PinCode, KYC, Password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    values = (option, name, email, number, pan, pincode, kyc, file, password)  
    cursor.execute(query, values)

    conn.commit()

except mysql.connector.Error as error:
    print("Failed to insert into MySQL table {}".format(error))

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
