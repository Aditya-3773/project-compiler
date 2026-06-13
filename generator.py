# Import the AST node classes
from parser import VarDeclNode, PrintNode, IfNode

class Generator:
    def __init__(self, ast):
        self.ast = ast
        self.indent = 0

    def generate_node(self, node):
        indent_str = "    " * self.indent
        lines = []

        if isinstance(node, VarDeclNode):
            lines.append(f"{indent_str}{node.name} = {node.value}")
        elif isinstance(node, PrintNode):
            lines.append(f"{indent_str}print({node.content})")
        elif isinstance(node, IfNode):
            lines.append(f"{indent_str}if {node.condition}:")
            self.indent += 1
            for stmt in node.body:
                lines.extend(self.generate_node(stmt))  # recursive call
            self.indent -= 1

        return lines

    def generate(self):
        lines = []
        for node in self.ast:
            lines.extend(self.generate_node(node))
        return "\n".join(lines)
