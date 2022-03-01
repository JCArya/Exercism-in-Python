
class SgfTree:
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []
    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for key, value in self.properties.items():
            if key not in other.properties:
                return False
            if other.properties[key] != value:
                return False
        for key in other.properties.keys():
            if key not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for child, other_child in zip(self.children, other.children):
            if child != other_child:
                return False
        return True
    def __ne__(self, other):
        return not self == other
def parse(input_string):
    import re
    if not input_string:
        raise ValueError('tree missing')
    if input_string == '()':
        raise ValueError('tree with no nodes')
    if not (input_string.startswith('(') and input_string.endswith(')')):
        raise ValueError('tree missing')
    nodes = input_string[1:-1].split(';')
    nodes = [n for n in nodes if n]
    if not nodes:
        return SgfTree()
    root = nodes[0]
    roots = re.findall(r'\w+\[[\\\]\w\s]+\]?\](?:\[.+\])*', root)
    if not roots:
        raise ValueError('properties without delimiter')
    properties = {}
    for root in roots:
        key = re.search(r'^[^\[]+', root).group(0)
        if any([letter == letter.lower() for word in key for letter in word]):
            raise ValueError('property must be in uppercase')
        properties[key] = []
        vals = re.findall(r'\[([\\\]\w\s]+\]?)\]', root)
        for val in vals:
            properties[key].append(val.replace('\\', '').replace('\t', ' '))
    children = []
    for node in nodes[1:]:
        child = {}
        node = node.replace('(', '').replace(')', '')
        key = re.search(r'^[^\[]+', node).group(0)
        if any([letter == letter.lower() for word in key for letter in word]):
            raise ValueError('property must be in uppercase')
        child[key] = []
        vals = re.findall(r'\[([\\\]\w\s]+\]?)\]', node)
        for val in vals:
            child[key].append(val.replace('\\', '').replace('\t', ' '))
        children.append(SgfTree(child))
    return SgfTree(properties, children)
