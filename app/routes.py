from app import app

@app.route('/')
def home():
    return "<h1>welcome to task manager</h1>"