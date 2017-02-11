# Lookup Bitcoin value from exchanges
from exchanges.bitfinex import Bitfinex

def bitcoinValue():
    val = Bitfinex().get_current_price()
    return "Bitcoin: $" + "{:,.2f}".format(val)
