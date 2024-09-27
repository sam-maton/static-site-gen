from textnode import TextNode
from website_utils import copy_static_files, generate_pages_reccursive
import shutil
import os

def main():
    if os.path.exists('public'):
        shutil.rmtree('public')
    os.mkdir('public')
    copy_static_files('static')
    generate_pages_reccursive('content', 'template.html', 'public')

if __name__ == "__main__":
    main()