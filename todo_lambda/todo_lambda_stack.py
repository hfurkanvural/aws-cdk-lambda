from aws_cdk import (
    core,
    aws_lambda as _lambda,
    aws_apigateway as api_gateway,
    aws_dynamodb as aws_dynamodb
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

        # create dynamo table
        demo_table = aws_dynamodb.Table(
            self, "ToDos_table",
            partition_key=aws_dynamodb.Attribute(
                name="id",
                type=aws_dynamodb.AttributeType.STRING
            )
        )
        get_todos_handler = _lambda.Function(
            self, 'GetTodos',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.asset('lambda'),
            handler='todos.get',
            memory_size=128
        )
        get_todos_handler.add_environment("TABLE_NAME", demo_table.table_name)
        demo_table.grant_read_data(get_todos_handler)

        get_todos_integration = api_gateway.LambdaIntegration(get_todos_handler)

        #/todos GET = todo listeleyecek
        todos = api.root.add_resource("todos")
        todos.add_method("GET", get_todos_integration)

        get_todo_handler = _lambda.Function(
            self, 'GetTodo',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.asset('lambda'),
            handler='todo.get',
            memory_size=128
        )

        get_todo_handler.add_environment("TABLE_NAME", demo_table.table_name)
        demo_table.grant_read_data(get_todo_handler)

        put_todo_handler = _lambda.Function(
            self, 'PutTodo',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.asset('lambda'),
            handler='todo.put',
            memory_size=128
        )
        put_todo_handler.add_environment("TABLE_NAME", demo_table.table_name)
        demo_table.grant_write_data(put_todo_handler)

        delete_todo_handler = _lambda.Function(
            self, 'DeleteTodo',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.asset('lambda'),
            handler='todo.delete',
            memory_size=128
        )

        delete_todo_handler.add_environment("TABLE_NAME", demo_table.table_name)
        demo_table.grant_write_data(delete_todo_handler)


        get_todo_integration = api_gateway.LambdaIntegration(get_todo_handler)
        put_todo_integration = api_gateway.LambdaIntegration(put_todo_handler)
        delete_todo_integration = api_gateway.LambdaIntegration(delete_todo_handler)


        #/todo path
        todo = api.root.add_resource("todo")

        #/todo/{todoId}
        todo_gd = todo.add_resource("{todoId}")
        #/todo/{todoId} GET
        todo_gd.add_method("GET", get_todo_integration)
        #/todo/{todoId} DELETE = todo silecek
        todo_gd.add_method("DELETE", delete_todo_integration)

        #/todo/new
        todo_p = todo.add_resource("new")
        todo_p.add_method("PUT", put_todo_integration)






