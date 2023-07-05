# Blog Project

This is a blog post project which uses RESTful APIs in order to perform a number of task for blog post.

For this project MongoDB is used in order to handle complex JSON structure
<br><br>

## How to use APIs?
---
For using the APIs, basic authentication needs to be passed.
<br>
**Credentials**
<br>
Username : admin
<br>
Password : admin
<br>

This utility is able to perform the following tasks:
<br><br>
**/createBlog** : Creates blog post
<br>
```
METHOD : POST

Payload : 
{ 'heading' : 'test heading', 'blog' : 'test blog', 'comment' : [ 'comment1', 'comment2' ]}
```

<br>

**/retrieveBlog** : Fetches blog posts with the help of ID
<br>
```
METHOD : GET

Payload : 
No payload required. Only ID value needs to passed in with the endpoint

Example : http://localhost:5000/retrieveBlog?id=56
```

<br>

**/updateBlog** : Updates blog post with the help of ID
<br>
```
METHOD : PUT

Payload : 
{ 'id' : 'testID', 'updated_blog' : 'test blog', 'comment' : [ 'comment1', 'comment2' ]}
```

<br>

**/deleteBlog** : Deletes a blog with the help of ID
<br>
```
METHOD : DELETE

Payload : 
No payload required. Only ID value needs to passed in with the endpoint

Example : http://localhost:5000/deleteBlog?id=56
```

<br>

**/listBlogs** : List sall blog posts
<br>
```
METHOD : GET

Payload : 
No payload required. Only endpoint is able to fetch all blogs

Example : http://localhost:5000/listBlogs
```

<br>

**/addComment** : Adds a comment in a blog post with the help of ID
<br>
```
METHOD : POST

Payload : 
{ 'id' : '72', 'comment' : 'test comment' }
```

<br>

**/listComments** : Lists all comments of a blog post with the help of ID
<br>
```
METHOD : POST

Payload:
No payload required. Only ID value needs to passed in with the endpoint

Example : http://localhost:5000/listComments?id=56
```

<br>
<br>

# How to install this utility
- Install Python form this [LINK](https://www.python.org/downloads/)
- Install below libraries with the command : **pip install LIBRARY_NAME**
    - flask
    - json
    - pymongo
    - jproperties
- Install MongoDB server from [MongoDB Portal](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-os-x/)
- Clone this repository
```
git clone https://github.com/irinbanik/BlogProject.git
```
- To start this tool, open command prompt/terminal/powershell in the directory and run below command to run the utility and use the API with any API client (e.g. Postman, ThunderClient)
```
python app.py
```
