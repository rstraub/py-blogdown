from string import capwords


def title_case_post(post: str) -> str:
    if is_heading(post):
        return capwords(post)
    return post


def is_heading(text: str) -> bool:
    return text.startswith(('#', '##'))