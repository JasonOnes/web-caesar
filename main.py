from flask import Flask, request 
from caesar import rotate_string
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True 

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form  {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
    <!-- this is where form goes -->
    <form  action="" method="POST">
        <label>Rotate by
        <input type="text" name="rot" />
        </label>
        <textarea name="text">
            
            </textarea>
        <input type="Submit" />
    </body>
</html>
"""

@app.route('/')
def index():
    return form 

@app.route('/', methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    text = cgi.escape(request.form['text'])
    return "<h1>{0}</h1>".format(rotate_string(text, rot))
    
app.run()
