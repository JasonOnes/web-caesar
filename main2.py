from flask import Flask, request, redirect, render_template
from caesar import rotate_string
import cgi
from time import sleep

app = Flask(__name__)
app.config['DEBUG'] = True 


@app.route('/')
def index():
    return render_template('rot_form.html', declarative="Rotate by")

@app.route('/', methods=['POST'])
def encrypt():
    try:
        rot = int(request.form['rot'])
        text = request.form['text']
        if rot and text:
            return render_template('rot_form.html', message=rotate_string(text, rot))
    except ValueError:
        return render_template('rot_form.html', declarative="Enter a value", 
                               message=request.form['text'])

@app.route('/error', methods=['POST'])
def error():
    return render_template('rot_form.html', declarative="Enter a value!")
    
app.run()
