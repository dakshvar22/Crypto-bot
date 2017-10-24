#!/usr/bin/env python2

# This file is part of krakenex.
# Licensed under the Simplified BSD license. See examples/LICENSE.

# Demonstrates how to use the conditional close functionality; that is,
# placing an order that, once filled, will place another order.
#
# This can be useful for very simple automation, where a bot is not
# needed to constantly monitor execution.

import krakenex
import argparse

k = krakenex.API()
k.load_key('/Users/daksh/personal/crypto/kraken/kraken.key')

# currency_pair = 'XETHZUSD'

def run(currency_pair):
    f = open('/Users/daksh/personal/crypto/kraken/vals/vals' + '_' + currency_pair + '.txt','a')
    # while 1:
    result =  k.query_public('Ticker', {'pair': currency_pair})['result'][currency_pair]

    askVal = result['a'][0]
    callVal = result['c'][0]
      
    # print askVal,callVal  
    f.write(str(askVal) + ',' + str(callVal) + '\n')

    # time.sleep(30)
    f.close()

# with daemon.DaemonContext(working_directory='/Users/daksh/personal'):
if __name__=='__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("--currency_pair", help="Currency pair", required=True, type=str)
 	args = parser.parse_args()
 	run(args.currency_pair)
    
