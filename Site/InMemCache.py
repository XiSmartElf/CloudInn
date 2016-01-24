from threading import Thread
import time
from Site.DataAccessLayer.PostsDataAccessLayer import PostsDataAccessLayer

class InMemCache(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.__postCollection = {}
        self.__postDal = PostsDataAccessLayer()

    def getOnePost(self,postId):
        if self.__postCollection.__contains__(postId):
            return self.__postCollection[str(postId)]
        else:
            post =  self.__postDal.getPosts([postId])[str(postId)]
            self.__postCollection[str(postId)]=post
            return post

    #tempory method to deal with blog post overview.
    def getAllPosts(self):
        if self.__postCollection is not None:
            return self.__postCollection.values()
        else:
            self.__postCollection = self.__postDal.getPosts()
            return self.__postCollection.values()

    def __S3SycJob(self):
        #todo: create merge method to do delta get only.
        self.__postCollection = self.__postDal.getPosts()

    def run(self):
        while True:
            self.__S3SycJob()
            print 'Sync one time.'
            time.sleep(60)
