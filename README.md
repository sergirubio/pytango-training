# PyTango Training for SKA developers

The training will be based on the existing Tango Development Environment for SKA:

  https://developer.skatelescope.org/en/latest/tools/tango-devenv-setup.html

During the first day of the training I will help you to deploy the Development Environment 
for the training on your laptops. But I would recommend you to test the environment setup 
procedure in advance, so we can detect and solve any problem with your OS/hardware. 

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

