class ASTNode: 
    pass

class VarDeclNode(ASTNode):
    def __init__(self, name, value):  # fixed constructor
        self.name = name
        self.value = value

class PrintNode(ASTNode):
    def __init__(self, content):  # fixed constructor
        self.content = content

class IfNode(ASTNode):
    def __init__(self, condition, body):  # fixed constructor
        self.condition = condition
        self.body = body

class Parser:
    def __init__(self, tokens):  # fixed constructor
        self.tokens = tokens
        self.pos = 0

    def consume(self, expected_type=None):
        token = self.tokens[self.pos]
        if expected_type and token[0] != expected_type:
            raise Exception(f"Syntax Error: Expected {expected_type} but got {token[0]}")
        self.pos += 1
        return token

    def parse(self):
        nodes = []
        while self.pos < len(self.tokens):
            token_type = self.tokens[self.pos][0]
            if token_type == 'MAIN':
                self.consume('MAIN')
                self.consume('LBRACE')
            elif token_type == 'DATATYPE':
                nodes.append(self.parse_declaration())
            elif token_type == 'PRINT':
                nodes.append(self.parse_print())
            elif token_type == 'IF':
                nodes.append(self.parse_if())
            elif token_type == 'RBRACE':
                self.consume('RBRACE')
            else:
                self.pos += 1
        return nodes

    def parse_declaration(self):
        self.consume('DATATYPE')
        name = self.consume('ID')[1]
        self.consume('OP') 
        val = self.consume('NUM')[1]
        self.consume('SEMICOLON')
        return VarDeclNode(name, val)

    def parse_print(self):
        self.consume('PRINT')
        self.consume('LPAREN')
        content = self.consume('STRING')[1]
        self.consume('RPAREN')
        self.consume('SEMICOLON')
        return PrintNode(content)

    def parse_if(self):
        self.consume('IF')
        self.consume('LPAREN')
        cond = f"{self.consume('ID')[1]} {self.consume('COMP')[1]} {self.consume('NUM')[1]}"
        self.consume('RPAREN')
        self.consume('LBRACE')
        body = [self.parse_print()]  # Simplified: only handles print in if-body
        self.consume('RBRACE')
        return IfNode(cond, body)
