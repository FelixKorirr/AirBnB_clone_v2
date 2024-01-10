#!/usr/bin/python3
"""
Fabric script to genereate tgz archive
"""

from datetime import datetime
from fabric.api import *


def do_pack():
    """
    function for making an archive on web_static folder
    """

    time = datetime.now()
    arch = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    do_create = local('tar -cvzf versions/{} web_static'.format(arch))
    if do_create is not None:
        return arch
    else:
        return None
