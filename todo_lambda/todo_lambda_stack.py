from aws_cdk import (
    core,
    aws_lambda as _lambda,
    aws_apigateway as api_gateway
)
class TodoLambdaStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        lambda_greetings = _lambda.Function(
            self, 'GreetingsHandler',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.asset('lambda'),
            handler='greetings.greet',
            memory_size=128
        )
        api_stage_options = api_gateway.StageOptions(stage_name="dev")
        api = api_gateway.LambdaRestApi(self, 'Endpoint', handler=lambda_greetings, deploy_options=api_stage_options)
        




