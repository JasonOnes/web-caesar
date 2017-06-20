from flask import Flask, request, redirect
from caesar import rotate_string
import cgi
from time import sleep

app = Flask(__name__)
app.config['DEBUG'] = True 

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form  {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
    <form  action="" method="POST">
        <label>Rotate by(enter a whole number)
        <input type="text" name="rot" />
        </label>
        <textarea name="text">
            {}
            </textarea>
        <input type="Submit" />
    </body>
</html>
"""

@app.route('/')
def index():
    return form.format("") 

@app.route('/', methods=['POST'])
def encrypt():
    try:
        rot = int(request.form['rot'])
        text = cgi.escape(request.form['text'])
        if rot and text:
            return form.format(rotate_string(text, rot))
    except ValueError:
        return redirect('/error')
        """ redirect to index with .format modifying tag of input to error message?"""

@app.route('/error', methods=['POST'])
def error():
    "<h1>a numeric rot value must be entered</h1>"
    
    #sleep(5)
    #return redirect('/')
    return form.format(label="Need to put numeric value for rot", tarea="")

    
app.run()
