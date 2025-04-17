from flask import Blueprint


hello_world_bp = Blueprint("hello_world", __name__)

@hello_world_bp.get("/")
def hello_world():

    return "Hello, World!"


@hello_world_bp.get("/hello/JSON")
def hello_json():
    response = {
        "name": "Brian",
        "message": "This is a test API.",
        "hobbies": [
            "playing videogames", "listening to music", "going for walks"
            ],
    }

    return response
