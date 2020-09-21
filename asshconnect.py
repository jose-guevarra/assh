"""
Class:  AsshConnect

"""


class AsshConnect(object):
    'Connect to ssh server defined by alias'
    Name = "AsshConnect"

    
    def __init__(self, aliasObj):

        self.alias = aliasObj
        self.sshArgs = ['ssh']
        self.genSshCommand()

    def genSshCommand(self):

        if self.alias.bulkSshArgs is not None:
            self.sshArgs.append(self.alias.bulkSshArgs)
        
        if self.alias.sshUser is not None:
            tmp = self.alias.sshUser + '@'
            
        tmp = tmp + self.alias.sshHostname
        self.sshArgs.append(tmp)
        
    def connect(self):
        from subprocess import call
        #print self.sshArgs
        call(self.sshArgs)
        
        
