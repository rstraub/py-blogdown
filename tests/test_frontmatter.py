import frontmatter

post = """
    ---
tags: [Test-Driven Development]
---
# Scala
    """


def test_should_parse_frontmatter():
    result = frontmatter.loads(post)

    assert result['tags'] == ['Test-Driven Development']


def test_should_modify_frontmatter():
    result = frontmatter.loads(post)
    result['tags'][0] = 'Test-After Development'

    assert 'Test-After Development' in frontmatter.dumps(result)


def test_should_return_content():
    result = frontmatter.loads(post)

    assert result.content == '# Scala'
