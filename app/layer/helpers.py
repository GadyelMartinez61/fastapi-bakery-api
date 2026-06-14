from aws_lambda_powertools.utilities import parameters

def get_parameter(path: str) -> str | list:
    try:
        return parameters.get_parameter(path)
    except Exception:
        return None