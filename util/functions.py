import sys
import datetime

def trace(*args):
    print(datetime.datetime.now(), '...', *args, file=sys.stderr)
    sys.stderr.flush()

def fill_batch(batch, token='</s>'):
    max_len = max(len(x) for x in batch)
    return [x + [token] * (max_len - len(x) + 1) for x in batch]

    return ' '.join(fmt % x for x in vector)

def vtos(v, fmt='%.8e'):
    return ' '.join(fmt % x for x in v)

def stov(s, tp=float):
    return [tp(x) for x in s.split()]
