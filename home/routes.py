from . import home


@home.route('/')
def home_page():
    return "Hello world"


@home.route('/sign_up')
def sign_up():
    return "sign up"


@home.route('/login')
def login():
    return "login"
