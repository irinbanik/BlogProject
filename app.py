from flask import *
import json
import crudLib

app = Flask(__name__)

# payload : { 'heading' : 'test heading', 'blog' : 'test blog', 'comment' : [ 'comment1', 'comment2',... ]}
@app.route('/createBlog', methods = ['POST'])
def createBlog():
    apiOutput = {}
    input_json = request.get_json(force=True)
    data = input_json
    crudLib.insertBlog(data)
    return { "message" : "BLOG CREATED" }

# payload : no payload. only need to pass id of the blog
@app.route('/retrieveBlog', methods = ['GET'])
def retrieveBlog():
    id = request.args.get('id')
    return crudLib.retrieveBlog(int(id))

# payload : { 'id' : 'testID', 'updated_blog' : 'test blog', 'comment' : [ 'comment1', 'comment2',... ]}
@app.route("/updateBlog", methods = ["PUT"])
def updateBlog():
    input_json = request.get_json(force=True)
    id = input_json['id']
    blog = input_json['blog']
    crudLib.updateBlog(int(id), str(blog))
    return crudLib.retrieveBlog(int(id))

# payload : no payload. only need to pass id of the blog
@app.route("/deleteBlog", methods = ['DELETE'])
def deleteBlog():
    id = request.args.get('id')
    crudLib.deleteBlog(int(id))
    return { "message" : str(id) + " No. BLOG DELETED" }

# payload : no payload. only need to pass id of the blog
@app.route("/listBlogs", methods = ['GET'])
def listBlogs():
    return crudLib.listBlog()

# payload : { 'id' : 'test id', 'comment' : 'test comment' }
@app.route("/addComment", methods = ['POST'])
def addComment():
    input_json = request.get_json(force=True)
    id = input_json['id']
    comment = input_json['comment']
    crudLib.updateComment(int(id), str(comment))
    return { 'message' : "COMMENT ADDED" }

# payload : no payload. only need to pass id of the blog
@app.route("/listComments", methods = ['GET'])
def listComments():
    id = request.args.get('id')
    return crudLib.listComments(int(id))

app.run(debug=True)