from Site import app, dynamo

@app.route('/create_post')
def create_post():
    with app.app_context():
           dynamo.create_all()

    dynamo.testPost.put_item(data={
         'postId': 'firstpost',
         'author_name': 'xi',
         'body': 'lalalaldes',
    })

    with app.app_context():
         for table_name, table in dynamo.tables.iteritems():
            print table_name, table