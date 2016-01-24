from threading import Thread
import thread
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

    def getAllPosts(self):
        if self.__postCollection is not None:
            return self.__postCollection.values()
        else:
            self.__postCollection = self.__postDal.getPosts()
            return self.__postCollection.values()

    # ***** background sync related function **********
    # def initBackgroundSycJobs(self):
    #     self.__startS3SycThread()

    def __S3SycJob(self):
        #todo: create merge method to do delta get only.
        self.__postCollection = self.__postDal.getPosts()


    # def __startS3SycThread(self):
    #     S3SycThread = Thread(name = 'backgroundSycJob', target = InMemCache.__S3SycJob())
    #     S3SycThread.setDaemon(True)
    #     S3SycThread.start()

    def run(self):
        while True:
            self.__S3SycJob()
            print 'Sync one time.'
            time.sleep(60)
