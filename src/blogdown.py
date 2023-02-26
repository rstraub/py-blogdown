#! /usr/bin/env python3

import argparse

from rename_tags import rename_tags_in_dir

parser = argparse.ArgumentParser(description='Blogdown')
parser.add_argument("--directory", type=str, help="The directory to process", default=".")
parser.add_argument("--old-tag", type=str, help="The tag to replace")
parser.add_argument("--new-tag", type=str, help="The tag that will be used instead")

args = parser.parse_args()

rename_tags_in_dir(args.directory, args.old_tag, args.new_tag)
