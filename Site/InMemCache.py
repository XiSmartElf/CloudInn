import threading
import time
from Model import Post

class InMemCach:

    #thread : update SQL every 1min,
    def __init__(self):
        self.__s3UrlMapping = {} # key: postId, value:url string
        self.__postMapping = {} # key: postId, value: postObject {url,  (content related)}
        self.__s3UrlLastSyncTime = '00/00/0000 00:00:00' #date
        self.initBackgroundSycJob() #thread.run(deltaSyncJob, 60*1000 milisecs)

    # sync url from Sql related function

    def syncAllS3UrlsFromSql(self):
        #sql do the work get data. get me all since last modifed time.
        #merge with s3UrlMapping
        #self.s3UrlLastSyncTime = now
        return

    def getOneUrlFromSql(self, postId):
        #get url from sql with postid key.
        #update s3UrlMapping=> s3UrlMapping[postId] =url fetched.
        return


    # get posts from S3 related function

    def syncAllPostsFromS3(self):
        for key in self.__s3UrlMapping:
            self.getOnePostFromS3(key, self.__s3UrlMapping[key])
        return

    def getOnePostFromS3(self, postId, post):
        #postMapping contains postId
        if self.__postMapping.__contains__(postId):
            # url is not up-to-date
            if self.__postMapping[postId] != post.url:
                self.__s3UrlMapping[postId].url = self.__postMapping[postId]
            self.fetchPostFromS3(self.__s3UrlMapping[postId])
        #postMapping doesn't contain postId, e.g: database delete the url and update to postMapping
        else:
            return

    def fetchPostFromS3(self, post):

        return


    # background sync related function

    def initBackgroundSycJob(self):
        self.startBackgroundSycThread()

    def deltaSyncJob(self):
        #syncS3UrlsFromSql
        #syncAllPostsFromS3
        return

    def backgroundSycJob(self):
        self.deltaSyncJob()
        time.sleep(60)
        self.deltaSyncJob()

    def startBackgroundSycThread(self):
        backgroundSycThread = threading.Thread(name = 'backgroundSycJob', target = self.backgroundSycJob())
        backgroundSycThread.setDaemon(True)
        backgroundSycThread.start()


    # user get post related function

    def getPost(self,postId):
        if self.postMapping[postId] is not None:
            return self.postMapping[postId]
        else:
            if self.s3UrlMapping[postId] is not None:
                url = self.s3UrlMapping[postId]
                self.getOnePostFromS3(url)
                return self.postMapping[postId]
            else:
                url = self.getOneUrlFromSql(postId)
                self.getOnePostFromS3(postId,url)

