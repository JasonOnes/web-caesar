"""A basic webapp to encrypt given message with caesar cipher. Bare bones, no validation, meets
requirements, no more no less."""

from flask import Flask, request, redirect
from caesar import rotate_string

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
        <label>Rotate by:
        <input type="text" name="rot" />
        </label>
        <textarea name="text">{}</textarea>
        <input type="Submit" />
    </body>
</html>
"""

@app.route('/')
def index():
    return form.format("") 

@app.route('/', methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    text = request.form['text']
    if rot and text:
        return form.format(rotate_string(text, rot))
    if rot == 0:
        return form.format(text, '')

app.run()