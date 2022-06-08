from . import home


@home.route('/')
def home_page():
    return "Hello world"


@home.route('/sign-up')
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


@home.route('/login')
def login():
    return "login"
