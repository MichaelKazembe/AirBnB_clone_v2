#!/usr/bin/python3
""" fabfile tar archive packaging """

from fabric.api import local, run, env, put, cd
from datetime import datetime
import os

env.hosts = ['100.25.211.0', '100.25.215.249']


def do_pack():
    """ Packes web_static in tgz format """
    now = datetime.now()
    name = "web_static_{}{}{}{}{}{}.tgz".format(
        now.year, now.month, now.day, now.hour, now.minute, now.second)
    local('mkdir -p versions')
    local("tar -cvzf versions/{} web_static".format(name))
    size = os.stat("versions/{}".format(name)).st_size
    print("web_static packed: versions/{} -> {}".format(name, size))
    path = "versions/{}".format(name)
    return(path)


def do_deploy(archive_path):

    if not archive_path:
        return(False)
    name = archive_path.split('/')[1]
    try:
        put(archive_path, '/tmp/')
        run("mkdir -p /data/web_static/releases/{}".format(name))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}"
            .format(name, name))
        run("rm /tmp/{}".format(name))
        run("mv /data/web_static/releases/{}/web_static/*\
        /data/web_static/releases/{}".format(name, name))
        run("rm -rf /data/web_static/releases/{}/web_static"
            .format(name))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(name))
        print("New version deployed")
        return(True)
    except BaseException:
        return(False)


def deploy():

    try:
        path = do_pack()
    except BaseException:
        return(False)
    do_deploy(path)

def do_clean(number=0):

    if number == 0 or number == 1:
        with cd.local('./versions/'):
            run('ls -t | tail -n +2 | xargs rm --')
        with cd.local('/data/web_static/releases/'):
            run('ls -t | tail -n +2 | xargs rm --')
    else:
        with cd.local('./versions/'):
            run('ls -t | tail -n +2 | xargs rm --')
        with cd.local('/data/web_static/releases/'):
            run('ls -t | tail -n +2 | xargs rm --')
