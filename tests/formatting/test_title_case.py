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


@pytest.mark.parametrize('post', [
    'titlecase is better',
    '#titlecase is better'
])
def test_should_not_title_case_content(post: str):
    assert title_case_post(post) == post

