#!/usr/bin/env python3

from aws_cdk import core

from todo_lambda.todo_lambda_stack import TodoLambdaStack

environment = core.Environment(region="eu-central-1")

app = core.App()
TodoLambdaStack(app, "todo-lambda")

app.synth()
