from copystatic import copypath
import shutil, os
from gencontent import generate_pages_recursive


dir_path_static= "/home/nestapon9/workspace/github.com/arturogood17/static_site/static/" #actualizar esto al subirlo
dir_path_public= "/home/nestapon9/workspace/github.com/arturogood17/static_site/public/"
dir_path_content = "/home/nestapon9/workspace/github.com/arturogood17/static_site/content/"
template_path = "/home/nestapon9/workspace/github.com/arturogood17/static_site/template.html"

def main():
    print("Deleting directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copypath(dir_path_static, dir_path_public)

    print("Generating page...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_public)



main()