from flask import Flask, render_template


app = Flask(__name__, static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/createNewEvent')
def create_New_Event():
    return render_template('layout2.html')

if __name__ == '__main__':
    app.run(debug=True)
