#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = """Darrell Purcell with help from
Piero's Sprint 3 Overview demo
https://www.youtube.com/watch?v=tJxcKyFMTGo"""

import re
import os
import sys
import shutil
import subprocess
import argparse


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""
    special_files = []
    dir_regex = re.compile(r'.*__\w+__.*')
    directory = os.listdir(dirname)
    for file in directory:
        dir_match = re.findall(dir_regex, file)
        if dir_match:
            absolute_path = os.path.abspath(os.path.join(dirname, file))
            special_files.append(absolute_path)
    if len(special_files) == 0:
        print("No special files exist in this directory.")
    return special_files


def create_directory(path):
    """Validation for directory creation"""
    if not os.path.exists(path):
        try:
            os.makedirs(path)
        except Exception as e:
            print(e)
            print(f'Creation of {path} was unsuccessful')
            return False
    return True


def copy_to(path_list, dest_dir):
    """Copies file directory to given destination"""
    if not create_directory(dest_dir):
        return
    else:
        for file in path_list:
            shutil.copyfile(
                file, os.path.join(dest_dir, os.path.basename(file)))


def zip_to(path_list, dest_zip):
    """Given a list of files and destination path,
    performs zip operation on all files in path list"""
    zip_run_cmd = ['zip', '-j', dest_zip]
    zip_run_cmd.extend(path_list)
    print('Performing the following operation:')
    # print(" ".join(zip_run_cmd))
    print(zip_run_cmd)
    try:
        subprocess.call(zip_run_cmd)
    except OSError as Error:
        print(Error)
        exit(1)


def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('from_dir', help='source dir for special files')
    # TODO: add one more argument definition to parse the 'from_dir' argument
    ns = parser.parse_args(args)

    # TODO: you must write your own code to get the command line args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation. If something is wrong (or missing) with
    # any required args, the general rule is to print a usage message and
    # exit(1).

    # Your code here: Invoke (call) your functions

    if not ns:
        parser.print_usage()
        sys.exit(1)

    if ns.todir:
        path_list = get_special_paths(ns.from_dir)
        home = os.environ.get('HOME')
        dest = os.path.join(home, ns.todir)
        copy_to(path_list, dest)
    elif ns.tozip:
        path_list = get_special_paths(ns.from_dir)
        zip_to(path_list, ns.tozip)
    else:
        path_list = get_special_paths(ns.from_dir)
        for file in path_list:
            print(file)


if __name__ == "__main__":
    main(sys.argv[1:])
