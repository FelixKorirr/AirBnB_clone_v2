#!/usr/bin/python3
"""
Fabric script based on the file 2-do_deploy_web_static.py that creates and
distributes an archive to the web servers
"""

from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir
env.hosts = ['100.25.102.196', '52.86.109.248']


def do_pack():
    """Generates tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        my_file = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(my_file))
        return my_file
    except:
        return None


def do_deploy(archive_path):
    """Distribute an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        my_file = archive_path.split("/")[-1]
        no_ext = my_file.split(".")[0]
        file_path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(file_path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(my_file, file_path, no_ext))
        run('rm /tmp/{}'.format(my_file))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(file_path, no_ext))
        run('rm -rf {}{}/web_static'.format(file_path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(file_path, no_ext))
        return True
    except:
        return False


def deploy():
    """creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
