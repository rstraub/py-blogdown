from src.emoji.remove_emoji import remove_emoji_from_post
from tests.post_utils import strip_multiline


def test_should_remove_leading_emoji_from_post_title():
    post = strip_multiline("""
    ---
    title: 🐍 Python3
    ---
    
    content
    """)

    expected = strip_multiline("""
    ---
    title: Python3
    ---
    
    content
    """)

    result = remove_emoji_from_post(post)

    assert result == expected


def test_should_trailing_emoji_from_post_title():
    post = strip_multiline("""
    ---
    title: Python3 🐍
    ---
    
    content
    """)

    expected = strip_multiline("""
    ---
    title: Python3
    ---
    
    content
    """)

    result = remove_emoji_from_post(post)

    assert result == expected
