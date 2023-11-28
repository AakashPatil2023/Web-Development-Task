import cgi
import mysql.connector

try:
    conn = mysql.connector.connect(host='localhost', username='root', password='root', database='form_db')
    cursor = conn.cursor()

    form = cgi.FieldStorage()
    option = form['SelectPartner'].value
    name = form['name'].value
    email = form['email'].value
    number = form['number'].value
    pan = form['pan'].value
    pincode = form['pincode'].value
    kyc = form['kyc'].value
    file = form['file']
    password = form['password'].value

    query = "INSERT INTO form (Partner, Name, Email, Number, Pan, PinCode, KYC, file, password) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    values = (option, name, email, number, pan, pincode, kyc, file.value, password)

    cursor.execute(query, values)

    conn.commit()

except mysql.connector.Error as error:
    print("Failed to insert into MySQL table {}".format(error))

finally:
    if (conn).is_connected():
        cursor.close()
        conn.close()
