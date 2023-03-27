import emoji
import frontmatter


def remove_emoji_from_post(post: str) -> str:
    """Removes emoji from a post title and headings"""
    metadata = frontmatter.loads(post)
    replaced_title = emoji.replace_emoji(metadata['title'], '')
    metadata['title'] = replaced_title.strip()

    return frontmatter.dumps(metadata)
