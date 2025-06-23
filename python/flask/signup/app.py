from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary list to hold users
users = []

@app.route('/')
def home():
    return redirect(url_for('signup'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        gender = request.form['gender']

        users.append({'name': name, 'email': email, 'gender': gender})
        return f"Signup successful! Welcome, {name} ({gender}) 🎉"

    return render_template('signup.html')


if __name__ == '__main__':
    app.run(debug=True)
