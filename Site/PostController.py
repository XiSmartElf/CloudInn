from flask import render_template
from flask import request
from flask import Response
from Site import app
import json

@app.route('/post',methods=['GET'])
def post():
    postId = request.args.get('id')
    return render_template("post.html")

@app.route('/postdata/<int:postId>', methods=['GET'])
def getPostArticle(postId):
    post = Test()
    data = json.dumps(post.__dict__)
    res = Response(data, status=200, mimetype='application/json')
    return res



class Test:
    static=88
    __private=99
    def __init__(self):
        self.id=1
        self.name="22"
        self.stuff="26"

        __this=1111
        hello=323
