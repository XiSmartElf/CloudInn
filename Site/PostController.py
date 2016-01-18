from flask import  request, Response
from Site import app
import json
from StaticServeController import serve_static


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

class Test:
    static=2
    __private=99
    def __init__(self):
        self.id=1
        self.text="22"
        self.title="26"
        self.date = "10/"+str(Test.static)+"/2016"
        Test.static+=1

        __this=1111
        hello=323