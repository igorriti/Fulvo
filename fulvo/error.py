from fulvo.strings_with_arrows import *
from fulvo.const import error_messages

#######################################
# ERRORS
#######################################

class Error:
    def __init__(self, pos_start, pos_end, error_name, details):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.error_name = error_name
        self.details = details
		
    def as_string(self):
        result  = f'{self.error_name}: {self.details}\n'
        result += f'En {self.pos_start.fn}, el juez cobra falta en {self.pos_start.ln + 1}'
        result += '\n\n' + string_with_arrows(self.pos_start.ftxt, self.pos_start, self.pos_end)
        return result

class IllegalCharError(Error):
    def __init__(self, pos_start, pos_end, details):
        super().__init__(pos_start, pos_end,error_messages["IllegalCharError"], details)

class ExpectedCharError(Error):
	def __init__(self, pos_start, pos_end, details):
		super().__init__(pos_start, pos_end, error_messages["ExpectedCharError"], details)
class InvalidSyntaxError(Error):
    def __init__(self, pos_start, pos_end, details=''):
        super().__init__(pos_start, pos_end, error_messages["InvalidSyntaxError"], details)

class RTError(Error):
    def __init__(self, pos_start, pos_end, details, context):
        super().__init__(pos_start, pos_end, error_messages, details)
        self.context = context
    def as_string(self):
        result = self.generate_traceback()
        result += f'{self.error_name}: {self.details}\n'
        result += '\n\n' + string_with_arrows(self.pos_start.ftxt, self.pos_start, self.pos_end)
        return result

    def generate_traceback(self):
        result = ''
        pos = self.pos_start
        ctx = self.context
        while ctx:
            result = f'  En {pos.fn}, el juez cobra falta {str(pos.ln + 1)}, por {ctx.display_name}\n' + result
            pos = ctx.parent_entry_pos
            ctx = ctx.parent
        return 'Repeticion de la jugada:\n' + result