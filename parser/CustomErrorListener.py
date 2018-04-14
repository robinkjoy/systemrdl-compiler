import logging
from antlr4.error.ErrorListener import ErrorListener

log = logging.getLogger()


class CustomErrorListener(ErrorListener):

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(line)
        log.error(f'{column}:{msg}', line)
