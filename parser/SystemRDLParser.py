# Generated from java-escape by ANTLR 4.5
# encoding: utf-8
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .SystemRDLListener import SystemRDLListener
else:
    from SystemRDLListener import SystemRDLListener
def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\u0085")
        buf.write("\u0176\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\3\2\3\2\3\2")
        buf.write("\3\2\3\2\7\2N\n\2\f\2\16\2Q\13\2\3\2\3\2\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\4\3\4\3\4\5\4_\n\4\3\4\3\4\3\4\5\4d\n")
        buf.write("\4\3\4\3\4\3\4\5\4i\n\4\3\4\3\4\3\4\5\4n\n\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\5\4w\n\4\5\4y\n\4\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\5\5\u0081\n\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\5")
        buf.write("\6\u008b\n\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\7\7\u0094\n\7")
        buf.write("\f\7\16\7\u0097\13\7\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3")
        buf.write("\13\3\13\3\f\3\f\3\r\3\r\3\r\5\r\u00a8\n\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\7\r\u00af\n\r\f\r\16\r\u00b2\13\r\3\r\3\r\5\r")
        buf.write("\u00b6\n\r\3\r\3\r\3\16\5\16\u00bb\n\16\3\16\5\16\u00be")
        buf.write("\n\16\3\16\3\16\5\16\u00c2\n\16\3\16\3\16\3\16\3\16\7")
        buf.write("\16\u00c8\n\16\f\16\16\16\u00cb\13\16\3\16\3\16\3\17\5")
        buf.write("\17\u00d0\n\17\3\17\3\17\3\17\7\17\u00d5\n\17\f\17\16")
        buf.write("\17\u00d8\13\17\3\20\3\20\5\20\u00dc\n\20\3\20\3\20\5")
        buf.write("\20\u00e0\n\20\3\20\3\20\5\20\u00e4\n\20\3\20\3\20\5\20")
        buf.write("\u00e8\n\20\3\20\3\20\5\20\u00ec\n\20\3\21\3\21\3\21\3")
        buf.write("\21\5\21\u00f2\n\21\3\21\3\21\3\22\3\22\3\22\7\22\u00f9")
        buf.write("\n\22\f\22\16\22\u00fc\13\22\3\22\3\22\5\22\u0100\n\22")
        buf.write("\3\23\3\23\3\23\3\23\3\23\5\23\u0107\n\23\3\24\3\24\3")
        buf.write("\24\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u0112\n\24\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u011e")
        buf.write("\n\26\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\5\30")
        buf.write("\u0129\n\30\3\31\3\31\3\31\3\31\7\31\u012f\n\31\f\31\16")
        buf.write("\31\u0132\13\31\3\31\3\31\3\32\3\32\5\32\u0138\n\32\3")
        buf.write("\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\5\34\u014a\n\34\3\35\3\35\3")
        buf.write("\36\3\36\3\37\3\37\3 \3 \3!\3!\3!\3!\3!\3\"\3\"\7\"\u015b")
        buf.write("\n\"\f\"\16\"\u015e\13\"\3\"\3\"\3#\3#\3#\3#\3#\7#\u0167")
        buf.write("\n#\f#\16#\u016a\13#\3#\5#\u016d\n#\3#\3#\3$\3$\3$\3$")
        buf.write("\3$\3$\2\2%\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"")
        buf.write("$&(*,.\60\62\64\668:<>@BDF\2\t\3\2\t\16\4\2\n\r\22\22")
        buf.write("\3\2\t\r\5\2\24\24\27`\u0085\u0085\3\2im\4\2qq\u0084\u0084")
        buf.write("\3\2\27\30\u0192\2O\3\2\2\2\4T\3\2\2\2\6x\3\2\2\2\bz\3")
        buf.write("\2\2\2\n\u0084\3\2\2\2\f\u008e\3\2\2\2\16\u009a\3\2\2")
        buf.write("\2\20\u009c\3\2\2\2\22\u009e\3\2\2\2\24\u00a0\3\2\2\2")
        buf.write("\26\u00a2\3\2\2\2\30\u00a4\3\2\2\2\32\u00ba\3\2\2\2\34")
        buf.write("\u00cf\3\2\2\2\36\u00d9\3\2\2\2 \u00ed\3\2\2\2\"\u00f5")
        buf.write("\3\2\2\2$\u0101\3\2\2\2&\u0111\3\2\2\2(\u0113\3\2\2\2")
        buf.write("*\u011d\3\2\2\2,\u011f\3\2\2\2.\u0128\3\2\2\2\60\u012a")
        buf.write("\3\2\2\2\62\u0137\3\2\2\2\64\u0139\3\2\2\2\66\u0149\3")
        buf.write("\2\2\28\u014b\3\2\2\2:\u014d\3\2\2\2<\u014f\3\2\2\2>\u0151")
        buf.write("\3\2\2\2@\u0153\3\2\2\2B\u0158\3\2\2\2D\u0161\3\2\2\2")
        buf.write("F\u0170\3\2\2\2HN\5\30\r\2IN\5@!\2JN\5\32\16\2KN\5&\24")
        buf.write("\2LN\5\4\3\2MH\3\2\2\2MI\3\2\2\2MJ\3\2\2\2MK\3\2\2\2M")
        buf.write("L\3\2\2\2NQ\3\2\2\2OM\3\2\2\2OP\3\2\2\2PR\3\2\2\2QO\3")
        buf.write("\2\2\2RS\7\2\2\3S\3\3\2\2\2TU\7\3\2\2UV\5:\36\2VW\7t\2")
        buf.write("\2WX\5\6\4\2XY\7u\2\2YZ\7|\2\2Z\5\3\2\2\2[c\5\b\5\2\\")
        buf.write("^\5\f\7\2]_\5\n\6\2^]\3\2\2\2^_\3\2\2\2_d\3\2\2\2`a\5")
        buf.write("\n\6\2ab\5\f\7\2bd\3\2\2\2c\\\3\2\2\2c`\3\2\2\2dy\3\2")
        buf.write("\2\2em\5\f\7\2fh\5\b\5\2gi\5\n\6\2hg\3\2\2\2hi\3\2\2\2")
        buf.write("in\3\2\2\2jk\5\n\6\2kl\5\b\5\2ln\3\2\2\2mf\3\2\2\2mj\3")
        buf.write("\2\2\2ny\3\2\2\2ov\5\n\6\2pq\5\b\5\2qr\5\f\7\2rw\3\2\2")
        buf.write("\2st\5\f\7\2tu\5\b\5\2uw\3\2\2\2vp\3\2\2\2vs\3\2\2\2w")
        buf.write("y\3\2\2\2x[\3\2\2\2xe\3\2\2\2xo\3\2\2\2y\7\3\2\2\2z{\7")
        buf.write("\4\2\2{\u0080\7\u0081\2\2|\u0081\5\22\n\2}\u0081\5\24")
        buf.write("\13\2~\u0081\5\20\t\2\177\u0081\5\26\f\2\u0080|\3\2\2")
        buf.write("\2\u0080}\3\2\2\2\u0080~\3\2\2\2\u0080\177\3\2\2\2\u0081")
        buf.write("\u0082\3\2\2\2\u0082\u0083\7|\2\2\u0083\t\3\2\2\2\u0084")
        buf.write("\u0085\7\5\2\2\u0085\u008a\7\u0081\2\2\u0086\u008b\5>")
        buf.write(" \2\u0087\u008b\5<\37\2\u0088\u008b\7\6\2\2\u0089\u008b")
        buf.write("\7\7\2\2\u008a\u0086\3\2\2\2\u008a\u0087\3\2\2\2\u008a")
        buf.write("\u0088\3\2\2\2\u008a\u0089\3\2\2\2\u008b\u008c\3\2\2\2")
        buf.write("\u008c\u008d\7|\2\2\u008d\13\3\2\2\2\u008e\u008f\7\b\2")
        buf.write("\2\u008f\u0090\7\u0081\2\2\u0090\u0095\5\16\b\2\u0091")
        buf.write("\u0092\7{\2\2\u0092\u0094\5\16\b\2\u0093\u0091\3\2\2\2")
        buf.write("\u0094\u0097\3\2\2\2\u0095\u0093\3\2\2\2\u0095\u0096\3")
        buf.write("\2\2\2\u0096\u0098\3\2\2\2\u0097\u0095\3\2\2\2\u0098\u0099")
        buf.write("\7|\2\2\u0099\r\3\2\2\2\u009a\u009b\t\2\2\2\u009b\17\3")
        buf.write("\2\2\2\u009c\u009d\7\17\2\2\u009d\21\3\2\2\2\u009e\u009f")
        buf.write("\7\20\2\2\u009f\23\3\2\2\2\u00a0\u00a1\7\21\2\2\u00a1")
        buf.write("\25\3\2\2\2\u00a2\u00a3\t\3\2\2\u00a3\27\3\2\2\2\u00a4")
        buf.write("\u00a7\t\4\2\2\u00a5\u00a8\5:\36\2\u00a6\u00a8\3\2\2\2")
        buf.write("\u00a7\u00a5\3\2\2\2\u00a7\u00a6\3\2\2\2\u00a8\u00a9\3")
        buf.write("\2\2\2\u00a9\u00b0\7t\2\2\u00aa\u00af\5\30\r\2\u00ab\u00af")
        buf.write("\5\32\16\2\u00ac\u00af\5&\24\2\u00ad\u00af\5@!\2\u00ae")
        buf.write("\u00aa\3\2\2\2\u00ae\u00ab\3\2\2\2\u00ae\u00ac\3\2\2\2")
        buf.write("\u00ae\u00ad\3\2\2\2\u00af\u00b2\3\2\2\2\u00b0\u00ae\3")
        buf.write("\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00b3\3\2\2\2\u00b2\u00b0")
        buf.write("\3\2\2\2\u00b3\u00b5\7u\2\2\u00b4\u00b6\5\34\17\2\u00b5")
        buf.write("\u00b4\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\u00b7\3\2\2\2")
        buf.write("\u00b7\u00b8\7|\2\2\u00b8\31\3\2\2\2\u00b9\u00bb\7\23")
        buf.write("\2\2\u00ba\u00b9\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00bd")
        buf.write("\3\2\2\2\u00bc\u00be\7\24\2\2\u00bd\u00bc\3\2\2\2\u00bd")
        buf.write("\u00be\3\2\2\2\u00be\u00c1\3\2\2\2\u00bf\u00c0\7\25\2")
        buf.write("\2\u00c0\u00c2\5:\36\2\u00c1\u00bf\3\2\2\2\u00c1\u00c2")
        buf.write("\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\u00c4\5:\36\2\u00c4")
        buf.write("\u00c9\5\36\20\2\u00c5\u00c6\7~\2\2\u00c6\u00c8\5\36\20")
        buf.write("\2\u00c7\u00c5\3\2\2\2\u00c8\u00cb\3\2\2\2\u00c9\u00c7")
        buf.write("\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca\u00cc\3\2\2\2\u00cb")
        buf.write("\u00c9\3\2\2\2\u00cc\u00cd\7|\2\2\u00cd\33\3\2\2\2\u00ce")
        buf.write("\u00d0\7\23\2\2\u00cf\u00ce\3\2\2\2\u00cf\u00d0\3\2\2")
        buf.write("\2\u00d0\u00d1\3\2\2\2\u00d1\u00d6\5\36\20\2\u00d2\u00d3")
        buf.write("\7~\2\2\u00d3\u00d5\5\36\20\2\u00d4\u00d2\3\2\2\2\u00d5")
        buf.write("\u00d8\3\2\2\2\u00d6\u00d4\3\2\2\2\u00d6\u00d7\3\2\2\2")
        buf.write("\u00d7\35\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d9\u00db\5:\36")
        buf.write("\2\u00da\u00dc\5 \21\2\u00db\u00da\3\2\2\2\u00db\u00dc")
        buf.write("\3\2\2\2\u00dc\u00df\3\2\2\2\u00dd\u00de\7\u0081\2\2\u00de")
        buf.write("\u00e0\5<\37\2\u00df\u00dd\3\2\2\2\u00df\u00e0\3\2\2\2")
        buf.write("\u00e0\u00e3\3\2\2\2\u00e1\u00e2\7z\2\2\u00e2\u00e4\5")
        buf.write("<\37\2\u00e3\u00e1\3\2\2\2\u00e3\u00e4\3\2\2\2\u00e4\u00e7")
        buf.write("\3\2\2\2\u00e5\u00e6\7\u0082\2\2\u00e6\u00e8\5<\37\2\u00e7")
        buf.write("\u00e5\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8\u00eb\3\2\2\2")
        buf.write("\u00e9\u00ea\7\u0083\2\2\u00ea\u00ec\5<\37\2\u00eb\u00e9")
        buf.write("\3\2\2\2\u00eb\u00ec\3\2\2\2\u00ec\37\3\2\2\2\u00ed\u00ee")
        buf.write("\7v\2\2\u00ee\u00f1\5<\37\2\u00ef\u00f0\7}\2\2\u00f0\u00f2")
        buf.write("\5<\37\2\u00f1\u00ef\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2")
        buf.write("\u00f3\3\2\2\2\u00f3\u00f4\7w\2\2\u00f4!\3\2\2\2\u00f5")
        buf.write("\u00fa\5$\23\2\u00f6\u00f7\7\177\2\2\u00f7\u00f9\5$\23")
        buf.write("\2\u00f8\u00f6\3\2\2\2\u00f9\u00fc\3\2\2\2\u00fa\u00f8")
        buf.write("\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb\u00ff\3\2\2\2\u00fc")
        buf.write("\u00fa\3\2\2\2\u00fd\u00fe\7\u0080\2\2\u00fe\u0100\5\64")
        buf.write("\33\2\u00ff\u00fd\3\2\2\2\u00ff\u0100\3\2\2\2\u0100#\3")
        buf.write("\2\2\2\u0101\u0106\5:\36\2\u0102\u0103\7v\2\2\u0103\u0104")
        buf.write("\5<\37\2\u0104\u0105\7w\2\2\u0105\u0107\3\2\2\2\u0106")
        buf.write("\u0102\3\2\2\2\u0106\u0107\3\2\2\2\u0107%\3\2\2\2\u0108")
        buf.write("\u0109\5(\25\2\u0109\u010a\7|\2\2\u010a\u0112\3\2\2\2")
        buf.write("\u010b\u010c\5*\26\2\u010c\u010d\7|\2\2\u010d\u0112\3")
        buf.write("\2\2\2\u010e\u010f\5,\27\2\u010f\u0110\7|\2\2\u0110\u0112")
        buf.write("\3\2\2\2\u0111\u0108\3\2\2\2\u0111\u010b\3\2\2\2\u0111")
        buf.write("\u010e\3\2\2\2\u0112\'\3\2\2\2\u0113\u0114\7\5\2\2\u0114")
        buf.write("\u0115\5*\26\2\u0115)\3\2\2\2\u0116\u0117\58\35\2\u0117")
        buf.write("\u0118\5\64\33\2\u0118\u011e\3\2\2\2\u0119\u011a\5\64")
        buf.write("\33\2\u011a\u011b\7\u0081\2\2\u011b\u011c\5.\30\2\u011c")
        buf.write("\u011e\3\2\2\2\u011d\u0116\3\2\2\2\u011d\u0119\3\2\2\2")
        buf.write("\u011e+\3\2\2\2\u011f\u0120\5\"\22\2\u0120\u0121\7\u0081")
        buf.write("\2\2\u0121\u0122\5.\30\2\u0122-\3\2\2\2\u0123\u0129\5")
        buf.write("\66\34\2\u0124\u0125\7\26\2\2\u0125\u0129\5B\"\2\u0126")
        buf.write("\u0129\5\"\22\2\u0127\u0129\5\60\31\2\u0128\u0123\3\2")
        buf.write("\2\2\u0128\u0124\3\2\2\2\u0128\u0126\3\2\2\2\u0128\u0127")
        buf.write("\3\2\2\2\u0129/\3\2\2\2\u012a\u012b\7t\2\2\u012b\u0130")
        buf.write("\5\62\32\2\u012c\u012d\7~\2\2\u012d\u012f\5\62\32\2\u012e")
        buf.write("\u012c\3\2\2\2\u012f\u0132\3\2\2\2\u0130\u012e\3\2\2\2")
        buf.write("\u0130\u0131\3\2\2\2\u0131\u0133\3\2\2\2\u0132\u0130\3")
        buf.write("\2\2\2\u0133\u0134\7u\2\2\u0134\61\3\2\2\2\u0135\u0138")
        buf.write("\5\"\22\2\u0136\u0138\5<\37\2\u0137\u0135\3\2\2\2\u0137")
        buf.write("\u0136\3\2\2\2\u0138\63\3\2\2\2\u0139\u013a\t\5\2\2\u013a")
        buf.write("\65\3\2\2\2\u013b\u014a\7\6\2\2\u013c\u014a\7\7\2\2\u013d")
        buf.write("\u014a\7a\2\2\u013e\u014a\7b\2\2\u013f\u014a\7c\2\2\u0140")
        buf.write("\u014a\7d\2\2\u0141\u014a\7e\2\2\u0142\u014a\7f\2\2\u0143")
        buf.write("\u014a\7g\2\2\u0144\u014a\7h\2\2\u0145\u014a\7S\2\2\u0146")
        buf.write("\u014a\7R\2\2\u0147\u014a\5<\37\2\u0148\u014a\5> \2\u0149")
        buf.write("\u013b\3\2\2\2\u0149\u013c\3\2\2\2\u0149\u013d\3\2\2\2")
        buf.write("\u0149\u013e\3\2\2\2\u0149\u013f\3\2\2\2\u0149\u0140\3")
        buf.write("\2\2\2\u0149\u0141\3\2\2\2\u0149\u0142\3\2\2\2\u0149\u0143")
        buf.write("\3\2\2\2\u0149\u0144\3\2\2\2\u0149\u0145\3\2\2\2\u0149")
        buf.write("\u0146\3\2\2\2\u0149\u0147\3\2\2\2\u0149\u0148\3\2\2\2")
        buf.write("\u014a\67\3\2\2\2\u014b\u014c\t\6\2\2\u014c9\3\2\2\2\u014d")
        buf.write("\u014e\t\7\2\2\u014e;\3\2\2\2\u014f\u0150\7r\2\2\u0150")
        buf.write("=\3\2\2\2\u0151\u0152\7s\2\2\u0152?\3\2\2\2\u0153\u0154")
        buf.write("\7\26\2\2\u0154\u0155\5:\36\2\u0155\u0156\5B\"\2\u0156")
        buf.write("\u0157\7|\2\2\u0157A\3\2\2\2\u0158\u015c\7t\2\2\u0159")
        buf.write("\u015b\5D#\2\u015a\u0159\3\2\2\2\u015b\u015e\3\2\2\2\u015c")
        buf.write("\u015a\3\2\2\2\u015c\u015d\3\2\2\2\u015d\u015f\3\2\2\2")
        buf.write("\u015e\u015c\3\2\2\2\u015f\u0160\7u\2\2\u0160C\3\2\2\2")
        buf.write("\u0161\u0162\5:\36\2\u0162\u0163\7\u0081\2\2\u0163\u016c")
        buf.write("\5<\37\2\u0164\u0168\7t\2\2\u0165\u0167\5F$\2\u0166\u0165")
        buf.write("\3\2\2\2\u0167\u016a\3\2\2\2\u0168\u0166\3\2\2\2\u0168")
        buf.write("\u0169\3\2\2\2\u0169\u016b\3\2\2\2\u016a\u0168\3\2\2\2")
        buf.write("\u016b\u016d\7u\2\2\u016c\u0164\3\2\2\2\u016c\u016d\3")
        buf.write("\2\2\2\u016d\u016e\3\2\2\2\u016e\u016f\7|\2\2\u016fE\3")
        buf.write("\2\2\2\u0170\u0171\t\b\2\2\u0171\u0172\7\u0081\2\2\u0172")
        buf.write("\u0173\5> \2\u0173\u0174\7|\2\2\u0174G\3\2\2\2)MO^chm")
        buf.write("vx\u0080\u008a\u0095\u00a7\u00ae\u00b0\u00b5\u00ba\u00bd")
        buf.write("\u00c1\u00c9\u00cf\u00d6\u00db\u00df\u00e3\u00e7\u00eb")
        buf.write("\u00f1\u00fa\u00ff\u0106\u0111\u011d\u0128\u0130\u0137")
        buf.write("\u0149\u015c\u0168\u016c")
        return buf.getvalue()


class SystemRDLParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'property'", u"'type'", u"'default'", 
                     u"'true'", u"'false'", u"'component'", u"'signal'", 
                     u"'addrmap'", u"'reg'", u"'regfile'", u"'field'", u"'all'", 
                     u"'boolean'", u"'string'", u"'number'", u"'ref'", u"'external'", 
                     u"'internal'", u"'alias'", u"'enum'", u"'name'", u"'desc'", 
                     u"'arbiter'", u"'rset'", u"'rclr'", u"'woclr'", u"'woset'", 
                     u"'we'", u"'wel'", u"'swwe'", u"'swwel'", u"'hwset'", 
                     u"'hwclr'", u"'swmod'", u"'swacc'", u"'sticky'", u"'stickybit'", 
                     u"'intr'", u"'anded'", u"'ored'", u"'xored'", u"'counter'", 
                     u"'overflow'", u"'sharedextbus'", u"'errextbus'", u"'reset'", 
                     u"'littleendian'", u"'bigendian'", u"'rsvdset'", u"'rsvdsetX'", 
                     u"'bridge'", u"'shared'", u"'msb0'", u"'lsb0'", u"'sync'", 
                     u"'async'", u"'cpuif_reset'", u"'field_reset'", u"'activehigh'", 
                     u"'activelow'", u"'singlepulse'", u"'underflow'", u"'incr'", 
                     u"'decr'", u"'incrwidth'", u"'decrwidth'", u"'incrvalue'", 
                     u"'decrvalue'", u"'saturate'", u"'decrsaturate'", u"'threshold'", 
                     u"'decrthreshold'", u"'dontcompare'", u"'donttest'", 
                     u"'alignment'", u"'regwidth'", u"'fieldwidth'", u"'signalwidth'", 
                     u"'accesswidth'", u"'sw'", u"'hw'", u"'addressing'", 
                     u"'precedence'", u"'encode'", u"'resetsignal'", u"'clock'", 
                     u"'mask'", u"'enable'", u"'hwenable'", u"'hwmask'", 
                     u"'haltmask'", u"'haltenable'", u"'halt'", u"'next'", 
                     u"'rw'", u"'wr'", u"'r'", u"'w'", u"'na'", u"'compact'", 
                     u"'regalign'", u"'fullalign'", u"'posedge'", u"'negedge'", 
                     u"'bothedge'", u"'level'", u"'nonsticky'", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"'{'", u"'}'", u"'['", u"']'", u"'('", 
                     u"')'", u"'@'", u"'|'", u"';'", u"':'", u"','", u"'.'", 
                     u"'->'", u"'='", u"'+='", u"'%='" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"WS", u"COMMENT", u"LINE_COMMENT", u"ID", u"NUM", 
                      u"STR", u"LBRACE", u"RBRACE", u"LSQ", u"RSQ", u"LPAREN", 
                      u"RPAREN", u"AT", u"OR", u"SEMI", u"COLON", u"COMMA", 
                      u"DOT", u"DREF", u"EQ", u"INC", u"MOD", u"INST_ID", 
                      u"PROPERTY" ]

    RULE_root = 0
    RULE_property_definition = 1
    RULE_property_body = 2
    RULE_property_type = 3
    RULE_property_default = 4
    RULE_property_usage = 5
    RULE_property_component = 6
    RULE_property_boolean_type = 7
    RULE_property_string_type = 8
    RULE_property_number_type = 9
    RULE_property_ref_type = 10
    RULE_component_def = 11
    RULE_explicit_component_inst = 12
    RULE_anonymous_component_inst_elems = 13
    RULE_component_inst_elem = 14
    RULE_array = 15
    RULE_instance_ref = 16
    RULE_instance_ref_elem = 17
    RULE_property_assign = 18
    RULE_default_property_assign = 19
    RULE_explicit_property_assign = 20
    RULE_post_property_assign = 21
    RULE_property_assign_rhs = 22
    RULE_concat = 23
    RULE_concat_elem = 24
    RULE_s_property = 25
    RULE_property_rvalue_constant = 26
    RULE_property_modifier = 27
    RULE_s_id = 28
    RULE_num = 29
    RULE_string = 30
    RULE_enum_def = 31
    RULE_enum_body = 32
    RULE_enum_entry = 33
    RULE_enum_property_assign = 34

    ruleNames =  [ "root", "property_definition", "property_body", "property_type", 
                   "property_default", "property_usage", "property_component", 
                   "property_boolean_type", "property_string_type", "property_number_type", 
                   "property_ref_type", "component_def", "explicit_component_inst", 
                   "anonymous_component_inst_elems", "component_inst_elem", 
                   "array", "instance_ref", "instance_ref_elem", "property_assign", 
                   "default_property_assign", "explicit_property_assign", 
                   "post_property_assign", "property_assign_rhs", "concat", 
                   "concat_elem", "s_property", "property_rvalue_constant", 
                   "property_modifier", "s_id", "num", "string", "enum_def", 
                   "enum_body", "enum_entry", "enum_property_assign" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    T__40=41
    T__41=42
    T__42=43
    T__43=44
    T__44=45
    T__45=46
    T__46=47
    T__47=48
    T__48=49
    T__49=50
    T__50=51
    T__51=52
    T__52=53
    T__53=54
    T__54=55
    T__55=56
    T__56=57
    T__57=58
    T__58=59
    T__59=60
    T__60=61
    T__61=62
    T__62=63
    T__63=64
    T__64=65
    T__65=66
    T__66=67
    T__67=68
    T__68=69
    T__69=70
    T__70=71
    T__71=72
    T__72=73
    T__73=74
    T__74=75
    T__75=76
    T__76=77
    T__77=78
    T__78=79
    T__79=80
    T__80=81
    T__81=82
    T__82=83
    T__83=84
    T__84=85
    T__85=86
    T__86=87
    T__87=88
    T__88=89
    T__89=90
    T__90=91
    T__91=92
    T__92=93
    T__93=94
    T__94=95
    T__95=96
    T__96=97
    T__97=98
    T__98=99
    T__99=100
    T__100=101
    T__101=102
    T__102=103
    T__103=104
    T__104=105
    T__105=106
    T__106=107
    WS=108
    COMMENT=109
    LINE_COMMENT=110
    ID=111
    NUM=112
    STR=113
    LBRACE=114
    RBRACE=115
    LSQ=116
    RSQ=117
    LPAREN=118
    RPAREN=119
    AT=120
    OR=121
    SEMI=122
    COLON=123
    COMMA=124
    DOT=125
    DREF=126
    EQ=127
    INC=128
    MOD=129
    INST_ID=130
    PROPERTY=131

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class RootContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(SystemRDLParser.EOF, 0)

        def component_def(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SystemRDLParser.Component_defContext)
            else:
                return self.getTypedRuleContext(SystemRDLParser.Component_defContext,i)


        def enum_def(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SystemRDLParser.Enum_defContext)
            else:
                return self.getTypedRuleContext(SystemRDLParser.Enum_defContext,i)


        def explicit_component_inst(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SystemRDLParser.Explicit_component_instContext)
            else:
                return self.getTypedRuleContext(SystemRDLParser.Explicit_component_instContext,i)


        def property_assign(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SystemRDLParser.Property_assignContext)
            else:
                return self.getTypedRuleContext(SystemRDLParser.Property_assignContext,i)


        def property_definition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SystemRDLParser.Property_definitionContext)
            else:
                return self.getTypedRuleContext(SystemRDLParser.Property_definitionContext,i)


        def getRuleIndex(self):
            return SystemRDLParser.RULE_root

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.enterRoot(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.exitRoot(self)




    def root(self):

        localctx = SystemRDLParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SystemRDLParser.T__0) | (1 << SystemRDLParser.T__2) | (1 << SystemRDLParser.T__6) | (1 << SystemRDLParser.T__7) | (1 << SystemRDLParser.T__8) | (1 << SystemRDLParser.T__9) | (1 << SystemRDLParser.T__10) | (1 << SystemRDLParser.T__16) | (1 << SystemRDLParser.T__17) | (1 << SystemRDLParser.T__18) | (1 << SystemRDLParser.T__19) | (1 << SystemRDLParser.T__20) | (1 << SystemRDLParser.T__21) | (1 << SystemRDLParser.T__22) | (1 << SystemRDLParser.T__23) | (1 << SystemRDLParser.T__24) | (1 << SystemRDLParser.T__25) | (1 << SystemRDLParser.T__26) | (1 << SystemRDLParser.T__27) | (1 << SystemRDLParser.T__28) | (1 << SystemRDLParser.T__29) | (1 << SystemRDLParser.T__30) | (1 << SystemRDLParser.T__31) | (1 << SystemRDLParser.T__32) | (1 << SystemRDLParser.T__33) | (1 << SystemRDLParser.T__34) | (1 << SystemRDLParser.T__35) | (1 << SystemRDLParser.T__36) | (1 << SystemRDLParser.T__37) | (1 << SystemRDLParser.T__38) | (1 << SystemRDLParser.T__39) | (1 << SystemRDLParser.T__40) | (1 << SystemRDLParser.T__41) | (1 << SystemRDLParser.T__42) | (1 << SystemRDLParser.T__43) | (1 << SystemRDLParser.T__44) | (1 << SystemRDLParser.T__45) | (1 << SystemRDLParser.T__46) | (1 << SystemRDLParser.T__47) | (1 << SystemRDLParser.T__48) | (1 << SystemRDLParser.T__49) | (1 << SystemRDLParser.T__50) | (1 << SystemRDLParser.T__51) | (1 << SystemRDLParser.T__52) | (1 << SystemRDLParser.T__53) | (1 << SystemRDLParser.T__54) | (1 << SystemRDLParser.T__55) | (1 << SystemRDLParser.T__56) | (1 << SystemRDLParser.T__57) | (1 << SystemRDLParser.T__58) | (1 << SystemRDLParser.T__59) | (1 << SystemRDLParser.T__60) | (1 << SystemRDLParser.T__61) | (1 << SystemRDLParser.T__62))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (SystemRDLParser.T__63 - 64)) | (1 << (SystemRDLParser.T__64 - 64)) | (1 << (SystemRDLParser.T__65 - 64)) | (1 << (SystemRDLParser.T__66 - 64)) | (1 << (SystemRDLParser.T__67 - 64)) | (1 << (SystemRDLParser.T__68 - 64)) | (1 << (SystemRDLParser.T__69 - 64)) | (1 << (SystemRDLParser.T__70 - 64)) | (1 << (SystemRDLParser.T__71 - 64)) | (1 << (SystemRDLParser.T__72 - 64)) | (1 << (SystemRDLParser.T__73 - 64)) | (1 << (SystemRDLParser.T__74 - 64)) | (1 << (SystemRDLParser.T__75 - 64)) | (1 << (SystemRDLParser.T__76 - 64)) | (1 << (SystemRDLParser.T__77 - 64)) | (1 << (SystemRDLParser.T__78 - 64)) | (1 << (SystemRDLParser.T__79 - 64)) | (1 << (SystemRDLParser.T__80 - 64)) | (1 << (SystemRDLParser.T__81 - 64)) | (1 << (SystemRDLParser.T__82 - 64)) | (1 << (SystemRDLParser.T__83 - 64)) | (1 << (SystemRDLParser.T__84 - 64)) | (1 << (SystemRDLParser.T__85 - 64)) | (1 << (SystemRDLParser.T__86 - 64)) | (1 << (SystemRDLParser.T__87 - 64)) | (1 << (SystemRDLParser.T__88 - 64)) | (1 << (SystemRDLParser.T__89 - 64)) | (1 << (SystemRDLParser.T__90 - 64)) | (1 << (SystemRDLParser.T__91 - 64)) | (1 << (SystemRDLParser.T__92 - 64)) | (1 << (SystemRDLParser.T__93 - 64)) | (1 << (SystemRDLParser.T__102 - 64)) | (1 << (SystemRDLParser.T__103 - 64)) | (1 << (SystemRDLParser.T__104 - 64)) | (1 << (SystemRDLParser.T__105 - 64)) | (1 << (SystemRDLParser.T__106 - 64)) | (1 << (SystemRDLParser.ID - 64)))) != 0) or _la==SystemRDLParser.INST_ID or _la==SystemRDLParser.PROPERTY:
                self.state = 75
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 70
                    self.component_def()
                    pass

                elif la_ == 2:
                    self.state = 71
                    self.enum_def()
                    pass

                elif la_ == 3:
                    self.state = 72
                    self.explicit_component_inst()
                    pass

                elif la_ == 4:
                    self.state = 73
                    self.property_assign()
                    pass

                elif la_ == 5:
                    self.state = 74
                    self.property_definition()
                    pass


                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 80
            self.match(SystemRDLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Property_definitionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def s_id(self):
            return self.getTypedRuleContext(SystemRDLParser.S_idContext,0)


        def LBRACE(self):
            return self.getToken(SystemRDLParser.LBRACE, 0)

        def property_body(self):
            return self.getTypedRuleContext(SystemRDLParser.Property_bodyContext,0)


        def RBRACE(self):
            return self.getToken(SystemRDLParser.RBRACE, 0)

        def SEMI(self):
            return self.getToken(SystemRDLParser.SEMI, 0)

        def getRuleIndex(self):
            return SystemRDLParser.RULE_property_definition

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.enterProperty_definition(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.exitProperty_definition(self)




    def property_definition(self):

        localctx = SystemRDLParser.Property_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_property_definition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(SystemRDLParser.T__0)
            self.state = 83
            self.s_id()
            self.state = 84
            self.match(SystemRDLParser.LBRACE)
            self.state = 85
            self.property_body()
            self.state = 86
            self.match(SystemRDLParser.RBRACE)
            self.state = 87
            self.match(SystemRDLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Property_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def property_type(self):
            return self.getTypedRuleContext(SystemRDLParser.Property_typeContext,0)


        def property_usage(self):
            return self.getTypedRuleContext(SystemRDLParser.Property_usageContext,0)


        def property_default(self):
            return self.getTypedRuleContext(SystemRDLParser.Property_defaultContext,0)


        def getRuleIndex(self):
            return SystemRDLParser.RULE_property_body

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.enterProperty_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.exitProperty_body(self)




    def property_body(self):

        localctx = SystemRDLParser.Property_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_property_body)
        self._la = 0 # Token type
        try:
            self.state = 118
            token = self._input.LA(1)
            if token in [SystemRDLParser.T__1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.property_type()
                self.state = 97
                token = self._input.LA(1)
                if token in [SystemRDLParser.T__5]:
                    self.state = 90
                    self.property_usage()
                    self.state = 92
                    _la = self._input.LA(1)
                    if _la==SystemRDLParser.T__2:
                        self.state = 91
                        self.property_default()



                elif token in [SystemRDLParser.T__2]:
                    self.state = 94
                    self.property_default()
                    self.state = 95
                    self.property_usage()

                else:
                    raise NoViableAltException(self)


            elif token in [SystemRDLParser.T__5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 99
                self.property_usage()
                self.state = 107
                token = self._input.LA(1)
                if token in [SystemRDLParser.T__1]:
                    self.state = 100
                    self.property_type()
                    self.state = 102
                    _la = self._input.LA(1)
                    if _la==SystemRDLParser.T__2:
                        self.state = 101
                        self.property_default()



                elif token in [SystemRDLParser.T__2]:
                    self.state = 104
                    self.property_default()
                    self.state = 105
                    self.property_type()

                else:
                    raise NoViableAltException(self)


            elif token in [SystemRDLParser.T__2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 109
                self.property_default()
                self.state = 116
                token = self._input.LA(1)
                if token in [SystemRDLParser.T__1]:
                    self.state = 110
                    self.property_type()
                    self.state = 111
                    self.property_usage()

                elif token in [SystemRDLParser.T__5]:
                    self.state = 113
                    self.property_usage()
                    self.state = 114
                    self.property_type()

                else:
                    raise NoViableAltException(self)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Property_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(SystemRDLParser.EQ, 0)

        def SEMI(self):
            return self.getToken(SystemRDLParser.SEMI, 0)

        def property_string_type(self):
            return self.getTypedRuleContext(SystemRDLParser.Property_string_typeContext,0)


        def property_number_type(self):
            return self.getTypedRuleContext(SystemRDLParser.Property_number_typeContext,0)


        def property_boolean_type(self):
            return self.getTypedRuleContext(SystemRDLParser.Property_boolean_typeContext,0)


        def property_ref_type(self):
            return self.getTypedRuleContext(SystemRDLParser.Property_ref_typeContext,0)


        def getRuleIndex(self):
            return SystemRDLParser.RULE_property_type

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.enterProperty_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.exitProperty_type(self)




    def property_type(self):

        localctx = SystemRDLParser.Property_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_property_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(SystemRDLParser.T__1)
            self.state = 121
            self.match(SystemRDLParser.EQ)
            self.state = 126
            token = self._input.LA(1)
            if token in [SystemRDLParser.T__13]:
                self.state = 122
                self.property_string_type()

            elif token in [SystemRDLParser.T__14]:
                self.state = 123
                self.property_number_type()

            elif token in [SystemRDLParser.T__12]:
                self.state = 124
                self.property_boolean_type()

            elif token in [SystemRDLParser.T__7, SystemRDLParser.T__8, SystemRDLParser.T__9, SystemRDLParser.T__10, SystemRDLParser.T__15]:
                self.state = 125
                self.property_ref_type()

            else:
                raise NoViableAltException(self)

            self.state = 128
            self.match(SystemRDLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Property_defaultContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(SystemRDLParser.EQ, 0)

        def SEMI(self):
            return self.getToken(SystemRDLParser.SEMI, 0)

        def string(self):
            return self.getTypedRuleContext(SystemRDLParser.StringContext,0)


        def num(self):
            return self.getTypedRuleContext(SystemRDLParser.NumContext,0)


        def getRuleIndex(self):
            return SystemRDLParser.RULE_property_default

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.enterProperty_default(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.exitProperty_default(self)




    def property_default(self):

        localctx = SystemRDLParser.Property_defaultContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_property_default)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(SystemRDLParser.T__2)
            self.state = 131
            self.match(SystemRDLParser.EQ)
            self.state = 136
            token = self._input.LA(1)
            if token in [SystemRDLParser.STR]:
                self.state = 132
                self.string()

            elif token in [SystemRDLParser.NUM]:
                self.state = 133
                self.num()

            elif token in [SystemRDLParser.T__3]:
                self.state = 134
                self.match(SystemRDLParser.T__3)

            elif token in [SystemRDLParser.T__4]:
                self.state = 135
                self.match(SystemRDLParser.T__4)

            else:
                raise NoViableAltException(self)

            self.state = 138
            self.match(SystemRDLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Property_usageContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(SystemRDLParser.EQ, 0)

        def property_component(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SystemRDLParser.Property_componentContext)
            else:
                return self.getTypedRuleContext(SystemRDLParser.Property_componentContext,i)


        def SEMI(self):
            return self.getToken(SystemRDLParser.SEMI, 0)

        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(SystemRDLParser.OR)
            else:
                return self.getToken(SystemRDLParser.OR, i)

        def getRuleIndex(self):
            return SystemRDLParser.RULE_property_usage

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.enterProperty_usage(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.exitProperty_usage(self)




    def property_usage(self):

        localctx = SystemRDLParser.Property_usageContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_property_usage)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(SystemRDLParser.T__5)
            self.state = 141
            self.match(SystemRDLParser.EQ)
            self.state = 142
            self.property_component()
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SystemRDLParser.OR:
                self.state = 143
                self.match(SystemRDLParser.OR)
                self.state = 144
                self.property_component()
                self.state = 149
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 150
            self.match(SystemRDLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Property_componentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SystemRDLParser.RULE_property_component

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.enterProperty_component(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.exitProperty_component(self)




    def property_component(self):

        localctx = SystemRDLParser.Property_componentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_property_component)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SystemRDLParser.T__6) | (1 << SystemRDLParser.T__7) | (1 << SystemRDLParser.T__8) | (1 << SystemRDLParser.T__9) | (1 << SystemRDLParser.T__10) | (1 << SystemRDLParser.T__11))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Property_boolean_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SystemRDLParser.RULE_property_boolean_type

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.enterProperty_boolean_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.exitProperty_boolean_type(self)




    def property_boolean_type(self):

        localctx = SystemRDLParser.Property_boolean_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_property_boolean_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(SystemRDLParser.T__12)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Property_string_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SystemRDLParser.RULE_property_string_type

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.enterProperty_string_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.exitProperty_string_type(self)




    def property_string_type(self):

        localctx = SystemRDLParser.Property_string_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_property_string_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(SystemRDLParser.T__13)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Property_number_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SystemRDLParser.RULE_property_number_type

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.enterProperty_number_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.exitProperty_number_type(self)




    def property_number_type(self):

        localctx = SystemRDLParser.Property_number_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_property_number_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(SystemRDLParser.T__14)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Property_ref_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SystemRDLParser.RULE_property_ref_type

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.enterProperty_ref_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.exitProperty_ref_type(self)




    def property_ref_type(self):

        localctx = SystemRDLParser.Property_ref_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_property_ref_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SystemRDLParser.T__7) | (1 << SystemRDLParser.T__8) | (1 << SystemRDLParser.T__9) | (1 << SystemRDLParser.T__10) | (1 << SystemRDLParser.T__15))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Component_defContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(SystemRDLParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(SystemRDLParser.RBRACE, 0)

        def SEMI(self):
            return self.getToken(SystemRDLParser.SEMI, 0)

        def s_id(self):
            return self.getTypedRuleContext(SystemRDLParser.S_idContext,0)


        def component_def(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SystemRDLParser.Component_defContext)
            else:
                return self.getTypedRuleContext(SystemRDLParser.Component_defContext,i)


        def explicit_component_inst(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SystemRDLParser.Explicit_component_instContext)
            else:
                return self.getTypedRuleContext(SystemRDLParser.Explicit_component_instContext,i)


        def property_assign(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SystemRDLParser.Property_assignContext)
            else:
                return self.getTypedRuleContext(SystemRDLParser.Property_assignContext,i)


        def enum_def(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SystemRDLParser.Enum_defContext)
            else:
                return self.getTypedRuleContext(SystemRDLParser.Enum_defContext,i)


        def anonymous_component_inst_elems(self):
            return self.getTypedRuleContext(SystemRDLParser.Anonymous_component_inst_elemsContext,0)


        def getRuleIndex(self):
            return SystemRDLParser.RULE_component_def

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.enterComponent_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.exitComponent_def(self)




    def component_def(self):

        localctx = SystemRDLParser.Component_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_component_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SystemRDLParser.T__6) | (1 << SystemRDLParser.T__7) | (1 << SystemRDLParser.T__8) | (1 << SystemRDLParser.T__9) | (1 << SystemRDLParser.T__10))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
            self.state = 165
            token = self._input.LA(1)
            if token in [SystemRDLParser.ID, SystemRDLParser.INST_ID]:
                self.state = 163
                self.s_id()

            elif token in [SystemRDLParser.LBRACE]:

            else:
                raise NoViableAltException(self)

            self.state = 167
            self.match(SystemRDLParser.LBRACE)
            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SystemRDLParser.T__2) | (1 << SystemRDLParser.T__6) | (1 << SystemRDLParser.T__7) | (1 << SystemRDLParser.T__8) | (1 << SystemRDLParser.T__9) | (1 << SystemRDLParser.T__10) | (1 << SystemRDLParser.T__16) | (1 << SystemRDLParser.T__17) | (1 << SystemRDLParser.T__18) | (1 << SystemRDLParser.T__19) | (1 << SystemRDLParser.T__20) | (1 << SystemRDLParser.T__21) | (1 << SystemRDLParser.T__22) | (1 << SystemRDLParser.T__23) | (1 << SystemRDLParser.T__24) | (1 << SystemRDLParser.T__25) | (1 << SystemRDLParser.T__26) | (1 << SystemRDLParser.T__27) | (1 << SystemRDLParser.T__28) | (1 << SystemRDLParser.T__29) | (1 << SystemRDLParser.T__30) | (1 << SystemRDLParser.T__31) | (1 << SystemRDLParser.T__32) | (1 << SystemRDLParser.T__33) | (1 << SystemRDLParser.T__34) | (1 << SystemRDLParser.T__35) | (1 << SystemRDLParser.T__36) | (1 << SystemRDLParser.T__37) | (1 << SystemRDLParser.T__38) | (1 << SystemRDLParser.T__39) | (1 << SystemRDLParser.T__40) | (1 << SystemRDLParser.T__41) | (1 << SystemRDLParser.T__42) | (1 << SystemRDLParser.T__43) | (1 << SystemRDLParser.T__44) | (1 << SystemRDLParser.T__45) | (1 << SystemRDLParser.T__46) | (1 << SystemRDLParser.T__47) | (1 << SystemRDLParser.T__48) | (1 << SystemRDLParser.T__49) | (1 << SystemRDLParser.T__50) | (1 << SystemRDLParser.T__51) | (1 << SystemRDLParser.T__52) | (1 << SystemRDLParser.T__53) | (1 << SystemRDLParser.T__54) | (1 << SystemRDLParser.T__55) | (1 << SystemRDLParser.T__56) | (1 << SystemRDLParser.T__57) | (1 << SystemRDLParser.T__58) | (1 << SystemRDLParser.T__59) | (1 << SystemRDLParser.T__60) | (1 << SystemRDLParser.T__61) | (1 << SystemRDLParser.T__62))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (SystemRDLParser.T__63 - 64)) | (1 << (SystemRDLParser.T__64 - 64)) | (1 << (SystemRDLParser.T__65 - 64)) | (1 << (SystemRDLParser.T__66 - 64)) | (1 << (SystemRDLParser.T__67 - 64)) | (1 << (SystemRDLParser.T__68 - 64)) | (1 << (SystemRDLParser.T__69 - 64)) | (1 << (SystemRDLParser.T__70 - 64)) | (1 << (SystemRDLParser.T__71 - 64)) | (1 << (SystemRDLParser.T__72 - 64)) | (1 << (SystemRDLParser.T__73 - 64)) | (1 << (SystemRDLParser.T__74 - 64)) | (1 << (SystemRDLParser.T__75 - 64)) | (1 << (SystemRDLParser.T__76 - 64)) | (1 << (SystemRDLParser.T__77 - 64)) | (1 << (SystemRDLParser.T__78 - 64)) | (1 << (SystemRDLParser.T__79 - 64)) | (1 << (SystemRDLParser.T__80 - 64)) | (1 << (SystemRDLParser.T__81 - 64)) | (1 << (SystemRDLParser.T__82 - 64)) | (1 << (SystemRDLParser.T__83 - 64)) | (1 << (SystemRDLParser.T__84 - 64)) | (1 << (SystemRDLParser.T__85 - 64)) | (1 << (SystemRDLParser.T__86 - 64)) | (1 << (SystemRDLParser.T__87 - 64)) | (1 << (SystemRDLParser.T__88 - 64)) | (1 << (SystemRDLParser.T__89 - 64)) | (1 << (SystemRDLParser.T__90 - 64)) | (1 << (SystemRDLParser.T__91 - 64)) | (1 << (SystemRDLParser.T__92 - 64)) | (1 << (SystemRDLParser.T__93 - 64)) | (1 << (SystemRDLParser.T__102 - 64)) | (1 << (SystemRDLParser.T__103 - 64)) | (1 << (SystemRDLParser.T__104 - 64)) | (1 << (SystemRDLParser.T__105 - 64)) | (1 << (SystemRDLParser.T__106 - 64)) | (1 << (SystemRDLParser.ID - 64)))) != 0) or _la==SystemRDLParser.INST_ID or _la==SystemRDLParser.PROPERTY:
                self.state = 172
                la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                if la_ == 1:
                    self.state = 168
                    self.component_def()
                    pass

                elif la_ == 2:
                    self.state = 169
                    self.explicit_component_inst()
                    pass

                elif la_ == 3:
                    self.state = 170
                    self.property_assign()
                    pass

                elif la_ == 4:
                    self.state = 171
                    self.enum_def()
                    pass


                self.state = 176
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 177
            self.match(SystemRDLParser.RBRACE)
            self.state = 179
            _la = self._input.LA(1)
            if _la==SystemRDLParser.T__16 or _la==SystemRDLParser.ID or _la==SystemRDLParser.INST_ID:
                self.state = 178
                self.anonymous_component_inst_elems()


            self.state = 181
            self.match(SystemRDLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Explicit_component_instContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def s_id(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SystemRDLParser.S_idContext)
            else:
                return self.getTypedRuleContext(SystemRDLParser.S_idContext,i)


        def component_inst_elem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SystemRDLParser.Component_inst_elemContext)
            else:
                return self.getTypedRuleContext(SystemRDLParser.Component_inst_elemContext,i)


        def SEMI(self):
            return self.getToken(SystemRDLParser.SEMI, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SystemRDLParser.COMMA)
            else:
                return self.getToken(SystemRDLParser.COMMA, i)

        def getRuleIndex(self):
            return SystemRDLParser.RULE_explicit_component_inst

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.enterExplicit_component_inst(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.exitExplicit_component_inst(self)




    def explicit_component_inst(self):

        localctx = SystemRDLParser.Explicit_component_instContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_explicit_component_inst)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            _la = self._input.LA(1)
            if _la==SystemRDLParser.T__16:
                self.state = 183
                self.match(SystemRDLParser.T__16)


            self.state = 187
            _la = self._input.LA(1)
            if _la==SystemRDLParser.T__17:
                self.state = 186
                self.match(SystemRDLParser.T__17)


            self.state = 191
            _la = self._input.LA(1)
            if _la==SystemRDLParser.T__18:
                self.state = 189
                self.match(SystemRDLParser.T__18)
                self.state = 190
                self.s_id()


            self.state = 193
            self.s_id()
            self.state = 194
            self.component_inst_elem()
            self.state = 199
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SystemRDLParser.COMMA:
                self.state = 195
                self.match(SystemRDLParser.COMMA)
                self.state = 196
                self.component_inst_elem()
                self.state = 201
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 202
            self.match(SystemRDLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Anonymous_component_inst_elemsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def component_inst_elem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SystemRDLParser.Component_inst_elemContext)
            else:
                return self.getTypedRuleContext(SystemRDLParser.Component_inst_elemContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SystemRDLParser.COMMA)
            else:
                return self.getToken(SystemRDLParser.COMMA, i)

        def getRuleIndex(self):
            return SystemRDLParser.RULE_anonymous_component_inst_elems

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.enterAnonymous_component_inst_elems(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.exitAnonymous_component_inst_elems(self)




    def anonymous_component_inst_elems(self):

        localctx = SystemRDLParser.Anonymous_component_inst_elemsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_anonymous_component_inst_elems)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            _la = self._input.LA(1)
            if _la==SystemRDLParser.T__16:
                self.state = 204
                self.match(SystemRDLParser.T__16)


            self.state = 207
            self.component_inst_elem()
            self.state = 212
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SystemRDLParser.COMMA:
                self.state = 208
                self.match(SystemRDLParser.COMMA)
                self.state = 209
                self.component_inst_elem()
                self.state = 214
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Component_inst_elemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def s_id(self):
            return self.getTypedRuleContext(SystemRDLParser.S_idContext,0)


        def array(self):
            return self.getTypedRuleContext(SystemRDLParser.ArrayContext,0)


        def EQ(self):
            return self.getToken(SystemRDLParser.EQ, 0)

        def num(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SystemRDLParser.NumContext)
            else:
                return self.getTypedRuleContext(SystemRDLParser.NumContext,i)


        def AT(self):
            return self.getToken(SystemRDLParser.AT, 0)

        def INC(self):
            return self.getToken(SystemRDLParser.INC, 0)

        def MOD(self):
            return self.getToken(SystemRDLParser.MOD, 0)

        def getRuleIndex(self):
            return SystemRDLParser.RULE_component_inst_elem

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.enterComponent_inst_elem(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.exitComponent_inst_elem(self)




    def component_inst_elem(self):

        localctx = SystemRDLParser.Component_inst_elemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_component_inst_elem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.s_id()
            self.state = 217
            _la = self._input.LA(1)
            if _la==SystemRDLParser.LSQ:
                self.state = 216
                self.array()


            self.state = 221
            _la = self._input.LA(1)
            if _la==SystemRDLParser.EQ:
                self.state = 219
                self.match(SystemRDLParser.EQ)
                self.state = 220
                self.num()


            self.state = 225
            _la = self._input.LA(1)
            if _la==SystemRDLParser.AT:
                self.state = 223
                self.match(SystemRDLParser.AT)
                self.state = 224
                self.num()


            self.state = 229
            _la = self._input.LA(1)
            if _la==SystemRDLParser.INC:
                self.state = 227
                self.match(SystemRDLParser.INC)
                self.state = 228
                self.num()


            self.state = 233
            _la = self._input.LA(1)
            if _la==SystemRDLParser.MOD:
                self.state = 231
                self.match(SystemRDLParser.MOD)
                self.state = 232
                self.num()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSQ(self):
            return self.getToken(SystemRDLParser.LSQ, 0)

        def num(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SystemRDLParser.NumContext)
            else:
                return self.getTypedRuleContext(SystemRDLParser.NumContext,i)


        def RSQ(self):
            return self.getToken(SystemRDLParser.RSQ, 0)

        def COLON(self):
            return self.getToken(SystemRDLParser.COLON, 0)

        def getRuleIndex(self):
            return SystemRDLParser.RULE_array

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.exitArray(self)




    def array(self):

        localctx = SystemRDLParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.match(SystemRDLParser.LSQ)
            self.state = 236
            self.num()
            self.state = 239
            _la = self._input.LA(1)
            if _la==SystemRDLParser.COLON:
                self.state = 237
                self.match(SystemRDLParser.COLON)
                self.state = 238
                self.num()


            self.state = 241
            self.match(SystemRDLParser.RSQ)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Instance_refContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instance_ref_elem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SystemRDLParser.Instance_ref_elemContext)
            else:
                return self.getTypedRuleContext(SystemRDLParser.Instance_ref_elemContext,i)


        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(SystemRDLParser.DOT)
            else:
                return self.getToken(SystemRDLParser.DOT, i)

        def DREF(self):
            return self.getToken(SystemRDLParser.DREF, 0)

        def s_property(self):
            return self.getTypedRuleContext(SystemRDLParser.S_propertyContext,0)


        def getRuleIndex(self):
            return SystemRDLParser.RULE_instance_ref

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.enterInstance_ref(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.exitInstance_ref(self)




    def instance_ref(self):

        localctx = SystemRDLParser.Instance_refContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_instance_ref)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.instance_ref_elem()
            self.state = 248
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SystemRDLParser.DOT:
                self.state = 244
                self.match(SystemRDLParser.DOT)
                self.state = 245
                self.instance_ref_elem()
                self.state = 250
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 253
            _la = self._input.LA(1)
            if _la==SystemRDLParser.DREF:
                self.state = 251
                self.match(SystemRDLParser.DREF)
                self.state = 252
                self.s_property()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Instance_ref_elemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def s_id(self):
            return self.getTypedRuleContext(SystemRDLParser.S_idContext,0)


        def LSQ(self):
            return self.getToken(SystemRDLParser.LSQ, 0)

        def num(self):
            return self.getTypedRuleContext(SystemRDLParser.NumContext,0)


        def RSQ(self):
            return self.getToken(SystemRDLParser.RSQ, 0)

        def getRuleIndex(self):
            return SystemRDLParser.RULE_instance_ref_elem

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.enterInstance_ref_elem(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.exitInstance_ref_elem(self)




    def instance_ref_elem(self):

        localctx = SystemRDLParser.Instance_ref_elemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_instance_ref_elem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.s_id()
            self.state = 260
            _la = self._input.LA(1)
            if _la==SystemRDLParser.LSQ:
                self.state = 256
                self.match(SystemRDLParser.LSQ)
                self.state = 257
                self.num()
                self.state = 258
                self.match(SystemRDLParser.RSQ)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Property_assignContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def default_property_assign(self):
            return self.getTypedRuleContext(SystemRDLParser.Default_property_assignContext,0)


        def SEMI(self):
            return self.getToken(SystemRDLParser.SEMI, 0)

        def explicit_property_assign(self):
            return self.getTypedRuleContext(SystemRDLParser.Explicit_property_assignContext,0)


        def post_property_assign(self):
            return self.getTypedRuleContext(SystemRDLParser.Post_property_assignContext,0)


        def getRuleIndex(self):
            return SystemRDLParser.RULE_property_assign

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.enterProperty_assign(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.exitProperty_assign(self)




    def property_assign(self):

        localctx = SystemRDLParser.Property_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_property_assign)
        try:
            self.state = 271
            token = self._input.LA(1)
            if token in [SystemRDLParser.T__2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 262
                self.default_property_assign()
                self.state = 263
                self.match(SystemRDLParser.SEMI)

            elif token in [SystemRDLParser.T__17, SystemRDLParser.T__20, SystemRDLParser.T__21, SystemRDLParser.T__22, SystemRDLParser.T__23, SystemRDLParser.T__24, SystemRDLParser.T__25, SystemRDLParser.T__26, SystemRDLParser.T__27, SystemRDLParser.T__28, SystemRDLParser.T__29, SystemRDLParser.T__30, SystemRDLParser.T__31, SystemRDLParser.T__32, SystemRDLParser.T__33, SystemRDLParser.T__34, SystemRDLParser.T__35, SystemRDLParser.T__36, SystemRDLParser.T__37, SystemRDLParser.T__38, SystemRDLParser.T__39, SystemRDLParser.T__40, SystemRDLParser.T__41, SystemRDLParser.T__42, SystemRDLParser.T__43, SystemRDLParser.T__44, SystemRDLParser.T__45, SystemRDLParser.T__46, SystemRDLParser.T__47, SystemRDLParser.T__48, SystemRDLParser.T__49, SystemRDLParser.T__50, SystemRDLParser.T__51, SystemRDLParser.T__52, SystemRDLParser.T__53, SystemRDLParser.T__54, SystemRDLParser.T__55, SystemRDLParser.T__56, SystemRDLParser.T__57, SystemRDLParser.T__58, SystemRDLParser.T__59, SystemRDLParser.T__60, SystemRDLParser.T__61, SystemRDLParser.T__62, SystemRDLParser.T__63, SystemRDLParser.T__64, SystemRDLParser.T__65, SystemRDLParser.T__66, SystemRDLParser.T__67, SystemRDLParser.T__68, SystemRDLParser.T__69, SystemRDLParser.T__70, SystemRDLParser.T__71, SystemRDLParser.T__72, SystemRDLParser.T__73, SystemRDLParser.T__74, SystemRDLParser.T__75, SystemRDLParser.T__76, SystemRDLParser.T__77, SystemRDLParser.T__78, SystemRDLParser.T__79, SystemRDLParser.T__80, SystemRDLParser.T__81, SystemRDLParser.T__82, SystemRDLParser.T__83, SystemRDLParser.T__84, SystemRDLParser.T__85, SystemRDLParser.T__86, SystemRDLParser.T__87, SystemRDLParser.T__88, SystemRDLParser.T__89, SystemRDLParser.T__90, SystemRDLParser.T__91, SystemRDLParser.T__92, SystemRDLParser.T__93, SystemRDLParser.T__102, SystemRDLParser.T__103, SystemRDLParser.T__104, SystemRDLParser.T__105, SystemRDLParser.T__106, SystemRDLParser.PROPERTY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 265
                self.explicit_property_assign()
                self.state = 266
                self.match(SystemRDLParser.SEMI)

            elif token in [SystemRDLParser.ID, SystemRDLParser.INST_ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 268
                self.post_property_assign()
                self.state = 269
                self.match(SystemRDLParser.SEMI)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Default_property_assignContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def explicit_property_assign(self):
            return self.getTypedRuleContext(SystemRDLParser.Explicit_property_assignContext,0)


        def getRuleIndex(self):
            return SystemRDLParser.RULE_default_property_assign

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.enterDefault_property_assign(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.exitDefault_property_assign(self)




    def default_property_assign(self):

        localctx = SystemRDLParser.Default_property_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_default_property_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.match(SystemRDLParser.T__2)
            self.state = 274
            self.explicit_property_assign()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Explicit_property_assignContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def property_modifier(self):
            return self.getTypedRuleContext(SystemRDLParser.Property_modifierContext,0)


        def s_property(self):
            return self.getTypedRuleContext(SystemRDLParser.S_propertyContext,0)


        def EQ(self):
            return self.getToken(SystemRDLParser.EQ, 0)

        def property_assign_rhs(self):
            return self.getTypedRuleContext(SystemRDLParser.Property_assign_rhsContext,0)


        def getRuleIndex(self):
            return SystemRDLParser.RULE_explicit_property_assign

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.enterExplicit_property_assign(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.exitExplicit_property_assign(self)




    def explicit_property_assign(self):

        localctx = SystemRDLParser.Explicit_property_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_explicit_property_assign)
        try:
            self.state = 283
            token = self._input.LA(1)
            if token in [SystemRDLParser.T__102, SystemRDLParser.T__103, SystemRDLParser.T__104, SystemRDLParser.T__105, SystemRDLParser.T__106]:
                self.enterOuterAlt(localctx, 1)
                self.state = 276
                self.property_modifier()
                self.state = 277
                self.s_property()

            elif token in [SystemRDLParser.T__17, SystemRDLParser.T__20, SystemRDLParser.T__21, SystemRDLParser.T__22, SystemRDLParser.T__23, SystemRDLParser.T__24, SystemRDLParser.T__25, SystemRDLParser.T__26, SystemRDLParser.T__27, SystemRDLParser.T__28, SystemRDLParser.T__29, SystemRDLParser.T__30, SystemRDLParser.T__31, SystemRDLParser.T__32, SystemRDLParser.T__33, SystemRDLParser.T__34, SystemRDLParser.T__35, SystemRDLParser.T__36, SystemRDLParser.T__37, SystemRDLParser.T__38, SystemRDLParser.T__39, SystemRDLParser.T__40, SystemRDLParser.T__41, SystemRDLParser.T__42, SystemRDLParser.T__43, SystemRDLParser.T__44, SystemRDLParser.T__45, SystemRDLParser.T__46, SystemRDLParser.T__47, SystemRDLParser.T__48, SystemRDLParser.T__49, SystemRDLParser.T__50, SystemRDLParser.T__51, SystemRDLParser.T__52, SystemRDLParser.T__53, SystemRDLParser.T__54, SystemRDLParser.T__55, SystemRDLParser.T__56, SystemRDLParser.T__57, SystemRDLParser.T__58, SystemRDLParser.T__59, SystemRDLParser.T__60, SystemRDLParser.T__61, SystemRDLParser.T__62, SystemRDLParser.T__63, SystemRDLParser.T__64, SystemRDLParser.T__65, SystemRDLParser.T__66, SystemRDLParser.T__67, SystemRDLParser.T__68, SystemRDLParser.T__69, SystemRDLParser.T__70, SystemRDLParser.T__71, SystemRDLParser.T__72, SystemRDLParser.T__73, SystemRDLParser.T__74, SystemRDLParser.T__75, SystemRDLParser.T__76, SystemRDLParser.T__77, SystemRDLParser.T__78, SystemRDLParser.T__79, SystemRDLParser.T__80, SystemRDLParser.T__81, SystemRDLParser.T__82, SystemRDLParser.T__83, SystemRDLParser.T__84, SystemRDLParser.T__85, SystemRDLParser.T__86, SystemRDLParser.T__87, SystemRDLParser.T__88, SystemRDLParser.T__89, SystemRDLParser.T__90, SystemRDLParser.T__91, SystemRDLParser.T__92, SystemRDLParser.T__93, SystemRDLParser.PROPERTY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 279
                self.s_property()

                self.state = 280
                self.match(SystemRDLParser.EQ)
                self.state = 281
                self.property_assign_rhs()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Post_property_assignContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instance_ref(self):
            return self.getTypedRuleContext(SystemRDLParser.Instance_refContext,0)


        def EQ(self):
            return self.getToken(SystemRDLParser.EQ, 0)

        def property_assign_rhs(self):
            return self.getTypedRuleContext(SystemRDLParser.Property_assign_rhsContext,0)


        def getRuleIndex(self):
            return SystemRDLParser.RULE_post_property_assign

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.enterPost_property_assign(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.exitPost_property_assign(self)




    def post_property_assign(self):

        localctx = SystemRDLParser.Post_property_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_post_property_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.instance_ref()

            self.state = 286
            self.match(SystemRDLParser.EQ)
            self.state = 287
            self.property_assign_rhs()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Property_assign_rhsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def property_rvalue_constant(self):
            return self.getTypedRuleContext(SystemRDLParser.Property_rvalue_constantContext,0)


        def enum_body(self):
            return self.getTypedRuleContext(SystemRDLParser.Enum_bodyContext,0)


        def instance_ref(self):
            return self.getTypedRuleContext(SystemRDLParser.Instance_refContext,0)


        def concat(self):
            return self.getTypedRuleContext(SystemRDLParser.ConcatContext,0)


        def getRuleIndex(self):
            return SystemRDLParser.RULE_property_assign_rhs

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.enterProperty_assign_rhs(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.exitProperty_assign_rhs(self)




    def property_assign_rhs(self):

        localctx = SystemRDLParser.Property_assign_rhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_property_assign_rhs)
        try:
            self.state = 294
            token = self._input.LA(1)
            if token in [SystemRDLParser.T__3, SystemRDLParser.T__4, SystemRDLParser.T__79, SystemRDLParser.T__80, SystemRDLParser.T__94, SystemRDLParser.T__95, SystemRDLParser.T__96, SystemRDLParser.T__97, SystemRDLParser.T__98, SystemRDLParser.T__99, SystemRDLParser.T__100, SystemRDLParser.T__101, SystemRDLParser.NUM, SystemRDLParser.STR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 289
                self.property_rvalue_constant()

            elif token in [SystemRDLParser.T__19]:
                self.enterOuterAlt(localctx, 2)
                self.state = 290
                self.match(SystemRDLParser.T__19)
                self.state = 291
                self.enum_body()

            elif token in [SystemRDLParser.ID, SystemRDLParser.INST_ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 292
                self.instance_ref()

            elif token in [SystemRDLParser.LBRACE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 293
                self.concat()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConcatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(SystemRDLParser.LBRACE, 0)

        def concat_elem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SystemRDLParser.Concat_elemContext)
            else:
                return self.getTypedRuleContext(SystemRDLParser.Concat_elemContext,i)


        def RBRACE(self):
            return self.getToken(SystemRDLParser.RBRACE, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SystemRDLParser.COMMA)
            else:
                return self.getToken(SystemRDLParser.COMMA, i)

        def getRuleIndex(self):
            return SystemRDLParser.RULE_concat

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.enterConcat(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.exitConcat(self)




    def concat(self):

        localctx = SystemRDLParser.ConcatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_concat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.match(SystemRDLParser.LBRACE)
            self.state = 297
            self.concat_elem()
            self.state = 302
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SystemRDLParser.COMMA:
                self.state = 298
                self.match(SystemRDLParser.COMMA)
                self.state = 299
                self.concat_elem()
                self.state = 304
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 305
            self.match(SystemRDLParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Concat_elemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instance_ref(self):
            return self.getTypedRuleContext(SystemRDLParser.Instance_refContext,0)


        def num(self):
            return self.getTypedRuleContext(SystemRDLParser.NumContext,0)


        def getRuleIndex(self):
            return SystemRDLParser.RULE_concat_elem

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.enterConcat_elem(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.exitConcat_elem(self)




    def concat_elem(self):

        localctx = SystemRDLParser.Concat_elemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_concat_elem)
        try:
            self.state = 309
            token = self._input.LA(1)
            if token in [SystemRDLParser.ID, SystemRDLParser.INST_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 307
                self.instance_ref()

            elif token in [SystemRDLParser.NUM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 308
                self.num()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class S_propertyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROPERTY(self):
            return self.getToken(SystemRDLParser.PROPERTY, 0)

        def getRuleIndex(self):
            return SystemRDLParser.RULE_s_property

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.enterS_property(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.exitS_property(self)




    def s_property(self):

        localctx = SystemRDLParser.S_propertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_s_property)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            _la = self._input.LA(1)
            if not(((((_la - 18)) & ~0x3f) == 0 and ((1 << (_la - 18)) & ((1 << (SystemRDLParser.T__17 - 18)) | (1 << (SystemRDLParser.T__20 - 18)) | (1 << (SystemRDLParser.T__21 - 18)) | (1 << (SystemRDLParser.T__22 - 18)) | (1 << (SystemRDLParser.T__23 - 18)) | (1 << (SystemRDLParser.T__24 - 18)) | (1 << (SystemRDLParser.T__25 - 18)) | (1 << (SystemRDLParser.T__26 - 18)) | (1 << (SystemRDLParser.T__27 - 18)) | (1 << (SystemRDLParser.T__28 - 18)) | (1 << (SystemRDLParser.T__29 - 18)) | (1 << (SystemRDLParser.T__30 - 18)) | (1 << (SystemRDLParser.T__31 - 18)) | (1 << (SystemRDLParser.T__32 - 18)) | (1 << (SystemRDLParser.T__33 - 18)) | (1 << (SystemRDLParser.T__34 - 18)) | (1 << (SystemRDLParser.T__35 - 18)) | (1 << (SystemRDLParser.T__36 - 18)) | (1 << (SystemRDLParser.T__37 - 18)) | (1 << (SystemRDLParser.T__38 - 18)) | (1 << (SystemRDLParser.T__39 - 18)) | (1 << (SystemRDLParser.T__40 - 18)) | (1 << (SystemRDLParser.T__41 - 18)) | (1 << (SystemRDLParser.T__42 - 18)) | (1 << (SystemRDLParser.T__43 - 18)) | (1 << (SystemRDLParser.T__44 - 18)) | (1 << (SystemRDLParser.T__45 - 18)) | (1 << (SystemRDLParser.T__46 - 18)) | (1 << (SystemRDLParser.T__47 - 18)) | (1 << (SystemRDLParser.T__48 - 18)) | (1 << (SystemRDLParser.T__49 - 18)) | (1 << (SystemRDLParser.T__50 - 18)) | (1 << (SystemRDLParser.T__51 - 18)) | (1 << (SystemRDLParser.T__52 - 18)) | (1 << (SystemRDLParser.T__53 - 18)) | (1 << (SystemRDLParser.T__54 - 18)) | (1 << (SystemRDLParser.T__55 - 18)) | (1 << (SystemRDLParser.T__56 - 18)) | (1 << (SystemRDLParser.T__57 - 18)) | (1 << (SystemRDLParser.T__58 - 18)) | (1 << (SystemRDLParser.T__59 - 18)) | (1 << (SystemRDLParser.T__60 - 18)) | (1 << (SystemRDLParser.T__61 - 18)) | (1 << (SystemRDLParser.T__62 - 18)) | (1 << (SystemRDLParser.T__63 - 18)) | (1 << (SystemRDLParser.T__64 - 18)) | (1 << (SystemRDLParser.T__65 - 18)) | (1 << (SystemRDLParser.T__66 - 18)) | (1 << (SystemRDLParser.T__67 - 18)) | (1 << (SystemRDLParser.T__68 - 18)) | (1 << (SystemRDLParser.T__69 - 18)) | (1 << (SystemRDLParser.T__70 - 18)) | (1 << (SystemRDLParser.T__71 - 18)) | (1 << (SystemRDLParser.T__72 - 18)) | (1 << (SystemRDLParser.T__73 - 18)) | (1 << (SystemRDLParser.T__74 - 18)) | (1 << (SystemRDLParser.T__75 - 18)) | (1 << (SystemRDLParser.T__76 - 18)) | (1 << (SystemRDLParser.T__77 - 18)) | (1 << (SystemRDLParser.T__78 - 18)) | (1 << (SystemRDLParser.T__79 - 18)) | (1 << (SystemRDLParser.T__80 - 18)))) != 0) or ((((_la - 82)) & ~0x3f) == 0 and ((1 << (_la - 82)) & ((1 << (SystemRDLParser.T__81 - 82)) | (1 << (SystemRDLParser.T__82 - 82)) | (1 << (SystemRDLParser.T__83 - 82)) | (1 << (SystemRDLParser.T__84 - 82)) | (1 << (SystemRDLParser.T__85 - 82)) | (1 << (SystemRDLParser.T__86 - 82)) | (1 << (SystemRDLParser.T__87 - 82)) | (1 << (SystemRDLParser.T__88 - 82)) | (1 << (SystemRDLParser.T__89 - 82)) | (1 << (SystemRDLParser.T__90 - 82)) | (1 << (SystemRDLParser.T__91 - 82)) | (1 << (SystemRDLParser.T__92 - 82)) | (1 << (SystemRDLParser.T__93 - 82)) | (1 << (SystemRDLParser.PROPERTY - 82)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Property_rvalue_constantContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def num(self):
            return self.getTypedRuleContext(SystemRDLParser.NumContext,0)


        def string(self):
            return self.getTypedRuleContext(SystemRDLParser.StringContext,0)


        def getRuleIndex(self):
            return SystemRDLParser.RULE_property_rvalue_constant

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.enterProperty_rvalue_constant(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.exitProperty_rvalue_constant(self)




    def property_rvalue_constant(self):

        localctx = SystemRDLParser.Property_rvalue_constantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_property_rvalue_constant)
        try:
            self.state = 327
            token = self._input.LA(1)
            if token in [SystemRDLParser.T__3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 313
                self.match(SystemRDLParser.T__3)

            elif token in [SystemRDLParser.T__4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 314
                self.match(SystemRDLParser.T__4)

            elif token in [SystemRDLParser.T__94]:
                self.enterOuterAlt(localctx, 3)
                self.state = 315
                self.match(SystemRDLParser.T__94)

            elif token in [SystemRDLParser.T__95]:
                self.enterOuterAlt(localctx, 4)
                self.state = 316
                self.match(SystemRDLParser.T__95)

            elif token in [SystemRDLParser.T__96]:
                self.enterOuterAlt(localctx, 5)
                self.state = 317
                self.match(SystemRDLParser.T__96)

            elif token in [SystemRDLParser.T__97]:
                self.enterOuterAlt(localctx, 6)
                self.state = 318
                self.match(SystemRDLParser.T__97)

            elif token in [SystemRDLParser.T__98]:
                self.enterOuterAlt(localctx, 7)
                self.state = 319
                self.match(SystemRDLParser.T__98)

            elif token in [SystemRDLParser.T__99]:
                self.enterOuterAlt(localctx, 8)
                self.state = 320
                self.match(SystemRDLParser.T__99)

            elif token in [SystemRDLParser.T__100]:
                self.enterOuterAlt(localctx, 9)
                self.state = 321
                self.match(SystemRDLParser.T__100)

            elif token in [SystemRDLParser.T__101]:
                self.enterOuterAlt(localctx, 10)
                self.state = 322
                self.match(SystemRDLParser.T__101)

            elif token in [SystemRDLParser.T__80]:
                self.enterOuterAlt(localctx, 11)
                self.state = 323
                self.match(SystemRDLParser.T__80)

            elif token in [SystemRDLParser.T__79]:
                self.enterOuterAlt(localctx, 12)
                self.state = 324
                self.match(SystemRDLParser.T__79)

            elif token in [SystemRDLParser.NUM]:
                self.enterOuterAlt(localctx, 13)
                self.state = 325
                self.num()

            elif token in [SystemRDLParser.STR]:
                self.enterOuterAlt(localctx, 14)
                self.state = 326
                self.string()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Property_modifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SystemRDLParser.RULE_property_modifier

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.enterProperty_modifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.exitProperty_modifier(self)




    def property_modifier(self):

        localctx = SystemRDLParser.Property_modifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_property_modifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            _la = self._input.LA(1)
            if not(((((_la - 103)) & ~0x3f) == 0 and ((1 << (_la - 103)) & ((1 << (SystemRDLParser.T__102 - 103)) | (1 << (SystemRDLParser.T__103 - 103)) | (1 << (SystemRDLParser.T__104 - 103)) | (1 << (SystemRDLParser.T__105 - 103)) | (1 << (SystemRDLParser.T__106 - 103)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class S_idContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SystemRDLParser.ID, 0)

        def INST_ID(self):
            return self.getToken(SystemRDLParser.INST_ID, 0)

        def getRuleIndex(self):
            return SystemRDLParser.RULE_s_id

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.enterS_id(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.exitS_id(self)




    def s_id(self):

        localctx = SystemRDLParser.S_idContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_s_id)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            _la = self._input.LA(1)
            if not(_la==SystemRDLParser.ID or _la==SystemRDLParser.INST_ID):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NumContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(SystemRDLParser.NUM, 0)

        def getRuleIndex(self):
            return SystemRDLParser.RULE_num

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.enterNum(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.exitNum(self)




    def num(self):

        localctx = SystemRDLParser.NumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_num)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            self.match(SystemRDLParser.NUM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StringContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STR(self):
            return self.getToken(SystemRDLParser.STR, 0)

        def getRuleIndex(self):
            return SystemRDLParser.RULE_string

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.exitString(self)




    def string(self):

        localctx = SystemRDLParser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            self.match(SystemRDLParser.STR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Enum_defContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def s_id(self):
            return self.getTypedRuleContext(SystemRDLParser.S_idContext,0)


        def enum_body(self):
            return self.getTypedRuleContext(SystemRDLParser.Enum_bodyContext,0)


        def SEMI(self):
            return self.getToken(SystemRDLParser.SEMI, 0)

        def getRuleIndex(self):
            return SystemRDLParser.RULE_enum_def

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.enterEnum_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.exitEnum_def(self)




    def enum_def(self):

        localctx = SystemRDLParser.Enum_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_enum_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.match(SystemRDLParser.T__19)
            self.state = 338
            self.s_id()
            self.state = 339
            self.enum_body()
            self.state = 340
            self.match(SystemRDLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Enum_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(SystemRDLParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(SystemRDLParser.RBRACE, 0)

        def enum_entry(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SystemRDLParser.Enum_entryContext)
            else:
                return self.getTypedRuleContext(SystemRDLParser.Enum_entryContext,i)


        def getRuleIndex(self):
            return SystemRDLParser.RULE_enum_body

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.enterEnum_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.exitEnum_body(self)




    def enum_body(self):

        localctx = SystemRDLParser.Enum_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_enum_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.match(SystemRDLParser.LBRACE)
            self.state = 346
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SystemRDLParser.ID or _la==SystemRDLParser.INST_ID:
                self.state = 343
                self.enum_entry()
                self.state = 348
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 349
            self.match(SystemRDLParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Enum_entryContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def s_id(self):
            return self.getTypedRuleContext(SystemRDLParser.S_idContext,0)


        def EQ(self):
            return self.getToken(SystemRDLParser.EQ, 0)

        def num(self):
            return self.getTypedRuleContext(SystemRDLParser.NumContext,0)


        def SEMI(self):
            return self.getToken(SystemRDLParser.SEMI, 0)

        def LBRACE(self):
            return self.getToken(SystemRDLParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(SystemRDLParser.RBRACE, 0)

        def enum_property_assign(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SystemRDLParser.Enum_property_assignContext)
            else:
                return self.getTypedRuleContext(SystemRDLParser.Enum_property_assignContext,i)


        def getRuleIndex(self):
            return SystemRDLParser.RULE_enum_entry

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.enterEnum_entry(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.exitEnum_entry(self)




    def enum_entry(self):

        localctx = SystemRDLParser.Enum_entryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_enum_entry)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.s_id()
            self.state = 352
            self.match(SystemRDLParser.EQ)
            self.state = 353
            self.num()
            self.state = 362
            _la = self._input.LA(1)
            if _la==SystemRDLParser.LBRACE:
                self.state = 354
                self.match(SystemRDLParser.LBRACE)
                self.state = 358
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SystemRDLParser.T__20 or _la==SystemRDLParser.T__21:
                    self.state = 355
                    self.enum_property_assign()
                    self.state = 360
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 361
                self.match(SystemRDLParser.RBRACE)


            self.state = 364
            self.match(SystemRDLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Enum_property_assignContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(SystemRDLParser.EQ, 0)

        def string(self):
            return self.getTypedRuleContext(SystemRDLParser.StringContext,0)


        def SEMI(self):
            return self.getToken(SystemRDLParser.SEMI, 0)

        def getRuleIndex(self):
            return SystemRDLParser.RULE_enum_property_assign

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.enterEnum_property_assign(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, SystemRDLListener ):
                listener.exitEnum_property_assign(self)




    def enum_property_assign(self):

        localctx = SystemRDLParser.Enum_property_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_enum_property_assign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            _la = self._input.LA(1)
            if not(_la==SystemRDLParser.T__20 or _la==SystemRDLParser.T__21):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
            self.state = 367
            self.match(SystemRDLParser.EQ)
            self.state = 368
            self.string()
            self.state = 369
            self.match(SystemRDLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx




