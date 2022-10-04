from app import app


@app.route("/")
def index():
    return "Hello from flask Nginx in a container"