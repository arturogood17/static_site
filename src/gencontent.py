from markdown_blocks import markdown_to_html_node
import os

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")
    with open(from_path, "r") as file_1:
        md= file_1.read()

    with open(template_path, "r") as file_2:
        template= file_2.read()

    content= markdown_to_html_node(md).to_html()
    title = extract_title(md)

    template= template.replace("{{ Title }}", title)
    template= template.replace("{{ Content }}", content)

    dest_dir_path= os.path.dirname(dest_path)
    if dest_dir_path == "":
        os.makedirs(dest_dir_path, exist_ok=True)
    with open(dest_path, "w") as to_file:
        to_file.write(template)



def extract_title(markdown):
    content= markdown.strip().split("\n")
    first_heading = content[0]
    if not first_heading.startswith("# "):
        raise Exception("Title not found.")
    return first_heading.strip("# ")