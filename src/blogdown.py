#! /usr/bin/env python3

import argparse

from src.rename_tags import rename_tags_in_dir


def main():
    parser = argparse.ArgumentParser(description='Streamline your markdown blogging workflow')
    parser.add_argument('-d', '--directory', type=str, help='Directory to run the rename in', default=".")
    parser.add_argument('-o', '--old-tag', type=str, required=True, help='Tag to rename')
    parser.add_argument('-n', '--new-tag', type=str, required=True, help='Replacement tag')

    args = parser.parse_args()

    rename_tags_in_dir(args.directory, args.old_tag, args.new_tag)


if __name__ == '__main__':
    main()
