from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('signup.html')

@app.route('/login', methods=['POST'])
def login():
    name = request.form.get('name')
    email = request.form.get('email')
    mobile = request.form.get('mobile')
    gender = request.form.get('gender')
    
    return 'welcome %s' % name
    

if __name__ == '__main__':
    app.run(debug=True)