from flask import Flask, render_template, request, redirect, url_for
app1 = Flask(__name__)
# Step 1: Basic Homepage
@app1.route('/')
def home():
    return "Welcome to Flask!"
# Step 2: Dynamic URL Route
@app1.route('/hello/<name>')
def hello(name):
    return f"Hello, {name}!"
# Step 3: GET and POST Request Handling
@app1.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        return redirect(url_for('display', name=name, email=email))
    return render_template('form.html')
@app1.route('/display')
def display():
    name = request.args.get('name')
    email = request.args.get('email')
    return f"Name: {name}, Email: {email}"
# Step 4: Template Rendering with Jinja2
@app1.route('/courses')
def courses():
    course_list = ['Flask Basics', 'Django Fundamentals', 'Data Science with Python']
    return render_template('output.html', courses=course_list)
if __name__ == '__main__':
    app1.run(debug=True)