import json
import xml.etree.ElementTree as ET


def xml_file_to_json(file):
    tree = ET.parse(file)
    t = tree.getroot()
    return xmldict(t)


def xmldict(node):
    children = list(node)
    ret = {node.tag: [] if children else ""}
    if children:
        for children_dict in map(xmldict, children):
            ret[node.tag].append(
                {k: v for k, v in children_dict.items()}
            )
    elif node.text and node.text.strip() != '':
        text = node.text.strip()
        ret[node.tag] = text
    return ret