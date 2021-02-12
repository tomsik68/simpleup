from flask import Flask, redirect, request
from uuid import uuid4
import string

app = Flask(__name__)

UPLOAD_FORM='''
<form action="/upload" method="post" enctype="multipart/form-data">
<input type="text" name="filename">
<input type="file" name="file">
<input type="submit" value="Upload">
</form>
'''

ALLOWED = string.ascii_letters + string.digits

def filter_fun(char):
    global ALLOWED
    return char in ALLOWED

@app.route('/')
def index():
    global UPLOAD_FORM
    return UPLOAD_FORM

@app.route('/upload', methods=['POST'])
def upload():
    f = request.files['file']
    fname = request.form['fname']
    fname = str(filter(filter_fun, fname))
    if fname == '':
        fname = str(uuid4())
    print('save ' + fname)
    f.save(fname)
    return index()
