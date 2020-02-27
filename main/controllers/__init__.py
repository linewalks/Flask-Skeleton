from flask import Blueprint

skeleton_bp = Blueprint('skeleton', __name__, url_prefix="/api")

API_CATEGORY = 'Skeleton'

from main.controllers.skeleton import *
