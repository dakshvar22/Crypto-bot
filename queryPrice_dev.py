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
import smtplib
from config import username,password

k = krakenex.API()
k.load_key('/home/daksh/cron/Crypto-bot/kraken.key')

def mail(currency_pair,val):
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()

    fromaddr = "dakshvar22@gmail.com"
    toaddr = "dakshvar22@gmail.com"

    msg = "\r\n".join([
  "From: dakshvar22@gmail.com",
  "To: dakshvar22@gmail.com",
  "Subject: Kraken BOT {0}".format(currency_pair) ,
  "",
  "Alert : {0} reached {1}".format(currency_pair,val)
  ])
    server.login(username,password)
    server.sendmail(fromaddr,toaddr,msg)
    server.quit()

def checkLastSent(filePath,val,direction):
    fPtr = open(filePath,'r')
    lines = fPtr.readlines()
    fPtr.close()
    # print lines
    if not len(lines):
        return False

    askVal,callVal = lines[-1].split(',')
    askVal = float(askVal)
    callVal = float(callVal[:-1])

    if direction == 'down':
        if askVal <= val:
            return True
        if callVal <= val:
            return True
    if direction == 'down':
        if askVal >= val:
            return True
        if callVal >= val:
            return True
    return False

def run(currency_pair,val,direction):

    filePath = '/home/daksh/cron/Crypto-bot/vals/vals' + '_' + currency_pair + '.txt'
    f = open(filePath,'ab+')
    # while 1:
    result =  k.query_public('Ticker', {'pair': currency_pair})['result'][currency_pair]

    askVal = float(result['a'][0])
    callVal = float(result['c'][0])
    
    # print type(askVal),type(callVal),type(val)

    if direction == 'down':
        if not checkLastSent(filePath,val,direction):
            if askVal <= val:
                # print 'sending mail 1'
                mail(currency_pair,askVal)
            elif callVal <= val:
                # print 'sending mail 2'
                mail(currency_pair,callVal)
    elif direction == 'up':
        if not checkLastSent(filePath,val,direction):
            if askVal >= val:
                # print 'sending mail 3'
                mail(currency_pair,askVal)
            elif callVal >= val:
                # print 'sending mail 4'
                mail(currency_pair,callVal)
    
    f.write(str(askVal) + ',' + str(callVal) + '\n')

    
    f.close()

# with daemon.DaemonContext(working_directory='/Users/daksh/personal'):
if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--currency_pair", help="Currency pair", required=True, type=str)
    parser.add_argument("--val", help="Target Val", required=True, type=float)
    parser.add_argument("--direction", help="down or up", required=True, type = str)
    args = parser.parse_args()
    run(args.currency_pair,args.val,args.direction)
    
