
import aws_cdk as cdk

from infrastructure.stack import InfrastructureBackeryStack
from app.core.config import settings

app = cdk.App()

environment = settings.environment

InfrastructureBackeryStack(app, "InfrastructureBackeryStack", environment)

app.synth()
