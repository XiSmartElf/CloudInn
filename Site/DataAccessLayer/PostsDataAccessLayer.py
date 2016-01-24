import json
from S3DataRepository import S3DataRepository
from Site.DataModels.Post import Post

class PostsDataAccessLayer:
    bucket_name = "cloudinn"
    posts_folder = "posts"

    def __init__(self):
        self.postsDal = S3DataRepository()

    def getPosts(self, postIds = None):
        json_dict = {}
        if postIds is None:
            raw_Dict = self.postsDal.getRaw(PostsDataAccessLayer.bucket_name,
                                            PostsDataAccessLayer.posts_folder)
        else:
            filename_list = []
            for postId in postIds:
                filename_list.append(str(postId) + ".json")

            raw_Dict = self.postsDal.getRaw(PostsDataAccessLayer.bucket_name,
                                            PostsDataAccessLayer.posts_folder,
                                            filename_list)

        for key in raw_Dict.keys():
            json_dict[key[:-(len(".json"))]] = Post.constructFromJson(json.loads(raw_Dict[key]))

        print json_dict
        return json_dict

    def getAllPostNames(self):
        name_list = self.postsDal.getObjNames(PostsDataAccessLayer.bucket_name,
                                              PostsDataAccessLayer.posts_folder)
        id_list = []
        for name in name_list:
            id = int(name[:-(len(".json"))])
            id_list.append(id)

        print id_list
        return id_list


