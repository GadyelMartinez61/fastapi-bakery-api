from aws_cdk import Stack, Construct, aws_dynamodb as dynamodb, aws_lambda as _lambda


class MyInfrastructureStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

