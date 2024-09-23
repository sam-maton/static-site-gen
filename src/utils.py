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