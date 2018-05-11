import logging
from antlr4.error.ErrorListener import ErrorListener

log = logging.getLogger()


class CustomErrorListener(ErrorListener):

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        msg = msg.replace('{', '{{')
        msg = msg.replace('}', '}}')
        log.error(f'{column}:{msg}', line)
