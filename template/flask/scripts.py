req = """honcho==1.0.1
Flask==0.12.2
gunicorn==19.7.1
python-envcfg==0.2.0
"""

procfile = """server: python app.py
"""

env_example = """{package_name}_HTTP_PORT='5000'
{package_name}_DEBUG='true'
"""
