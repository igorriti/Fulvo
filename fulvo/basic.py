
from fulvo.lexer import Lexer
from fulvo.parser import Parser
from fulvo.interpreter import Interpreter
from fulvo.context import Context
from fulvo.builtIn_const import global_symbol_table


#######################################
# RUN
#######################################
def run(fn, text):
    # Genera token
    lexer = Lexer(fn, text)
    tokens, error = lexer.make_tokens()
    if error: return None, error
    
    # Genera arbol sintactico
    parser = Parser(tokens)
    ast = parser.parse()
    if ast.error: return None, ast.error

    # Correr programa
    interpreter = Interpreter()
    context = Context('<program>')
    context.symbol_table = global_symbol_table
    result = interpreter.visit(ast.node, context)
    
    return result.value, result.error