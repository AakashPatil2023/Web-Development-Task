import cgi
import mysql.connector

try:
    conn = mysql.connector.connect(host='localhost', username='root', password='root', database='form_db')
    cursor = conn.cursor()

    form = cgi.FieldStorage()
    option = form.getvalue("SelectPartner")
    name = form.getvalue("name")
    email = form.getvalue("email")
    number = form.getvalue("number")
    pan = form.getvalue("pan")
    pincode = form.getvalue("pincode")
    kyc = form.getvalue("Skyc")
    file = form.getvalue("file")
    password = form.getvalue("password")

    query = "INSERT INTO form (Partner, Name, Email, Number, Pan, PinCode, KYC, file, password) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    values = (option, name, email, number, pan, pincode, kyc, file, password)

    cursor.execute(query, values)

    conn.commit()

except mysql.connector.Error as error:
    print("Failed to insert into MySQL table {}".format(error))

finally:
    if (conn).is_connected():
        cursor.close()
        conn.close()
