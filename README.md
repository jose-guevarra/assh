Assh creates ssh aliases in a centrally located aliasdb.yml file.  
This allows you to easily copy that file between machines to keep
you aliases consistent across machines.



REQUIRED PACKAGES:

Python YAML
$> sudo apt-get install python-yaml


INSTALLATION:

copy misc/assh to /etc/bash_completion.d/

then run
$> . /etc/bash_completion.d/assh


CONFIGURATION FILES:

assh.yml tells assh the directory to find the aliasdb.yml file.

copy misc/assh.yml.sample to ~/.local/share/assh/assh.yml

By default, Ussh looks for a configuration file in 
~/.local/share/assh/assh.yaml

NOTES ON SECURITY:

Keep your asshdb.yml file secure and not visible to anyone
else.  This file contains connection information and
credentials for the ssh servers you connect to.


