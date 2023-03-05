from src.frontmatter import rename_tag


def test_should_rename_matching_tag_with_new_tag():
    post = """
---
tags: [Test-Driven Development, XP]
---
# Content
    """

    result = rename_tag(post, 'Test-Driven Development', 'tdd')

    assert 'Test-Driven Development' not in result
    assert 'tdd' in result
