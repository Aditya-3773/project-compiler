from lexer import Lexer
from parser import Parser
from generator import Generator

def compile_c_to_python(c_filename):
    # Step 0: Read C code
    with open(c_filename, 'r') as f:
        c_code = f.read()

    # Step 0.5: Show the input C code
    print("=== Input C Code ===\n")
    print(c_code)
    print("\n=== End of Input ===\n")

    # Step 1: Lexical Analysis
    lexer = Lexer(c_code)
    tokens = lexer.tokenize()

    # Step 2: Parsing
    parser = Parser(tokens)
    ast = parser.parse()

    # Step 3: Code Generation
    gen = Generator(ast)
    python_code = gen.generate()

    # Step 4: Show generated Python code
    print("=== Generated Python Code ===\n")
    print(python_code)
    print("\n=== End of Generated Code ===\n")

    # Step 5: Run the generated Python code
    print("=== Output of Python Code ===\n")
    exec(python_code)
    print("\n=== End of Output ===")

if __name__ == "__main__":
    compile_c_to_python("input.c")

Hi adi
