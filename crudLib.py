from pymongo import MongoClient
import json
from jproperties import Properties
configs = Properties()
  
with open('config.properties', 'rb') as read_prop:
    configs.load(read_prop)
config = {
    "server" : "",
    "db" : "",
    "collection" : ""
}

config['server'] = str(configs.get("server").data) 
config['db'] = str(configs.get("db").data)
config['collection'] = str(configs.get("collection").data) 



def insertBlog(data):
    client = MongoClient(config['server'])
    db = client[config['db']]
    collection = db[config['collection']] 
    data["id"] = getID()
    collection.insert_one(data)
    print("Document inserted with ID:", data["_id"])

def getID():
    myclient = MongoClient(config['server'])
    mydb = myclient[config['db']]
    mycol = mydb[config['collection']]
    return len(list(mycol.find()))+1

def retrieveBlog(id):
    myclient = MongoClient(config['server'])
    mydb = myclient[config['db']]
    mycol = mydb[config['collection']]
    data = list(mycol.find())
    outputBlog = {}
    for x in data:
        if x['id'] == id:
            outputBlog = x
            break
    del outputBlog['_id']
    return outputBlog

def updateBlog(id, blog):
    myclient = MongoClient(config['server'])
    mydb = myclient[config['db']]
    mycol = mydb[config['collection']]
    data = list(mycol.find())
    myquery = { "id": id }
    newvalues = { "$set": { "blog": blog } }
    mycol.update_one(myquery, newvalues)

def deleteBlog(id):
    myclient = MongoClient(config['server'])
    mydb = myclient[config['db']]
    mycol = mydb[config['collection']]
    data = list(mycol.find())
    myquery = { "id": id }
    mycol.delete_one(myquery)

def listBlog():
    myclient = MongoClient(config['server'])
    mydb = myclient[config['db']]
    mycol = mydb[config['collection']]
    data = list(mycol.find())
    output = { "BLOGS" : []}
    for x in data:
        del x['_id']
        output["BLOGS"].append(x)
    return output

def updateComment(id, comment):
    myclient = MongoClient(config['server'])
    mydb = myclient[config['db']]
    mycol = mydb[config['collection']]
    data = list(mycol.find())
    op = {}
    for x in data:
        if x['id'] == int(id):
            op = x
    del op['_id']
    op['comment'].append(str(comment))
    myquery = { "id": int(id) }
    newvalues = { "$set": { "comment": op['comment'] } }
    mycol.update_one(myquery, newvalues)

def listComments(id):
    myclient = MongoClient(config['server'])
    mydb = myclient[config['db']]
    mycol = mydb[config['collection']]
    data = list(mycol.find())
    op = {}
    for x in data:
        if x['id'] == int(id):
            op = x
    del op['_id']
    commentOp = {'id' : int(id), 'comment' : []}
    commentOp['comment'] = op['comment']
    return commentOp


    

