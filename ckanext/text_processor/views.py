from flask import Blueprint


text_processor = Blueprint(
    "text_processor", __name__)


def page():
    return "Hello, text_processor!"


text_processor.add_url_rule(
    "/text_processor/page", view_func=page)


def get_blueprints():
    return [text_processor]
