from src.formatting.title_case import title_case_post


def test_should_title_case_headings():
    post = '# why dumb tests are smart'
    expected = '# Why Dumb Tests Are Smart'

    assert title_case_post(post) == expected


def test_should_not_title_case_content():
    post = 'why dumb tests are smart'

    assert title_case_post(post) == post
