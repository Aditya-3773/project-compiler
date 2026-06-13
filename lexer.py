import re

class Lexer:
    def __init__(self, text):  # fixed constructor
        self.text = text
        self.tokens = []
        # Defined grammar for C language tokens
        self.rules = [
            ('MAIN',      r'^int\s+main\(\)'),
            ('DATATYPE',  r'^(int|float|char|double)\b'),
            ('IF',        r'^if\b'),
            ('WHILE',     r'^while\b'),
            ('PRINT',     r'^printf'),
            ('ID',        r'^[a-zA-Z_]\w*'),
            ('NUM',       r'^\d+'),
            ('OP',        r'^[=+*/-]'),
            ('COMP',      r'^[<>]=?|=='),
            ('LPAREN',    r'^\('),
            ('RPAREN',    r'^\)'),
            ('LBRACE',    r'^\{'),
            ('RBRACE',    r'^\}'),
            ('STRING',    r'^"[^"]*"'),
            ('SEMICOLON', r'^;'),
            ('SKIP',      r'^[ \t\n]+'),
        ]

    def tokenize(self):
        code = self.text
        while code:
            matched = False
            for name, pattern in self.rules:
                match = re.match(pattern, code)
                if match:
                    value = match.group()
                    if name != 'SKIP':
                        self.tokens.append((name, value))
                    code = code[len(value):]
                    matched = True
                    break
            if not matched:
                raise SyntaxError(f"Lexer Error: Illegal character '{code[0]}'")
        return self.tokens
