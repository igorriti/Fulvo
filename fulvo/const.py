import string

#######################################
# CONSTANTS
#######################################

DIGITS = '0123456789'
LETTERS = string.ascii_letters + '_'
LETTERS_DIGITS = LETTERS + DIGITS

#######################################
# TOKENS
#######################################

TT_INT		= 'INT'
TT_FLOAT    = 'FLOAT'
TT_STRING 	= 'STRING'
TT_IDENTIFIER = 'IDENTIFIER'
TT_KEYWORD = 'KEYWORD'
TT_PLUS     = 'PLUS'
TT_MINUS    = 'MINUS'
TT_MUL      = 'MUL'
TT_DIV      = 'DIV'
TT_POW      = 'POW'
TT_EQ       = 'EQ'
TT_EE 		= 'EE'
TT_NE  		= 'NE'
TT_LT  		= 'LT'
TT_GT  		= 'GT'
TT_LTE  	= 'LTE'
TT_GTE  	= 'GTE'
TT_COMMA   	= 'COMMA'
TT_ARROW    = 'ARROW'
TT_LPAREN   = 'LPAREN'
TT_RPAREN   = 'RPAREN'
TT_LSQUARE 	= 'LSQUARE'
TT_RSQUARE 	= 'RSQUARE'
TT_NEWLINE  = 'NEWLINE'
TT_EOF	    = 'EOF'
TT_ASSIGN   = 'ASSIGN'

#######################################
# KEYWORDS
#######################################

KEYWORDS = [
    'Jugador',
	'y',
	'o',
	'no',
	'si',
	'patea',
	'palo',
	'rebote',
	'ArrancaPorLaDerecha',
	'hasta',
	'pasala',
	'mientras',
	'jugada',
	'gol',
	'devuelve',
	'gambetea',
	'falta',
]

#######################################
# ERRORS MESSAGES
#######################################

error_messages = {
	"IllegarlCharError" : "Pipa pipa pipa, no no no. Se te fue por afuera, pusiste ",
	"ExpectedCharError" : "Chequeado con el VAR, te falto ",
	"InvalidSyntaxError" : "No entendi nada. Murió el fútbol. Falleció la pelota. Pareció el balónpie. Agoniza la caprichosa. Se mancho la de cuero. La esferica de luto.",
	"RuntimeError" : "\033[93m Amarilla, la proxima es roja \033[0m"
}

#######################################
# ERRORS DETAILS
#######################################

detail_messages = {
	"expected_int_or_float" : "\nNecesito el NUMERO de camiseta",
	"expected_expr" : "\nHiciste un pase a la nada",
	"expected_op" 	: "\nTirate una gambeta porque sino no pasas a ningun defensa",
	"expected_rparen" : "\nFuera de juego, no pusiste parentesis",
	"expected_identifier" : "\nChe y como se llama el jugador? Digo porque sino no lo puedo anotar en la plantilla viste",
	"expected_equal" : "\nTenes que poner una igualdad, ejemplo Messi = GOAT",
	"expected_not_equal" : "\n Vos te equivocaste y pagaste, pero el codigo no se mancha. Te falto la igualdad",
	"zero_div" : "\nEs mas probable que San Marino gane un partido de fútbol a que puedas dividir por 0",
	"unknown_variable" : "\n No se que jugador es ese, no lo tengo en la planilla a ",
	"syntax_error" : "Viven en un country, andan en BMW para arriba, morfan bien todos los dias. Tan dificil era leer la documentacion?",
	"expected_end" : "Y el gol??? Hacelo, por dios hacelo Cuevas, HACELO CUEVAAAASSS"

}
