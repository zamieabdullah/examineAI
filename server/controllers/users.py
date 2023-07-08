from flask import Blueprint
from models.model import db

bp = Blueprint('routes', __name__)

@bp.route('/ping', methods=['GET'])
def ping_pong():
    print('pong')
    return 'pong'