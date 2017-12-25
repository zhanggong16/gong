import os
import errno

def _create_module(filepath):
    dir = os.path.dirname(filepath)
    open(dir + '/__init__.py', 'a').close()

def _fill_script(package_name, package_path, filename, pre_code):
    cur_path = package_path
    filepath = ('{cur_path}/{package_name}/{filename}').format(
        cur_path=cur_path,
        package_name=package_name,
        filename=filename)
    dir = os.path.dirname(filepath)
    if not os.path.exists(dir):
        try:
            os.makedirs(dir)
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise
    with open(filepath, 'w+') as file:
        file.write(pre_code)

def _fill_py_file(package_name, package_path, pre_code, filename, create_module=True):
    pre_code = pre_code.format(package_name=package_name)
    cur_path = package_path
    filepath = ('{cur_path}/{package_name}/{filename}').format(
        cur_path=cur_path,
        package_name=package_name,
        filename=filename)
    dir = os.path.dirname(filepath)
    if not os.path.exists(dir):
        try:
            os.makedirs(dir)
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise
    if create_module:
        _create_module(filepath)
    with open(filepath, 'w+') as file:
        file.write(pre_code)

def create_flask_project(package_name, package_path):
    # scripts
    from template.flask import scripts

    # entrypoint
    from template.flask.app import pre_code as entrypoint
    
    # package
    from template.flask.project.app import pre_code as app_code
    from template.flask.project.config import pre_code as config_code    
    from template.flask.project.error.views import pre_code as error_code
    from template.flask.project.index.views import pre_code as index_code
    from template.flask.project.templates.index import pre_code as templates_index_code

    # fill .py files
    _fill_py_file(package_name, package_path, entrypoint, 'app.py', create_module=False)
    _fill_py_file(package_name, package_path, app_code, '{package_name}/app.py'.format(package_name=package_name))
    _fill_py_file(package_name, package_path, config_code, '{package_name}/config.py'.format(package_name=package_name))
    _fill_py_file(package_name, package_path, error_code, '{package_name}/error/views.py'.format(package_name=package_name))    
    _fill_py_file(package_name, package_path, index_code, '{package_name}/index/views.py'.format(package_name=package_name))
    _fill_py_file(package_name, package_path, templates_index_code, '{package_name}/templates/index.html'.format(package_name=package_name), create_module=False)

    # fill scripts
    _fill_script(package_name, package_path, 'requirement.txt', scripts.req)
    _fill_script(package_name, package_path, 'Procfile', scripts.procfile)
    _fill_script(package_name, package_path, '.env', scripts.env_example.format(package_name=package_name.upper()))

