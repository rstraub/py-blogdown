import frontmatter


def rename_tag(post, old_tag, new_tag):
    content = frontmatter.loads(post)

    content['tags'] = [new_tag if tag == old_tag else tag for tag in content['tags']]

    return frontmatter.dumps(content)
