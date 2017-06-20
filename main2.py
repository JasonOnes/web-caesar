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
        <label>{}
        <input type="number" name="rot" />
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
    return form.format("Rotate by:", "") 

@app.route('/', methods=['POST'])
def encrypt():
    try:
        rot = int(request.form['rot'])
        text = cgi.escape(request.form['text'])
        if rot and text:
            return form.format("Rotated By", rotate_string(text, rot))
    except ValueError:
        # if not text:
        #     return redirect('/')
        # elif not rot:
        return redirect('/error')
        """ redirect to index with .format modifying tag of input to error message?"""

@app.route('/error')
def error():
    return form.format("Enter a value!", "")

@app.route('/', methods=['POST'])
def reroute():
    return redirect('/')

    
app.run()
