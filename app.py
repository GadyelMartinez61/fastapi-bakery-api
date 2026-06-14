
import aws_cdk as cdk

from infrastructure.stack import InfraestructureBackeryStack

app = cdk.App()
InfraestructureBackeryStack(app, "InfraestructueBakeryApiStack",)

app.synth()
