import re

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link
)


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    resList = []
    for node in old_nodes:
        splitted = node.text.split(delimiter)
        if node.text_type != text_type_text:
            resList.append(node)
            continue
        for index, elements in enumerate(splitted):
            if index % 2 == 0 and elements != '':
                resList.append(TextNode(elements,text_type_text))
            elif index % 2 == 1 and elements != '':
                resList.append(TextNode(elements,text_type))
    return resList

def extract_markdown_images(text):
    pattern = r"!\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    pattern = r"\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches

def split_nodes_image(old_nodes):
    resList = []
    for node in old_nodes:
        image_tup = extract_markdown_images(node.text)
        for image in image_tup:
            splitted = node.text.split(f"![{image[0]}]({image[1]})", 1)
            if splitted[0] == '' and splitted[1] == '':
                resList.append(TextNode(image[0],text_type_image,image[1]))
                return resList
            if splitted[0] != '':
                resList.append(TextNode(splitted[0],text_type_text))
                resList.append(TextNode(image[0],text_type_image,image[1]))
            node.text = splitted[1] 
        
    return resList

def split_nodes_link(old_nodes):
    resList = []
    for node in old_nodes:
        image_tup = extract_markdown_links(node.text)
        for image in image_tup:
            splitted = node.text.split(f"[{image[0]}]({image[1]})", 1)
            if splitted[0] == '' and splitted[1] == '':
                resList.append(TextNode(image[0],text_type_image,image[1]))
                return resList
            if splitted[0] != '':
                resList.append(TextNode(splitted[0],text_type_text))
                resList.append(TextNode(image[0],text_type_link,image[1]))
            node.text = splitted[1]
    resList.append(TextNode(node.text,text_type_text))
    return resList