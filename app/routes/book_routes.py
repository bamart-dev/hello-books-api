from flask import Blueprint
from app.models.book import books

books_bp = Blueprint("books_bp", __name__, url_prefix="/books")


@books_bp.get("")
def get_all_books():

    return [
            {
            "id": book.id,
            "title": book.title,
            "description": book.description,
            } for book in books]
