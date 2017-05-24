# Lookup Bitcoin value from exchanges
from exchanges.bitfinex import Bitfinex
import re


def bitcoinValue(msg):
    val = Bitfinex().get_current_price()
    formattedVal = "$" + "{:,.2f}".format(val)

    if re.search(r"(?i)moon", msg):
        return "To the moon! " + formattedVal
    else:
        return "Bitcoin: " + formattedVal
