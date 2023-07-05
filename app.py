from flask import *
import json
import crudLib

app = Flask(__name__)

# payload : { 'heading' : 'test heading', 'blog' : 'test blog', 'comment' : [ 'comment1', 'comment2',... ]}
@app.route('/createBlog', methods = ['POST'])
def createBlog():
    if request.authorization and request.authorization.username == 'admin' and request.authorization.password == 'admin':
        apiOutput = {}
        input_json = request.get_json(force=True)
        data = input_json
        crudLib.insertBlog(data)
        return { "message" : "BLOG CREATED" }
    return make_response('Unauthorized', 401, { "message" : "Authorization Required" })

# payload : no payload. only need to pass id of the blog
@app.route('/retrieveBlog', methods = ['GET'])
def retrieveBlog():
    if request.authorization and request.authorization.username == 'admin' and request.authorization.password == 'admin':
        id = request.args.get('id')
        return crudLib.retrieveBlog(int(id))
    return make_response('Unauthorized', 401, { "message" : "Authorization Required" })

# payload : { 'id' : 'testID', 'updated_blog' : 'test blog', 'comment' : [ 'comment1', 'comment2',... ]}
@app.route("/updateBlog", methods = ["PUT"])
def updateBlog():
    if request.authorization and request.authorization.username == 'admin' and request.authorization.password == 'admin':
        input_json = request.get_json(force=True)
        id = input_json['id']
        blog = input_json['blog']
        crudLib.updateBlog(int(id), str(blog))
        return crudLib.retrieveBlog(int(id))
    return make_response('Unauthorized', 401, { "message" : "Authorization Required" })

# payload : no payload. only need to pass id of the blog
@app.route("/deleteBlog", methods = ['DELETE'])
def deleteBlog():
    if request.authorization and request.authorization.username == 'admin' and request.authorization.password == 'admin':
        id = request.args.get('id')
        crudLib.deleteBlog(int(id))
        return { "message" : str(id) + " No. BLOG DELETED" }
    return make_response('Unauthorized', 401, { "message" : "Authorization Required" })
    

# payload : no payload. only need to pass id of the blog
@app.route("/listBlogs", methods = ['GET'])
def listBlogs():
    if request.authorization and request.authorization.username == 'admin' and request.authorization.password == 'admin':
       return crudLib.listBlog()
    return make_response('Unauthorized', 401, { "message" : "Authorization Required" })
    

# payload : { 'id' : 'test id', 'comment' : 'test comment' }
@app.route("/addComment", methods = ['POST'])
def addComment():
    if request.authorization and request.authorization.username == 'admin' and request.authorization.password == 'admin':
        input_json = request.get_json(force=True)
        id = input_json['id']
        comment = input_json['comment']
        crudLib.updateComment(int(id), str(comment))
        return { 'message' : "COMMENT ADDED" }
    return make_response('Unauthorized', 401, { "message" : "Authorization Required" })


# payload : no payload. only need to pass id of the blog
@app.route("/listComments", methods = ['GET'])
def listComments():
    if request.authorization and request.authorization.username == 'admin' and request.authorization.password == 'admin':
        id = request.args.get('id')
        return crudLib.listComments(int(id))
    return make_response('Unauthorized', 401, { "message" : "Authorization Required" })


app.run(debug=True)
