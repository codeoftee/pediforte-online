from . import home


@home.route('/')
def home_page():
    return "Hello world"


@home.route('/sign-up')
<<<<<<< HEAD
def sign-up():
    return render_template('sign-up.html')  

@home.route('/do-sign-up', methods=['POST'])
def do_signup():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    username = request.form['username']
    email = request.form['email']
    phone = request.form['phone']
    password = request.form['password']
    password2 = request.form['password2']
    if firstname == '' or lastname == '' or email == ''or password == '' or username == '':
        flash('All fields are required! ')
        return redirect(url_for('register_page'))
    if password != password2:
        flash('Password does not match')
        return redirect(url_for('register_page'))
    password_hash = hashlib.sha256(password.encode()).hexdigest()
=======
def sign_up():
    return "sign up"
>>>>>>> e02b4b4ec4188a33d2c06a87d35bed13fd0c8cf8


@home.route('/login')
def login():
    return "login"
