import threading
import time
from Site.DataAccessLayer.PostsDataAccessLayer import PostsDataAccessLayer

class InMemCache:

    __postCollection = {}
    __postDal = PostsDataAccessLayer()

    @staticmethod
    def getOnePost(postId):
        if InMemCache.__postCollection.__contains__(postId):
            return InMemCache.__postCollection[str(postId)]
        else:
            #todo:add it to collection.
            return InMemCache.__postDal.getPosts([postId])[str(postId)]

    @staticmethod
    def getAllPosts():
        if InMemCache.__postCollection is not None:
            return InMemCache.__postCollection.items()
        else:
            InMemCache.__postCollection = InMemCache.__postDal.getPosts()
            return InMemCache.__postCollection.items()

    # ***** background sync related function **********
    @staticmethod
    def initBackgroundSycJobs():
        InMemCache.__startS3SycThread()

    @staticmethod
    def __S3SycJob():
        #todo: create merge method to do delta get only.
        InMemCache.__postCollection = InMemCache.__postDal.getPosts()
        time.sleep(60)

    @staticmethod
    def __startS3SycThread():
        S3SycThread = threading.Thread(name = 'backgroundSycJob', target = InMemCache.__S3SycJob())
        S3SycThread.setDaemon(True)
        S3SycThread.start()

