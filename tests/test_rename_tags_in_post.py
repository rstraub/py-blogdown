import os
import shutil

import pytest

from src.rename_tags import rename_tags_in_dir


def test_should_rename_matching_tag_with_new_tag():
    tmp_dir = _data_dir_path() + '/tmp/'

    _copy_blogs_to_tmp()

    posts = ['test_post_1.md', 'test_post_2.md']
    rename_tags_in_dir(tmp_dir, 'Scala', 'Python3')

    for post in posts:
        tmp_post_path = tmp_dir + post

        result = _get_post_contents(tmp_post_path)

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


def _copy_blogs_to_tmp():
    tmp_dir = _data_dir_path() + '/tmp'
    if os.path.exists(tmp_dir):
        shutil.rmtree(tmp_dir)
    shutil.copytree(_data_dir_path() + '/input', tmp_dir)


def _data_dir_path():
    # Get the directory of the current script
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # Construct the path to the reference post
    return os.path.join(dir_path, 'data')


def _get_post_contents(blog_path):
    with open(blog_path, 'r') as file:
        contents = file.read()
    return contents
