from datetime import datetime
import utils


def greet(event, context):
    response = "Hi! This is simple ToDo API. You have hit {}".format(event.get('path'))
    return utils.respond_success(response)