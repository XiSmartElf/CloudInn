class Post:

    def __init__(self, title,date,author,content,description,coverImg, postId=None):
        if postId is not None:
            self.postId = postId

        self.title = title
        self.date = date
        self.author = author
        self.content = content
        self.description = description
        self.coverImg = coverImg
        #todo:add auto-increment post id when creation.

    @staticmethod
    def constructFromJson(json):
        post = Post(
            postId = int(json['postId']),
            title = json['title'],
            date = json['date'],
            author = json['author'],
            content = json['content'],
            description = json['description'],
            coverImg = json['coverImg'],
        )
        #todo: @bug handle key doesn't contain possibilities. validate json from s3.
        # post.s3_raw_json = json
        return post

    #define two static vars for mocking id and date.
    static = 30
    staticId = 1
    def getPostOverview(self):
        postOverview = {}
        postOverview['postId']=Post.staticId
        postOverview['postTitle'] = self.title
        postOverview['postDate'] ="10/"+str(Post.static)+"/2013"
        Post.static-=1
        Post.staticId +=1
        postOverview['postDescription'] = self.description
        postOverview['coverImg'] = self.coverImg
        return postOverview
