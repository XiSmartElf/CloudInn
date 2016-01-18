from Site import db

class Post(db.Model):
    __tablename__ = 'posts'
    postId = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(140), nullable = False)
    authorId = db.Column(db.Integer, db.ForeignKey('user.id'))
    timestamp = db.Column(db.DateTime)
    url = db.Column(db.String(140), nullable = False)

    def __init__(self, title, author, url):
        self.title = title
        self.author = author
        self.url = url

    def __repr__(self):
        return '<Post %r>' % (self.postId)