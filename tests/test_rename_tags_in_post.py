import pytest
import os
import shutil

from src.rename_tags import rename_tags_in_post


def test_should_rename_matching_tag_with_new_tag():
    # Copy the reference test blog to a temporary file
    test_post_path = _data_dir_path() + '/input/test_post.md'
    tmp_path = test_post_path.replace('input', 'tmp')
    copy_blog(test_post_path, tmp_path)

    rename_tags_in_post(tmp_path, 'Scala', 'Python3')

    result = _get_post_contents(tmp_path)

    assert "Python3" in result


@pytest.fixture(autouse=True)
def _fixture():
    yield
    _clean_tmp_dir()

def _clean_tmp_dir():
    # Get the directory of the current script
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # Construct the path to the tmp folder
    tmp_path = os.path.join(dir_path, 'data/tmp')
    # Delete the contents of the tmp folder
    for file in os.listdir(tmp_path):
        file_path = os.path.join(tmp_path, file)
        os.remove(file_path)


def copy_blog(test_file, new_file):
    shutil.copyfile(test_file, new_file)


def _data_dir_path():
    # Get the directory of the current script
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # Construct the path to the reference post
    return os.path.join(dir_path, 'data')


def _get_post_contents(blog_path):
    with open(blog_path, 'r') as file:
        contents = file.read()
    return contents
