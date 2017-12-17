Note: Python and Flask should be installed on your system for running this task.
You will need Python 2.6 or higher to get started, so be sure to have an up-to-date Python 2.x installation.
For flask, follow this documentation http://flask.pocoo.org/docs/0.12/installation/
or you can follow installation steps given below-

Installation steps-
1.open the terminal and go to your current working where you download this project

for example in my case-

indus-MacBook-Air:~ indukushwaha$ cd desktop

indus-MacBook-Air:desktop indukushwaha$ cd flask_example

indus-MacBook-Air:flask_example indukushwaha$

2.if you are on Mac OS X or Linux, chances are that one of the following two commands will work for you:

$ sudo easy_install virtualenv

Enter your Password:

3.Once you have virtualenv installed, just fire up a shell and create your own environment.

$ virtualenv venv

4.Now, whenever you want to work on a project, you only have to activate the corresponding environment

$ . venv/bin/activate

5.Now you can just enter the following command to get Flask activated in your virtualenv:

$ pip install Flask

6.Now we have to install requests module

$ pip install requests

7.now finally run flask project

python task1.py

8.(venv) indus-MacBook-Air:flask_example indukushwaha$ python task1.py
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 102-617-775

1.A simple hello-world at http://localhost:8080/​ that displays a simple string like "Hello World - Indu".

Steps of execution-

Go to browser and open http://127.0.0.1:5000/ and output will be "Hello World - Indu".

2.Add a route, for e.g. http://localhost:8080/authors​, which:
a) fetches a list of authors from a request to https://jsonplaceholder.typicode.com/users
b) fetches a list of posts from a request to https://jsonplaceholder.typicode.com/posts
c) Respond with only​ a list of authors and the count of their posts (a newline for each author).

Steps for execution:

Go to browser and open http://127.0.0.1:5000/authors and output will be displayed.

3.Set a simple cookie (if it has not already been set) at http://localhost:8080/setcookie​ with the following values: name= and age=.
Fetch the set cookie with http://localhost:8080/getcookies​ and display the stored key-values in it.

Steps for execution:

Go to browser and open http://127.0.0.1:5000/setcookie and cookie will be set.
Click the link to go to http://127.0.0.1:5000/getcookies and cookie's key-value will be displayed.

4.Deny requests to your http://localhost:8080/robots.txt​ page. (or you can use the response at http://httpbin.org/deny if needed)

Steps for execution:

Go to browser and open http://127.0.0.1:5000/robots.txt and response at http://httpbin.org/deny will be displayed.

5.Render an HTML page at http://localhost:8080/html​ or an image at http://localhost:8080/image​.

Steps for execution:

Go to browser and open http://127.0.0.1:5000/html and a html page will be rendered.

6.A text box at http://localhost:8080/input​ which sends the data as POST to any endpoint of your choice. This endpoint should log the received the received to stdout.

Steps for execution:

Go to browser and open http://127.0.0.1:5000/input.
There will be two text box. Enter your data in it and hit enter.
Then your log will be displayed on terminal.
