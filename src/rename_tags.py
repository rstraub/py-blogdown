def rename_tags_in_post(file_path, old_tag, new_tag):
    # Read the contents of the file
    with open(file_path, 'r') as file:
        contents = file.read()

    # Replace the old tag with the new tag
    contents = contents.replace(old_tag, new_tag)

    # Write the contents back to the file
    with open(file_path, 'w') as file:
        file.write(contents)

