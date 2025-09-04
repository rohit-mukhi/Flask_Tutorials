from flask import Flask, render_template
from dotenv import load_dotenv # The python-dotenv package is required to load the environment variables
import os

load_dotenv() # This is how you can load the environment varibales in the file.

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

# Below is how you can run the app without typing the command: flask --app app run everytime

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

"""    
However this is an older way to run the code. The flask command is preferred for modern 
development. Therefore I have used flask command always.
"""

