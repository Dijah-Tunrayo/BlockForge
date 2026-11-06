import tree_sitter_python as tspython
from tree_sitter import Language, Parser

# Set up the Python parser
parser = Parser(Language(tspython.language()))

# Broken code: the colon after f(x) is missing
code = b"def f(x)\n    return x\n"
tree = parser.parse(code)

# Show the whole parse tree
print(tree.root_node)


# Walk through the tree and report any error spots
def find_errors(node):
    if node.type == "ERROR" or node.is_missing:
        yield node
    for child in node.children:
        yield from find_errors(child)


for n in find_errors(tree.root_node):
    line = n.start_point[0] + 1
    column = n.start_point[1] + 1
    print(
        f"Problem: type={n.type}, missing={n.is_missing}, line {line}, column {column}"
    )
