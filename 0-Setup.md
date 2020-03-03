# Setup of the Tango Development Environment

The training will be based on the existing Tango Development Environment for SKA:

  https://developer.skatelescope.org/en/latest/tools/tango-devenv-setup.html

This training will use the existing docker containers for database, Tango Database Server
and itango CLI.

I recommend you to test the environment setup procedure in advance, 
so we can detect and solve any problem with your OS/hardware. 

I've tested the development docker containers on Ubuntu (works), Debian (doesn't work) 
and Lubuntu (better performance). So in case your system is other than Ubuntu, 
it is highly recommended to install virtual box before the training: 

  https://www.virtualbox.org/

These are the OS images that can be used for the training:

**UBUNTU** (full-featured):
https://sourceforge.net/projects/osboxes/files/v/vb/55-U-u/18.04/18.04.2/18042.64.7z/download

**LUBUNTU** (much, much faster):
https://sourceforge.net/projects/osboxes/files/v/vb/33-Lb--t/18.04/18.04.3/L1804.3-64bit.7z/download

## Using the Lubuntu (non-standard) image

The lubuntu image would require these two lines to be removed on deploy_tangoenv.yml file:

    install_ide: 'yes'
    - ide

And you will have to use lighter editors for the training (mousepad or geany instead of PyCharm). 
This will not be an impediment for the training as all the exercises can be done using 
a simple lightweight editor.

# Setup of itango container to run SKABaseDevice Tango classes

ska_logging and skabase libraries will have to be downloaded:

    git clone https://gitlab.com/ska-telescope/ska-logging
    ln -s ska-logging/ska_logging
    git clone https://github.com/ska-telescope/lmc-base-classes
    ln -s lmc-base-classes/skabase
    
then, modify the itango.yml file to mount host home on the container:

    
    



----


