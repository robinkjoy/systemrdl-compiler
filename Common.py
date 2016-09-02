def error(line, msg, *args):
    exit('error:{}: '.format(line) + msg.format(*args))


def warn(line, msg, *args):
    print('warn:{}: '.format(line) + msg.format(*args))


def itercomps(comps):
    for comp in comps:
        if isinstance(comp, list):
            for c in comp:
                yield c
        else:
            yield comp


def itercomps0(comps):
    for comp in comps:
        if isinstance(comp, list):
            yield comp[0]
        else:
            yield comp
