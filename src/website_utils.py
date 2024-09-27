import os
import shutil
from markdown_utils import markdown_to_html_node

def extract_title(markdown: str):
    lines = markdown.split('\n')

    if not lines[0].startswith('# '):
        raise Exception('The markdown file is missing a header')
    
    return lines[0].removeprefix('# ')


def copy_static_files(path):
    if not os.path.exists(path):
        raise Exception('Invalid path')
    
    def get_items_to_create(folder, files):
        items = os.listdir(folder)

        for i in items:
            joined_path = os.path.join(folder + '/',i)

            if os.path.isfile(joined_path):
                files.append(joined_path)
            else:
                files.append(joined_path)
                get_items_to_create(joined_path, files)
        
        return files

    items: list[str] = get_items_to_create(path, [])

    for i in items:
        if os.path.isfile(i):
            shutil.copy(i, f"public{i.removeprefix(path)}")
        else:
            os.mkdir(f"public{i.removeprefix(path)}")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")

    markdown_file = open(from_path, "r")
    markdown = markdown_file.read()
    template_file = open(template_path, "r")
    template = template_file.read()

    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    markdown_file.close()
    template_file.close()


    if not os.path.exists(dest_path):
        os.makedirs(dest_path)
    
    new_html = open(f"{dest_path}/index.html", "w")
    new_html.write(template)
    new_html.close()