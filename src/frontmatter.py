import frontmatter


def rename_tag(post, old_tag, new_tag):
    _post = frontmatter.loads(post)

    updated_tags = [new_tag if tag == old_tag else tag for tag in _post['tags']]
    _post['tags'] = updated_tags

    return frontmatter.dumps(_post)
