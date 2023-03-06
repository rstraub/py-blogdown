from src.metadata.rename_tags import rename_tag


def test_should_rename_matching_tag_with_new_tag():
    post = """
---
tags:
- Test-Driven Development
---

# Content""".strip()

    expected = """
---
tags:
- tdd
---

# Content
""".strip()

    result = rename_tag(post, 'Test-Driven Development', 'tdd')

    assert result == expected
