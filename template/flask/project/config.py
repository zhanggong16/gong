pre_code = """from envcfg.json.{package_name} import HTTP_PORT
from envcfg.json.{package_name} import DEBUG


APP = '{package_name}'

__all__ = [
    'HTTP_PORT',
    'DEBUG',
]
"""
