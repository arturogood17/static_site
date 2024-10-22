from textnode import TextNode
from copystatic import copypath
import shutil, os

dir_path_static= "./static"
dir_path_public= "./public"

def main():
    print("Deleting directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copypath(dir_path_static, dir_path_public)



main()