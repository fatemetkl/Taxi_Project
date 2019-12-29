from flask import Flask, render_template, request
import pyodbc
app = Flask(__name__)

conn = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=DESKTOP-696VHCV;"
    "Database=taxii;"
    "Trusted_Connection=yes;"
)
# def read(conn):
#     print("Read")
#     cursor = conn.cursor()
#     cursor.execute("select * from dummy")
#     for row in cursor:
#         print(f'row = {row}')
#     print()
#
# def create(conn):
#     print("Create")
#     cursor = conn.cursor()
#     cursor.execute(
#         'insert into dummy(a,b) values(?,?);',
#         (3232, 'catzzz')
#     )
#     conn.commit()
#     read(conn)

@app.route('/')
def home():
    return render_template('/TaxiiHome/TaxiiHome.html')
@app.route('/Signinpass')
def passSignIn():
    return render_template('/SignInPass/Signinpass.html')
@app.route('/SignInDriver')
def drverSignIn():
    return render_template('signupDriver/SigniInDriver.html')

@app.route('/DriverLogin')
def Driverlogin():
    return render_template('DriverLogIn/DriverLogin.html')

@app.route('/passLogIn')
def PassLogIn():
    return render_template('passLogIn/passLogIn.html')



if __name__ == '__main__':
    app.run()
