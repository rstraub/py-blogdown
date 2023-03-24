import re
from titlecase import titlecase


def title_case_post(post: str) -> str:
    if not is_heading(post):
        return post

    return titlecase(post)


def is_heading(text: str) -> bool:
    regex = re.compile(r'^#{1,6} ')
    return bool(regex.match(text))
