from slugify import slugify
from markdown2 import markdown, markdown_path
from pathlib import Path

htmll = markdown(open(Path.cwd() / 'data/blog/slug-more.md').read(), extras=["metadata"])
print(htmll.metadata)
blog = {
    'pages': [1, 2],
    'posts': {
        'slug-more': {
            'title': 'tits',
            'excerpt': htmll.metadata['excerpt'],
            'text': htmll,
            'metadata': htmll.metadata
        },
        'slug-more-2': {
            'title': 'tits2',
            'excerpt': 'short description.2',
            'text': 'text of the post2',
        },
    }
}