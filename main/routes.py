from flask import render_template, request, redirect
from flask import current_app as app
import sqlite3
from sqlite3 import Error
from .dashboard import db


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        gender = request.form['gender']
        degree = request.form['degree']
        # Process the above values in conjunction with voter data
        # Insert data into database
        # connection = db.sqlConnect()
        # cursor = connection.cursor()
        # query = "INSERT INTO USERS VALUES (?, ?, ?, ?)"
        # data = (str(name), str(age), str(gender), str(degree))

        # cursor.execute(query, data)
        # connection.commit()
        # cursor.close()
        # After processing, take users to the dash app
        # This route is defined directly in Dash's initialization
        return redirect("/dash")
    else:
        return render_template('index.html')
