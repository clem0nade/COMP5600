from flask import render_template, request, redirect
from flask import current_app as app

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        gender = request.form['gender']
        degree = request.form['degree']
        # Process the above values in conjunction with voter data

        # After processing, take users to the dash app
        # This route is defined directly in Dash's initialization
        return redirect("/cluster")
    else:
        return render_template('index.html')