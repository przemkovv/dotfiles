#!/usr/bin/env python

"""
Prepare environment for dotfiles.

Created by Przemyslaw Walkowiak <przemkovv@gmail.com>

Usage:
    dotfiles.py install [DOTFILES_PATH] [PATH]
    dotfiles.py install_package <package> [DOTFILES_PATH] [PATH]
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
            yield entry


def make_symlink(source, target):
    print("\t%s -> %s" % (source, target))
    if os.path.exists(target):
        os.remove(target)
    os.symlink(source, target)


def get_package_path(package, dotfiles_path):
    package_path = os.path.join(dotfiles_path, package)
    if not os.path.exists(package_path):
        raise IOError("Package '%s' cannot be found. Path '%s' doesn't exists."
                      % (package, package_path))
    return package_path


def install_package(package, dotfiles_path, dst_path):
    print("Installing package '%s':" % package)
    package_path = get_package_path(package, dotfiles_path)
    for entry in os.listdir(package_path):
        if entry.startswith(".git"):
            continue
        source = os.path.join(package_path, entry)
        target = os.path.join(dst_path, ".%s" % entry)
        make_symlink(source, target)


def install(dotfiles_path, dst_path):
    for package in list_packages(dotfiles_path):
        install_package(package, dotfiles_path, dst_path)
    #for package in os.listdir(dotfiles):
        #pass


def update(dotfiles_path):
    pass


def main(args):

    try:
        DEFAULT_PATH = "~"
        DEFAULT_DOTFILES_PATH = "~/dotfiles"

        dst_path = args["PATH"] or DEFAULT_PATH
        dotfiles_path = args["DOTFILES_PATH"] or DEFAULT_DOTFILES_PATH

        dst_path = os.path.expanduser(dst_path)
        dotfiles_path = os.path.expanduser(dotfiles_path)
        dotfiles_path = os.path.abspath(dotfiles_path)

        if not os.path.exists(dst_path):
            raise IOError("Destination path '%s' cannot be found." % dst_path)
        if not os.path.exists(dotfiles_path):
            raise IOError("Dotfiles path '%s' cannot be found."
                          % dotfiles_path)

        if args['install']:
            install(dotfiles_path, dst_path)
        if args['install_package']:
            package_name = args["<package>"]
            install_package(package_name, dotfiles_path, dst_path)
        elif args['update']:
            update(dotfiles_path)

    except IOError as ex:
        print("I/O error: %s" % ex)

if __name__ == '__main__':
    main(docopt(__doc__, version='0.1alpha'))
