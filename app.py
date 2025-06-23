from flask import Flask, url_for, request, redirect, render_template
app = Flask(__name__)

@app.route('/route')
def hello():
    return "Welcome to Flask"

@app.route('/hello/<name>/<email>')
def greetings(name, email):
    return f"Hello {name} and your email is {email}"

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        name = request.form['name']
        email = request.form['email']
        return redirect(url_for('greetings', name = name, email = email))
    

@app.route('/courses', methods = ['GET','POST'])
def display():
    courses = ['Python', 'C++', 'Java', 'MongoDB']
    return render_template('output.html', courses = courses)

'''@app.route('/courses/<list>', methods = ['GET','POST'])
def display(list):
    #list1 = [1,5,9,7]
    return render_template('output.html', list1 = list)'''

if __name__ == "__main__":
    app.run(debug=True)