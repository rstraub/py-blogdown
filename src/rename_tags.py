import os

from src.frontmatter_utils import rename_tag


def rename_tags_in_dir(dir_path, old_tag, new_tag):
    files_in_dir = os.listdir(dir_path)

    for file in files_in_dir:
        file_path = os.path.join(dir_path, file)

        rename_tags_in_post(file_path, old_tag, new_tag)


def rename_tags_in_post(file_path, old_tag, new_tag):
    # Read the contents of the file
    with open(file_path, 'r') as file:
        contents = file.read()

    contents = rename_tag(contents, old_tag, new_tag)

    # Write the contents back to the file
    with open(file_path, 'w') as file:
        file.write(contents)

