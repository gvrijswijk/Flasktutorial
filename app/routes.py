from flask import render_template

#The routes are the different URLs that the application implements. In Flask, handlers for the application routes are written as Python functions, called view functions. View functions are mapped to one or more route URLs so that Flask knows what logic to execute when a client requests a given URL.

from app import app

# A decorator modifies the function that follows it. A common pattern with decorators is to use them to register functions as callbacks for certain events. In this case, the @app.route decorator creates an association between the URL given as an argument and the function.
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Gerben'}
    return render_template('index.html', title='Home', user=user)

@app.route('/tmp')
def tmp():
    user = {'username': 'Gerben'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', user=user, posts=posts)