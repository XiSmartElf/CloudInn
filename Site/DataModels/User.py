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