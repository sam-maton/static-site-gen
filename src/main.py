from textnode import TextNode
from website_utils import copy_static_files, generate_page
import shutil
import os

def main():
    shutil.rmtree('public')
    os.mkdir('public')
    copy_static_files('static')
    generate_page('content/index.md', 'template.html', 'public')

if __name__ == "__main__":
    main()