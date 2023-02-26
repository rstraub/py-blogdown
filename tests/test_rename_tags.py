import os

from src.rename_tags import rename_tags


def test_should_rename_matching_tag_with_new_tag():
    contents = read_test_blog()
    print(contents)
    rename_tags(contents, 'Python', 'Python3')

    assert True is False


def read_test_blog():
    # Get the directory of the current script
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # Construct the path to the data file
    test_blog_path = os.path.join(dir_path, 'data/input/test_blog.md')
    with open(test_blog_path, 'r') as file:
        contents = file.read()
    return contents
