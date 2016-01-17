from flask import render_template, request, Response,send_from_directory
from Site import app
import json
import os

@app.route('/post',methods=['GET'])
def post():
    postId = request.args.get('id')
    return serve_static("HTML/post.html")

@app.route('/postdata/<int:postId>', methods=['GET'])
def getPostArticle(postId):
    post = Test()
    data = json.dumps(post.__dict__)
    res = Response(data, status=200, mimetype='application/json')
    res.headers['Access-Control-Allow-Origin'] = "*"
    return res

@app.route('/Content/<path:dir>')
def serve_static(dir):
    root_dir = os.path.dirname(os.getcwd())+"\CloudInn\Site\\templates\\"
    tokens = dir.split("/");
    contentType = tokens[0];
    filename = tokens[1];
    res= send_from_directory(os.path.join(root_dir, 'Content', contentType), filename)
    return res

class Test:
    static=88
    __private=99
    def __init__(self):
        self.id=1
        self.text="22"
        self.title="26"
        self.date = "10/2/2016"

        __this=1111
        hello=323
