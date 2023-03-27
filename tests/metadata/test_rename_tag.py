from src.metadata.rename_tags import rename_tag
from tests.post_utils import strip_multiline


def test_should_rename_matching_tag_with_new_tag():
    post = strip_multiline("""
    ---
    tags:
    - Test-Driven Development
    ---
    
    # Content
    """)

    expected = strip_multiline("""
    ---
    tags:
    - tdd
    ---
    
    # Content
    """)

    result = rename_tag(post, 'Test-Driven Development', 'tdd')

    assert result == expected
