from flask import send_from_directory
from Site import app
import os

@app.route('/Content/<path:dir>')
def serve_static(dir):
    tokens = dir.split("/");
    contentType = tokens[0];
    filename = tokens[1];
    completePath = os.path.join(os.getcwd(),"Content",contentType)
    res= send_from_directory(completePath, filename)
    return res