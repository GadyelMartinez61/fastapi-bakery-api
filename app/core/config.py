from pydantic_settings import BaseSettings
from ..layer.helpers import get_parameter


class Settings(BaseSettings):
    environment: str = "dev"
    project: str = "fast-api-bakery"
    region: str = "us-east-1"

    products_table: str = f"fast-api-products-{environment}"
    branches_table: str = f"fast-api-branches-{environment}"
    sales_table: str = f"fast-api-sales-{environment}"
    users_table: str = f"fast-api-users-{environment}"

    jwt_secret: str = get_parameter(f"{project}-{environment}/jwt_secret")
    jwt_algorithm: str = "HS256"
    jwt_expire_minutes: int = 10

    model_config = {"env_file": ".env"}


settings = Settings()  # instancia única (singleton)
