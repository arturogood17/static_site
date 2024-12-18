from markdown_blocks import markdown_to_html_node
import os
from pathlib import Path

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for item in os.listdir(dir_path_content):
        from_path= os.path.join(dir_path_content, item)
        dest_path= os.path.join(dest_dir_path, item)
        if os.path.isfile(from_path): #revisas si es un file
            dest_path= Path(dest_path).with_suffix(".html") #creas el Path de destino con el path normal, el file y un sufijo ".html"
            generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")
    with open(from_path, "r") as file_1:
        md= file_1.read()

    with open(template_path, "r") as file_2:
        template= file_2.read()

    node= markdown_to_html_node(md)
    content= node.to_html()
    title = extract_title(md)

    template= template.replace("{{ Title }}", title)
    template= template.replace("{{ Content }}", content)

    dest_dir_path= os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    with open(dest_path, "w") as to_file:
        to_file.write(template)



def extract_title(markdown):
    content= markdown.strip().split("\n")
    for line in content:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("No title found")