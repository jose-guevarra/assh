#!/usr/bin/python
## Jose Guevarra 7.2012

import argparse
import sys

from aliasdb import *
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
    aliasdb = Aliasdb(asshconfig)
    
    if args['alias']:
        
        ## verify alias
        if aliasdb.checkAlias(args['alias']) and aliasdb.aliases[args['alias']].aliasType == 'ssh':
            #print 'connect to alias: ' + args['alias']
            asshconnect = AsshConnect(aliasdb.aliases[args['alias']])
            asshconnect.connect()
            sys.exit()
        else:
            print args['alias'] + ': Alias not found or not ssh type.'
            sys.exit()
    elif args['list']: # print alias list (used by autocomplete)
        aliaslist = ''
        for k in aliasdb.aliases:
            aliaslist += k + ' '
        print aliaslist.strip()
        sys.exit()
    elif args['print']:
        
        print "Print alias: " + args['print']
    
        aliasdb.printAlias(args['print'])
        
        ##aliasdb.add({'aliasName': 'otaku', 'sshHostname': 'otaku.freeshell.org', 'sshCompression': True, 'sshVersion': '2'})
        ##aliasdb.aliases['otaku'].setOption('sshUser', 'jose')
        
        ##aliasdb.printAlias('otaku')
        ##aliasdb.save()
        #aliasdb.aliases['otaku'].aliasDict()
        sys.exit()
    elif args['all']:
        print "print all aliases"
        
        for k in aliasdb.aliases:
            aliasdb.printAlias(k)
        
        sys.exit()

    else:
        sys.exit()
    
    
    
    
    
                
                
    
