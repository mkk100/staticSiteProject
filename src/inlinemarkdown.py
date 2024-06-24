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
        