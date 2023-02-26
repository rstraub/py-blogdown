import os

from src.rename_tags import rename_tags_in_post


def test_should_rename_matching_tag_with_new_tag():
    # TODO create a copy of the file
    contents = test_blog_path()

    rename_tags_in_post(contents, 'Python', 'Python3')

    result = test_blog_path()

    assert "Python3" in result


def test_blog_path():
    # Get the directory of the current script
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # Construct the path to the data file
    return os.path.join(dir_path, 'data/input/test_blog.md')


def read_test_blog():
    with open(test_blog_path(), 'r') as file:
        contents = file.read()
    return contents

