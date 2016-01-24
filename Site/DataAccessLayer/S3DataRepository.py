from boto3.session import Session
from botocore.client import ClientError

class S3DataRepository:

    __access_key = 'AKIAIXLQOAPSWCA6ISEA'
    __secret_key = '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'

    def __createSession(self):
        session = Session(aws_access_key_id=S3DataRepository.__access_key,
                  aws_secret_access_key=S3DataRepository.__secret_key
                  )
        s3 = session.resource('s3')
        return s3

    def getRaw(self,bucket,folder, filename_list=None):
        s3 = self.__createSession()
        bucket = s3.Bucket(bucket)
        raw_list = {}
        if filename_list is not None:
            for filename in filename_list:
                raw = bucket.Object(folder+"/"+filename).get()['Body'].read()
                raw_list[filename] = raw
        else:
            objects = bucket.objects.filter(Prefix=folder+'/')
            for object in objects:
                if object.key != (folder+"/"):
                    raw_list[str(object.key)[len(folder+"/"):]] = object.get()['Body'].read()

        return raw_list

    def getObjNames(self,bucket,folder):
        s3 = self.__createSession()
        bucket = s3.Bucket(bucket)
        objects = bucket.objects.filter(Prefix=folder+'/')
        raw_list = []
        for object in objects:
            if object.key != (folder+"/"):
                raw_list.append(str(object.key)[len(folder+"/"):])

        return raw_list

    # def uploadObj(self,bucket,filename):
    #     s3client = boto3.client('s3')
    #     for key in s3client.list_objects(Bucket=bucket)['posts/schema.json']:
    #         print key

    def exsit(self):
        s3 = self.__createSession()
        try:
            s3.Object('my-bucket', 'dootdoot.jpg').load()
        except ClientError as e:
            if e.response['Error']['Code'] == "404":
                exists = False
            else:
                raise e
        else:
            exists = True

        print exists
