from htmlnode import LeafNode
from textnode import *
import re

# Constants
text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

# Functions

def text_node_to_html_node(text_node):
    if text_node.text_type == text_type_text:
        return LeafNode(None, text_node.text)
    if text_node.text_type == text_type_bold:
        return LeafNode('b', text_node.text)
    if text_node.text_type == text_type_italic:
        return LeafNode('i', text_node.text)
    if text_node.text_type == text_type_code:
        return LeafNode('code', text_node.text)
    if text_node.text_type == text_type_link:
        return LeafNode('a', text_node.text, {"href": text_node.url})
    if text_node.text_type == text_type_image:
        return LeafNode('img', '', {"src": text_node.url, "alt": text_node.text})
    
    raise Exception('Text node is not a valid type.')

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        split_nodes = []
        sections = node.text.split(delimiter)

        if len(sections) % 2 == 0:
            raise Exception('Invalid markdown.')
        
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    
    return new_nodes

def extract_markdown_images(text):
    pattern = r"!\[(.*?)\]\((.*?)\)"
    
    matches = re.findall(pattern, text)

    return matches

def extract_markdown_links(text):
    pattern = r"(?<!!)\[(.*?)\]\((.*?)\)"

    matches = re.findall(pattern, text)

    return matches

def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type == text_type_text:
            new_nodes += separate_links_from_text(node.text)
        else:
            new_nodes.append(node)

    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type == text_type_text:
            new_nodes += separate_images_from_text(node.text)
        else:
            new_nodes.append(node)

    return new_nodes

def separate_links_from_text(text):

    if len(text) < 1:
        return []
    
    links = extract_markdown_links(text)

    if len(links) == 0:
        return [TextNode(text, text_type_text)]
    
    for link in links:
        new_link = TextNode(link[0], text_type_link, link[1])
        sections = text.split(f"[{link[0]}]({link[1]})", 1)
        if len(sections[0]) == 0:
            return[new_link] + separate_links_from_text(sections[1])
        else:
            if len(sections[1]) == 0:
                return[TextNode(sections[0], text_type_text), new_link]
            return[TextNode(sections[0], text_type_text), new_link] + separate_links_from_text(sections[1])
    return []

def separate_images_from_text(text):

    if len(text) < 1:
        return []
    
    images = extract_markdown_images(text)

    if len(images) == 0:
        return [TextNode(text, text_type_text)]
    
    for image in images:
        new_image = TextNode(image[0], text_type_image, image[1])
        sections = text.split(f"![{image[0]}]({image[1]})", 1)
        if len(sections[0]) == 0:
            return[new_image] + separate_images_from_text(sections[1])
        else:
            if len(sections[1]) == 0:
                return[TextNode(sections[0], text_type_text), new_image]
            return[TextNode(sections[0], text_type_text), new_image] + separate_images_from_text(sections[1])
    return []

def text_to_textnodes(text):
    starting_node = TextNode(text, text_type_text)
    bold_nodes = split_nodes_delimiter([starting_node], '**', text_type_bold)
    italic_nodes = split_nodes_delimiter(bold_nodes, '*', text_type_italic)
    code_nodes = split_nodes_delimiter(italic_nodes, '`', text_type_code)
    link_nodes = split_nodes_link(code_nodes)
    image_nodes = split_nodes_image(link_nodes)

    return(image_nodes)

string = 'This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)'

converted = text_to_textnodes(string)

for c in converted:
    print(c)