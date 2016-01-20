
class InMemCach:

    #thread : update SQL every 1min,
    def __init__(self):
        self.s3UrlMapping = {} # key: postId, value:url string
        self.postMapping = {} # key: postId, value: postObject {url,  (content related)}
        self.s3UrlLastSyncTime = '' #date
        #thread.run(deltaSyncJob, 60*1000 milisecs)

    def syncAllS3UrlsFromSql(self):
        #sql do the work get data. get me all since last modifed time.
        #merge with s3UrlMapping
        #self.s3UrlLastSyncTime = now
        return


    def syncAllPostsFromS3(self):
        #foreach(key ins3UrlMapping.keySets),
        # syncOnePostFromS3
        return

    def getOnePostFromS3(self, postId, url):
        # !postMapping.contains(key) || postMapping[key].url!=s3UrlMapping[key]
        # fetch()==> http GET url...> content.(do file read work)=> save to post object
        # postobject. text = content. postobject.url=s3urlmapping[key]
        # postMapping[key] = postobject
        return

    def getOneUrlFromSql(self, postId):
        #get url from sql with postid key.
        #update s3UrlMapping=> s3UrlMapping[postId] =url fetched.
        return

    def deltaSyncJob(self):
        #syncS3UrlsFromSql
        #syncAllPostsFromS3
        return

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

