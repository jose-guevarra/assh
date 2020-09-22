#!/usr/bin/python3

import argparse
import sys

from asshdb import *
from asshconfig import *
from asshconnect import *


## process the command arguments
app_desc = """SSH Aliases.  Create aliases to stored ssh server profiles."""

parser = argparse.ArgumentParser(description=app_desc)
parser.add_argument('alias', help='Execute alias.', metavar='aliasname', type=str, nargs='?')
parser.add_argument('-p','--print', help='Print alias information.', metavar='alias', action='store', required=False)
parser.add_argument('-a','--all', help='Print all aliases in detail.', required=False, action='store_true')
parser.add_argument('-l','--list', help='List all alias names.', required=False, action='store_true')
args = vars(parser.parse_args())

if __name__ == '__main__':

    ## Load our config
    asshconfig = AsshConfig()
    asshdb = Asshdb(asshconfig)
    
    if args['alias']:
        
        ## verify alias
        if asshdb.checkAlias(args['alias']) and asshdb.aliases[args['alias']].aliasType == 'ssh':
            asshconnect = AsshConnect(asshdb.aliases[args['alias']])
            asshconnect.connect()
            sys.exit()
        else:
            print(args['alias'] + ': Alias not found or not ssh type.')
            sys.exit()
    elif args['list']: # print alias list (used by autocomplete)
        aliaslist = ''
        for k in asshdb.aliases:
            aliaslist += k + ' '
        print(aliaslist.strip())
        sys.exit()
    elif args['print']:
        
        print("Print alias: " + args['print'])
    
        asshdb.printAlias(args['print'])
        
        sys.exit()
    elif args['all']:
        print("print all aliases")
        
        for k in asshdb.aliases:
            asshdb.printAlias(k)
        
        sys.exit()

    else:
        sys.exit()
    
    
