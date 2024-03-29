import os
import shutil

import pytest

from src.metadata.rename_tags import rename_tags_in_dir, rename_tags_in_post


def _data_dir_path():
    # Get the directory of the current script
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # Construct the path to the reference post
    return os.path.join(dir_path, 'data')


output_dir = _data_dir_path() + '/golden/'
tmp_dir = _data_dir_path() + '/tmp/'


def test_should_rename_tags_in_directory():
    _copy_blogs_to(tmp_dir)

    rename_tags_in_dir(tmp_dir, 'Scala', 'Python3')

    posts = ['test_post_1.md', 'test_post_2.md']
    for post in posts:
        result = _get_post_contents(tmp_dir + post)
        expected = _get_post_contents(output_dir + post)

        assert result == expected


def test_should_rename_tags_in_file():
    post = 'test_post_1.md'

    rename_tags_in_post(tmp_dir + post, 'Scala', 'Python3')

    result = _get_post_contents(tmp_dir + post)
    expected = _get_post_contents(output_dir + post)

    assert result == expected


@pytest.fixture(autouse=True)
def _fixture():
    _copy_blogs_to(tmp_dir)
    yield
    _clean_tmp_dir()


def _get_post_contents(blog_path):
    with open(blog_path, 'r') as file:
        contents = file.read()
    return contents


def _clean_tmp_dir():
    # Get the directory of the current script
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # Construct the path to the tmp folder
    tmp_path = os.path.join(dir_path, 'data/tmp')
    # Delete the contents of the tmp folder
    for file in os.listdir(tmp_path):
        file_path = os.path.join(tmp_path, file)
        os.remove(file_path)


def _copy_blogs_to(dir):
    if os.path.exists(dir):
        shutil.rmtree(dir)
    shutil.copytree(_data_dir_path() + '/input', dir)
