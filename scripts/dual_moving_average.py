from zipline.api import (
    history,
    order_target,
    record,
    symbol,
)


# context: a python dict, a place to save global variables
def initialize(context):
    # they are actually methods and not functions
    context.i = 0

def handle_data(context, data):
    context.i += 1
    if context.i < 300:
        return

    short_mvag = history(100, '1d', 'price').mean()
    long_mvad = history(300, '1d', 'price').mean()

    sym = symbol('AAPL')

    if short_mvag[sym] > long_mvad[sym]:
        order_target(sym, 100)
    elif short_mvag[sym] < long_mvad[sym]:
        order_target(sym, 0)

    record(AAPL=data[sym].price,
           short_mvag=short_mvag[sym],
           long_mvad=long_mvad[sym])
