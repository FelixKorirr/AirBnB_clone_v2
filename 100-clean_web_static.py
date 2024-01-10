#!/usr/bin/python3
"""
Deletes out-of-date archives
"""

import os
from fabric.api import *

env.hosts = ['100.25.102.196', '52.86.109.248']


def do_clean(number=0):
    """Delete out-of-date archives.
    Args:
        number (int): number of archives to keep.
    """
    number = 1 if int(number) == 0 else int(number)

    archive = sorted(os.listdir("versions"))
    [archive.pop() for x in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archive]

    with cd("/data/web_static/releases"):
        archive = run("ls -tr").split()
        archive = [a for a in archive if "web_static_" in a]
        [archive.pop() for x in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archive]
