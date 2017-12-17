import requests
from flask import Flask, url_for, request, jsonify, redirect, make_response
from flask import render_template
app = Flask(__name__)

# 1.A simple hello-world at http://localhost:8080/ that displays a simple string like "Hello World - Arpit"; replace "Arpit" with your own first name).

@app.route('/hello')
def hello():
   return 'Hello World - Indu'

# 2. Add a route, for e.g. http://localhost:8080/authors, which:
# a) fetches a list of authors from a request to https://jsonplaceholder.typicode.com/users
# b) fetches a list of posts from a request to https://jsonplaceholder.typicode.com/posts
# c) Respond with only a list of authors and the count of their posts (a newline for each author).

@app.route('/authors')
def get_users():
    r_users= requests.get('http://jsonplaceholder.typicode.com/users')
    r_posts= requests.get('http://jsonplaceholder.typicode.com/posts')
    json_object_authors=r_users.json()
    json_object_posts=r_posts.json()
    return render_template('authors.html',authors=json_object_authors,posts=json_object_posts)


# 3.Set a simple cookie (if it has not already been set) at http://localhost:8080/setcookie with the following values: name=<your-first-name> and age=<your-age>.

@app.route('/setcookie')
def cookie_insertion():
    redirect_to_index = redirect('/index')
    response =make_response(redirect_to_index )
    name = request.cookies.get('name')
    age = request.cookies.get('age')
    if name!='indu' and age!='31':
        response.set_cookie('name',value='indu')
        response.set_cookie('age',value='31')
        return response
    return 'cookies already set'

# 4. Fetch the set cookie with http://localhost:8080/getcookies and display the stored key-values in it.

@app.route('/getcookies')
def cookie_retrive():
    name = request.cookies.get('name')
    age = request.cookies.get('age')
    string_temp='key: first name and value: %s' % name
    string_temp+='<br>key: age and value: %s' % age
    return string_temp

# 5.Deny requests to your http://localhost:8080/robots.txt page. (or you can use the response at http://httpbin.org/deny if needed)

@app.route('/robots.txt')
def deny_page():
    redirect_to_deny_page = redirect('http://httpbin.org/deny')
    response =make_response(redirect_to_deny_page )
    return response

# 6.Render an HTML page at http://localhost:8080/html or an image at http://localhost:8080/image.

@app.route('/html')
def show_html_page():
    return render_template('profile.html')

# 7.A text box at http://localhost:8080/input which sends the data as POST to any endpoint of your choice. This endpoint should log the received the received to stdout.

@app.route('/input')
def login_form():
   return render_template('login.html')

@app.route('/login',methods = ['POST', 'GET'])
def login():
   username=request.form['username']
   app.logger.debug('A value for debugging %s' % username)
   if request.method == 'POST' and request.form['username'] == 'indu' :
       return redirect(url_for('success'))
   return 'logged in fail'

@app.route('/success')
def success():
   return 'logged in successfully'

if __name__ == '__main__':
    app.run(debug=True)
