import os

import aws_cdk as cdk

from infrastructure.stack import InfraestructureStack

app = cdk.App()
InfraestructureStack(app, "InfraestructueBakeryApiStack",)

app.synth()
