from flask_apispec import use_kwargs, marshal_with, doc

from . import skeleton_bp, API_CATEGORY


@skeleton_bp.route('/skeleton', methods=['GET'])
@marshal_with((), code=200)
@doc(tags=[API_CATEGORY],
     summary="skeleton get",
     description="skeleton get")
def skeleton_get():
  pass


@skeleton_bp.route('/skeleton', methods=['POST'])
@marshal_with((), code=200)
@doc(tags=[API_CATEGORY],
     summary="skeleton post",
     description="skeleton post")
def skeleton_post():
  pass


@skeleton_bp.route('/skeleton', methods=['PUT'])
@marshal_with((), code=200)
@doc(tags=[API_CATEGORY],
     summary="skeleton put",
     description="skeleton put")
def skeleton_put():
  pass


@skeleton_bp.route('/skeleton', methods=['DELETE'])
@marshal_with((), code=200)
@doc(tags=[API_CATEGORY],
     summary="skeleton delete",
     description="skeleton delete")
def skeleton_delete():
  pass
