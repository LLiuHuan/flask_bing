from flask import Blueprint, render_template, request, Response, session, url_for


blue = Blueprint('blue', __name__, url_prefix='/db', template_folder='../template', static_url_path='../static/')

