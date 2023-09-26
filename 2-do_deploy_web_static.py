#!/usr/bin/python3
"""
Fabric script distributes an archive to your web servers
"""
from fabric.contrib import files
from fabric.api import env, put, run
import os

env.hosts = ['100.25.211.0', '52.202.33.14']


def do_deploy(archive_path):
    """remote deployment function"""
    if not os.path.exists(archive_path):
        return False

    data_path = '/data/web_static/releases/'
    tmp = archive_path.split('.')[0]
    name = tmp.split('/')[1]
    destination = data_path + name

    try:
        put(archive_path, '/tmp')
        run('mkdir -p {}'.format(destination))
        run('tar -xzf /tmp/{}.tgz -C {}'.format(name, destination))
        run('rm -f /tmp/{}.tgz'.format(name))
        run('mv {}/web_static/* {}/'.format(destination, destination))
        run('rm -rf {}/web_static'.format(destination))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(destination))
        return True

    except Exception:
        return False  
