import pytest

from src.formatting.title_case import title_case_post


@pytest.mark.parametrize('post,expected', [
    ('# titlecase is better', '# Titlecase Is Better'),
    ('## titlecase is better', '## Titlecase Is Better'),
    ('### titlecase is better', '### Titlecase Is Better'),
    ('#### titlecase is better', '#### Titlecase Is Better'),
    ('##### titlecase is better', '##### Titlecase Is Better'),
    ('###### titlecase is better', '###### Titlecase Is Better'),
])
def test_should_title_case_headings(post: str, expected: str):
    assert title_case_post(post) == expected


@pytest.mark.parametrize('post,expected', [
    ("# They're better", "# They're Better"),
    ("# Programmer's bane", "# Programmer's Bane"),
])
def test_should_title_case_difficult_headings(post: str, expected: str):
    assert title_case_post(post) == expected


@pytest.mark.parametrize('post', [
    'titlecase is better',
    'titlecase is #better'
])
def test_should_not_title_case_content(post: str):
    assert title_case_post(post) == post


@pytest.mark.parametrize('post,expected', [
    ("# 6 reasons for TDD", "# 6 Reasons for TDD"),
    ("# Test-driven Development", "# Test-Driven Development"),
])
def test_should_not_title_case_capitalized_headings(post: str, expected: str):
    assert title_case_post(post) == expected


@pytest.mark.parametrize('post', [
    '#titlecase is better'
    '####### titlecase is better'
])
def test_should_not_title_case_invalid_headings(post: str):
    assert title_case_post(post) == post


@pytest.mark.skip(reason='On the roadmap')
def test_should_title_case_all_headings_in_post():
    post = """
    # titlecase is better
    content
    ## it really is
    """

    expected = """
    # Titlecase is Better
    content
    ## It Really Is
    """

    assert title_case_post(post) == expected
