from flask import Blueprint

api_bp = Blueprint('api', __name__, url_prefix='/api/v1')

from . import items
from . import sales
from . import stock
from . import home
from . import suppliers
from . import rubros 