#!/usr/bin/python3
""" Deletes out-of-date archives """

from fabric.api import *


env.hosts = ['100.25.211.0', '100.25.215.249']


def do_clean(number=0):
    """ clears out-of-date archives """

    number = int(number)

    if number == 0:
        number = 2
    else:
        number += 1

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))
