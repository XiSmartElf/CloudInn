from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.conf import settings
import json
import os

@require_http_methods(["GET"])
def post(request):
    postId = request.GET.get('id', None)
    abspath = os.path.join(settings.MEDIA_ROOT,'HTML','post.html')
    data = open(abspath).read()
    response = HttpResponse(content=data)
    return response

@require_http_methods(["GET"])
def getPostArticle(request, postId):
    post = Test()
    data = json.dumps(post.__dict__)
    res = HttpResponse(data, status=200, content_type='application/json')
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