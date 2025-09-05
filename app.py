from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv # The python-dotenv package is required to load the environment variables
import os
import requests


load_dotenv() # This is how you can load the environment varibales in the file.

app = Flask(__name__)

@app.route("/")
def hello_world():
    # data = None
    # response = requests.get("http://www.omdbapi.com/?apikey=50571acc&" + "s=swades")
    # if response.status_code == 200:
    #     data = response.json()
    # return render_template('index.html', arr = data['Search'])
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

# Below is how you can send some form data to another page
# First you need to import request, redirect and url_for methods from flask
# Then you need to create a route to move the data into routes as done below

@app.route('/submit_data', methods=['POST'])
def submit_data():
    if request.method == 'POST':
        username = request.form['username']
        return redirect(url_for('display', username=username))
    
# the above code will intercept the data and redirect the user to a different page with the data

# Then the below code is used to render the display page with the the info grabbed from the source page
    
@app.route('/display')
def display():
    username = request.args.get('username')
    return render_template('display.html', username=username)



# Below is how you can run the app without typing the command: flask --app app run everytime

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

"""    
However this is an older way to run the code. The flask command is preferred for modern 
development. Therefore I have used flask command always.
"""

