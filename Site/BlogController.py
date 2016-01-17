from flask import request,Response
from Site import app
from StaticServeController import serve_static
import json

@app.route('/',methods=['GET'])
def index():
    return serve_static("HTML/index.html")

@app.route('/getPostsOverview',methods=['GET'])
def getPostsOverview():
    postIds = request.values.getlist('id')
    postsOverview = []
    for postId in postIds:
        overview = postOverview(postId)
        postsOverview.append(overview.__dict__)

    data = json.dumps(postsOverview)
    res = Response(data, status=200, mimetype='application/json')
    res.headers['Access-Control-Allow-Origin'] = "*"
    return res

class postOverview:

    def __init__(self, postId):
        self.postId=postId
        self.postTitle="title"
        self.postDate ="10/20/2013"
        self.postDescription = "description"