class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(140), nullable = False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    timestamp = db.Column(db.DateTime)
    body = db.Column(db.String(140))

    def __init__(self, title, author, body):
        self.title = title
        self.author = author
        self.body = body

    def __repr__(self):
        return '<Post %r>' % (self.body)