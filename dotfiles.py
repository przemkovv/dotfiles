#!/usr/bin/env python

"""
Prepare environment for dotfiles.

Created by Przemyslaw Walkowiak <przemkovv@gmail.com>

Usage:
    dotfiles.py install [DOTFILES_PATH] [PATH]
    dotfiles.py update [DOTFILES_PATH]

Arguments:
    DOTFILES_PATH   dotfiles folder.
    PATH            place where the dotfiles
    will be installed. [default: ~]

Options:
    -h --help       Show this screen.

"""

import os
from docopt import docopt


def list_packages(path):
    for entry in os.listdir(path):
        entry_path = os.path.join(path, entry)
        if os.path.isdir(entry_path) and not entry.startswith("."):
            yield entry_path


def make_symlink(source, target):
    print "%s -> %s" % (source, target)
    if os.path.exists(target):
        os.remove(target)
    os.symlink(source, target)


def install_package(package_path, dst_path):
    for entry in os.listdir(package_path):
        if not entry.startswith(".git"):
            source = os.path.join(package_path, entry)
            target = os.path.join(dst_path, ".%s" % entry)
            make_symlink(source, target)


def install(dotfiles_path, dst_path):
    for package in list_packages(dotfiles_path):
        install_package(package, dst_path)
    #for package in os.listdir(dotfiles):
        #pass


def update(dotfiles_path):
    pass


def main(args):
    DEFAULT_PATH = "~"
    DEFAULT_DOTFILES_PATH = "~/dotfiles"

    dst_path = args["PATH"] or DEFAULT_PATH
    dotfiles_path = args["DOTFILES_PATH"] or DEFAULT_DOTFILES_PATH

    dst_path = os.path.expanduser(dst_path)
    dotfiles_path = os.path.expanduser(dotfiles_path)

    if not os.path.exists(dst_path):
        raise IOError("Destination path '%s' cannot be found" % dst_path)
    if not os.path.exists(dotfiles_path):
        raise IOError("Dotfiles path '%s' cannot be found" % dotfiles_path)

    if args['install']:
        install(dotfiles_path, dst_path)
    elif args['update']:
        update(dotfiles_path)


if __name__ == '__main__':
    main(docopt(__doc__, version='0.1alpha'))
