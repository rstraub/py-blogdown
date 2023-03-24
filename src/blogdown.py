#! /usr/bin/env python3

import argparse
import sys
import os

from src.metadata.rename_tags import rename_tags_in_dir, rename_tags_in_post

# Ensures that the src directory is found
sys.path.insert(0, '../src')


def main():
    parser = argparse.ArgumentParser(description='Streamline your markdown blogging workflow')
    subparsers = parser.add_subparsers(title='subcommands', description='Valid subcommands', help='Additional help')

    rename_tag_parser = subparsers.add_parser('rename-tag',
                                              help='Rename a tag in markdown files or files in a directory')
    rename_tag_parser.add_argument('locations', type=str, help='Files and/or directories in which to rename tags',
                                   default='.', nargs='+')
    rename_tag_parser.add_argument('-o', '--old-tag', type=str, required=True, help='Tag to rename')
    rename_tag_parser.add_argument('-n', '--new-tag', type=str, required=True, help='Replacement tag')

    args = parser.parse_args()

    locations = args.locations
    old_tag = args.old_tag
    new_tag = args.new_tag
    print(f'Renaming tags in {", ".join(locations)} from {old_tag} to {new_tag}')

    for location in locations:
        if os.path.isdir(location):
            rename_tags_in_dir(location, old_tag, new_tag)
        elif os.path.isfile(location):
            rename_tags_in_post(location, old_tag, new_tag)
        else:
            print('Path is not a file or directory')


if __name__ == '__main__':
    main()
