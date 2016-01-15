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