from app import app_object

@app_object.route('/')
@app_object.route('/index')
def index():
    return "Hello, World!"