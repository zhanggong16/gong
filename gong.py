#!/usr/bin/env python
import os
import click
import gen_code, create_venv

@click.command()
@click.option('--framework', default='flask', help='Framework you want to use')
@click.option('--name', prompt='package name', help='Package name you want to create')
@click.option('--path', prompt='package path', help='Package name you want to deploy')
def gong(framework, name, path):
    print "=" * 20
    if framework.lower() == 'flask':
        full_path = path + '/' + name
        print "framework: %s, package name: %s, package path: %s" % (framework, name, full_path)
        confirm = raw_input("confirm(y,n): ")
        if confirm.lower() == 'y':
            if os.path.isdir(full_path):
                create_venv.create_venv(full_path)
                gen_code.create_flask_project(name, path) 
            else:
                print "%s is not dir, do 'mkdir -p %s'." % (full_path, full_path)
        else:
            print "exit."


if __name__ == '__main__':
    gong()
