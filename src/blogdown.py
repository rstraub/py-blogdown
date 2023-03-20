#! /usr/bin/env python3

import argparse
import sys

from src.metadata.rename_tags import rename_tags_in_dir

# Ensures that the src directory is found
sys.path.insert(0, '../src')


def main():
    parser = argparse.ArgumentParser(description='Streamline your markdown blogging workflow')
    subparsers = parser.add_subparsers(title='subcommands', description='Valid subcommands', help='Additional help')

    rename_tag_parser = subparsers.add_parser('rename-tag', help='Rename a tag in all files in a directory')
    rename_tag_parser.add_argument('directory', type=str, help='Files in which to rename tags', default='.')
    rename_tag_parser.add_argument('-o', '--old-tag', type=str, required=True, help='Tag to rename')
    rename_tag_parser.add_argument('-n', '--new-tag', type=str, required=True, help='Replacement tag')

    args = parser.parse_args()

    rename_tags_in_dir(args.directory, args.old_tag, args.new_tag)


if __name__ == '__main__':
    main()
