#! /usr/bin/env python3

import os
import argparse


def rename_tags_in_dir(dir_path, old_tag, new_tag):
    files_in_dir = os.listdir(dir_path)

    for file in files_in_dir:
        file_path = os.path.join(dir_path, file)

        rename_tags_in_post(file_path, old_tag, new_tag)


def rename_tags_in_post(file_path, old_tag, new_tag):
    # Read the contents of the file
    with open(file_path, 'r') as file:
        contents = file.read()

    # Replace the old tag with the new tag
    contents = contents.replace(old_tag, new_tag)

    # Write the contents back to the file
    with open(file_path, 'w') as file:
        file.write(contents)


parser = argparse.ArgumentParser(description='Blogdown')
parser.add_argument("--directory", type=str, help="The directory to process", default=".")
parser.add_argument("--old-tag", type=str, help="The tag to replace")
parser.add_argument("--new-tag", type=str, help="The tag that will be used instead")

args = parser.parse_args()

rename_tags_in_dir(args.directory, args.old_tag, args.new_tag)
