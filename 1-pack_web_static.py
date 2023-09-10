#!/usr/bin/python3
"""generates an archive of web_static folder"""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """function to generate the archive"""
    try:
        # Create the 'versions' directory if it doesn't exist
        if not os.path.exists('versions'):
            os.makedirs('versions')

        # Create the archive filename (web_static_<timestamp>.tgz)
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        archive_name = f'web_static_{timestamp}.tgz'

        # Create the archive using tar command
        local('tar -cvzf versions/{} web_static'.format(archive_name))

        # Return the archive path if successful
        return 'versions/{}'.format(archive_name)
    except Exception as e:
        return None
