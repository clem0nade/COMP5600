from flask import Flask, render_template, request

app = Flask(__name__, static_url_path="")

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        pass
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)