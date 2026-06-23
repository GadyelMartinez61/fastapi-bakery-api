from aws_cdk import Stack, Construct, aws_dynamodb as dynamodb, aws_lambda as _lambda


class InfrastructureBackeryStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, environment: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        branch_table = dynamodb.Table(
            self,
            f"BranchesTable{environment}",
            table_name=f"fast-api-branches-{environment}",
            partition_key=dynamodb.Attribute(
                name="id", type=dynamodb.AttributeType.STRING
            ),
        )

        products_table = dynamodb.Table(
            self,
            f"ProductsTable{environment}",
            table_name=f"fast-api-products-{environment}",
            partition_key=dynamodb.Attribute(
                name="branch_id", type=dynamodb.AttributeType.STRING
            ),
            sort_key=dynamodb.Attribute(
                name="product_id", type=dynamodb.AttributeType.STRING
            ),
        )

        users_table = dynamodb.Table(
            self,
            f"UsersTable{environment}",
            table_name=f"fast-api-users-{environment}",
            partition_key=dynamodb.Attribute(
                name="username", type=dynamodb.AttributeType.STRING
            ),
        )

        sales_table = dynamodb.Table(
            self,
            f"SalesTable{environment}",
            table_name=f"fast-api-sales-{environment}",
            partition_key=dynamodb.Attribute(
                name="branch_id", type=dynamodb.AttributeType.STRING
            ),
            sort_key=dynamodb.Attribute(
                name="sale_id", type=dynamodb.AttributeType.STRING
            ),
        )
