from flask import render_template, request, redirect
from flask import current_app as app
import pyodbc


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']
        degree = request.form['degree']
        # Process the above values in conjunction with voter data
        server = 'tcp:comp5600.database.windows.net'
        database = 'UserData'
        username = '16-CAM'
        password = 'COMP5600Database'
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                              server+';DATABASE='+database+';UID='+username+';PWD=' + password)
        curs = conn.cursor()
        sql = "INSERT INTO Users Values (?, ?, ?, ?)"
        values = (name, age, gender, degree)
        curs.execute(sql, values)
        conn.commit()
        curs.close()
        conn.close()
        # After processing, take users to the dash app
        # This route is defined directly in Dash's initialization
        return redirect("/cluster")
    else:
        return render_template('index.html')
