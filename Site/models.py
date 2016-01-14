from Site import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=True)
    posts = db.relationship('Post', backref = 'author', lazy = 'dynamic')
    comments = db.relationship('Comment', backref='author', lazy='dynamic')

    def __init__(self, nickname, email):
        self.nickname = nickname
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.nickname)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3



class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, body):
        self.body = body

    def __repr__(self):
        return '<Comment %r>' % (self.body)



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



