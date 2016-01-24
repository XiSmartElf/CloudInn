from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.conf import settings
import json
import os
from Site.InMemCache import InMemCache

@require_http_methods(["GET"])
def getBlogPage(request):
    abspath = os.path.join(settings.MEDIA_ROOT,'HTML','index.html')
    data = open(abspath).read()
    response = HttpResponse(content=data)
    return response

@require_http_methods(["GET"])
def getPostsOverviewBeforeDate(request):
    date = request.GET.get('date', None)
    numOfPost = int(request.GET.get('numOfPost',1))
    if numOfPost > 10 or numOfPost<=0 or date is None:
        return HttpResponse(
                json.dumps(
                {"error":"Please query between 1 to 10 posts; Please specify a date"}),
                status=400,
                content_type="application/json")

    postsSinceDate  = InMemCache.getAllPosts()
    if len(postsSinceDate)==0:
        return HttpResponse(json.dumps(''),
                            status=404,
                            content_type="application/json")

    #Convert result to JSON.
    postsOverview = []
    for post in postsSinceDate:
        postsOverview.append(post.getPostOverview().__dict__)

    data = json.dumps(postsOverview)
    res = HttpResponse(data,
                       status=200,
                       content_type="application/json")
    return res

