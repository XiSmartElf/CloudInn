from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.conf import settings
import json
import os
from Site.DataAccessLayer.PostsDataAccessLayer import PostsDataAccessLayer
# from django.http import JsonResponse


@require_http_methods(["GET"])
def post(request):
    postId = request.GET.get('id', None)
    abspath = os.path.join(settings.MEDIA_ROOT,'HTML','post.html')
    data = open(abspath).read()
    response = HttpResponse(content=data)
    return response

@require_http_methods(["GET"])
def getPostArticle(request, postId):
    postId = 1
    test = PostsDataAccessLayer()
    post = test.getPosts([postId])[str(postId)]
    data = json.dumps(post.__dict__)
    res = HttpResponse(data, status=200, content_type='application/json')
    return res
