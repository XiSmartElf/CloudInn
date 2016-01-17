from flask import render_template
from Site import app
from StaticServeController import serve_static


@app.route('/',methods=['GET'])
def index():
    return serve_static("HTML/index.html")


