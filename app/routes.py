from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'ning'}
    return '''
<html>
    <head>
        <title> Home Page -myBlog </title> 
    <head>
    <body>
        <h1>Hello,'''+user['username']+'''!</h1>
    </body>
</html>     
'''
