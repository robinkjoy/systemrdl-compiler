from antlr4.error.ErrorListener import ErrorListener

class CustomErrorListener(ErrorListener):
    
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        exit('error:{}:{} {}'.format(line, column, msg))
