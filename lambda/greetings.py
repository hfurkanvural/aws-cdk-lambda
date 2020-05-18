from datetime import datetime
import utils


def greet(event, context):
    response = "Hi!!! Greetings from CDK. You have hit {} at {}".format(event.get('path'), datetime.now().isoformat())
    return utils.respond_success(response)