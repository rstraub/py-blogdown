def strip_multiline(post: str) -> str:
    lines = post.splitlines()
    lines = [line.lstrip() for line in lines]
    return '\n'.join(lines).strip()
