from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__, template_folder='templates')

@app.route('/')
def homePage():
    return render_template('index.html', message='Welcome to HomePage')

@app.route('/base')
def basePage():
    return render_template('base.html')

@app.route('/testing')
def testPage():
    return render_template('test.html')

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]
        if username:
            return redirect(url_for("sayHello", name=username
            ,password=password))
    
    return render_template('login.html')

@app.route('/user/<name>')
def hello_user(name):
    return f"<h1> Hello {name} </h1>"

@app.route('/sayHello/<name>/<password>')
def sayHello(name, password):
    return render_template('sayHello.html', username=name, 
    password=password)

if __name__ == '__main__':
    app.run(debug=True)