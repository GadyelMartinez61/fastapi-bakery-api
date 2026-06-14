from pydantic_settings import BaseSettings
from ..layer.helpers import get_parameter


class Settings(BaseSettings):
    environment: str = "dev"
    project: str = "fast-api-backery"
    region: str = "us-east-1"

    products_table: str = "Products"
    branches_table: str = "Branches"
    sales_table: str = "Sales"
    users_table: str = "Users"

    jwt_secret: str = get_parameter(f"{project}-{environment}/jwt_secret")
    jwt_algorithm: str = "HS256"
    jwt_expire_minutes: int = 10

    model_config = {"env_file": ".env"}


settings = Settings()  # instancia única (singleton)
