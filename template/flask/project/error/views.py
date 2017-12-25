pre_code = '''from flask import jsonify
from flask import Blueprint
from werkzeug.exceptions import HTTPException

bp = Blueprint('errors', __name__)

@bp.app_errorhandler(400)
@bp.app_errorhandler(401)
@bp.app_errorhandler(403)
@bp.app_errorhandler(404)
def handler_http_common_error(error):
    return jsonify(errmsg=error.description), error.code
'''
