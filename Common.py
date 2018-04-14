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


def flatten(l, a):
    for i in l:
        if isinstance(i, list):
            flatten(i, a)
        else:
            a.append(i)
    return a
