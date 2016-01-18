from flask import request,Response
from Site import app
from StaticServeController import serve_static
import json

@app.route('/',methods=['GET'])
def index():
    return serve_static("HTML/index.html")

@app.route('/getPostsOverviewBeforeDate',methods=['GET'])
def getPostsOverviewBeforeDate():
    #postIds = request.values.getlist('id')
    date = request.args.get('date')
    numOfPost = int(request.args.get('numOfPost'))
    if numOfPost > 10 or numOfPost<=0 or date == 'undefined':
        return Response(
                json.dumps(
                {"error":"Please query between 1 to 10 posts; Please specify a date"}),
                status=400,
                mimetype='application/json')

    postsSinceDate  = [postOverview(1),postOverview(2)]
    postsOverview = []
    for post in postsSinceDate:
        postsOverview.append(post.__dict__)

    data = json.dumps(postsOverview)
    res = Response(data, status=200, mimetype='application/json')
    res.headers['Access-Control-Allow-Origin'] = "*"
    return res

class postOverview:
    static = 30;
    staticId = 1;
    def __init__(self, postId):
        self.postId=postOverview.staticId
        self.postTitle="title"
        self.postDate ="10/"+str(postOverview.static)+"/2013"
        postOverview.static-=1
        postOverview.staticId +=1;
        self.postDescription = "description"