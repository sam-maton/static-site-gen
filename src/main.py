import os.path
from textnode import TextNode
import os
import shutil

def copy_static_files(path):
    if not os.path.exists(path):
        raise Exception('Invalid path')
    
    shutil.rmtree('public')
    os.mkdir('public')
    
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

def main():
    copy_static_files('static')

if __name__ == "__main__":
    main()