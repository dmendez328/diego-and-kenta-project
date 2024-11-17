# Alpaca packages
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest
from alpaca.trading.enums import AssetClass

from transitions import Machine # State machine package

import sys # System package


# These are the kays for the PAPER TRADING Account
api_key = 'PK8GF9Z7PRX6NVL2SQNB'
api_secret = '89H3rauNygywwKDmGEjgvcJ2LdPyncxgAjXudD2u'
alpaca_account_url = 'https://paper-api.alpaca.markets/v2/account' # URL for paper trading market


trading_client = TradingClient(api_key, api_secret) # Getting specific clients details

class States:

    def __init__(self):
        self.running = True
        self.trading = Trading(api_key, api_secret, alpaca_account_url)




if __name__ == '__main__':

    ''' Actually starts state machine '''
    states = States()
    states.start()