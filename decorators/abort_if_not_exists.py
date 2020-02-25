from functools import wraps
from flask import abort


def abort_if_not_exists(entity):
    def inner_function(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            response, status_code = function(**kwargs)
            if status_code != 200 or response["data"] == None:
                abort(404, {"code": 404, "message": "{} do no exists".format(entity)})
            return response

        return wrapper

    return inner_function
