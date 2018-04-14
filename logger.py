import logging
import sys


class CustomFormatter(logging.Formatter):
    def __init__(self, debug, line_info=None):
        self.debug = debug
        self.line_info = line_info

    def set_line_info(self, line_info):
        self.line_info = line_info

    def format(self, record):
        if record.args and self.line_info:
            record.msg = '{}({}):'.format(*self.line_info[record.args[0] - 1]) + record.msg
            record.args = record.args[1:]
        if self.debug:
            record.msg = '{}({})::'.format(record.filename, record.lineno) + record.msg
        record.msg = record.msg.format(*record.args)
        record.msg = '{}:'.format(record.levelname) + record.msg
        return record.msg


class NonErrorHandler(logging.Handler):
    def emit(self, record):
        print(self.format(record), file=sys.stdout)

    def filter(self, record):
        return True if record.levelno < logging.ERROR else False


class ErrorHandler(logging.Handler):
    def emit(self, record):
        print(self.format(record), file=sys.stderr)
        logging.shutdown()
        sys.exit()


def setup_logging(level, debug):
    log = logging.getLogger()
    log.setLevel(level)
    error_handler = ErrorHandler(level=logging.ERROR)
    nonerror_handler = NonErrorHandler(level=logging.DEBUG)
    fmt = CustomFormatter(debug)
    error_handler.setFormatter(fmt)
    nonerror_handler.setFormatter(fmt)
    log.addHandler(error_handler)
    log.addHandler(nonerror_handler)
