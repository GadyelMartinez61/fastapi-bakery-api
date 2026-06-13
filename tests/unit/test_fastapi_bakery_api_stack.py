import aws_cdk as core
import aws_cdk.assertions as assertions

from fastapi_bakery_api.fastapi_bakery_api_stack import FastapiBakeryApiStack

# example tests. To run these tests, uncomment this file along with the example
# resource in fastapi_bakery_api/fastapi_bakery_api_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = FastapiBakeryApiStack(app, "fastapi-bakery-api")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
