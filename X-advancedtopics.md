Testing




##################################################

Polling 

Dynamic class loading / Dynamic devices / Dynamic Attributes

Time consuming tasks: use either ThreadDict or WorkerDS + Threads for extremely consuming tasks

Acces to Database: Use fandango and cached methods instead of direct access (do not block the database please!)
	multiple database devices!! don't expose the system flaws!


##################################################

getting attr list from within the device
(TEST IT!!)
self.get_device_attr().get_attribute_list()
or self.get_device_attr().attr_list
it accesss the MultiAttribute object

Device Hierarchies

special cases

timeouts
polling out of synch
asynchronous commands
event based hierarchies
risk of high cpu usage
background threads
multiprocess
separate two threads in two different devices in the same server

## How to deal with Qualities

Sometimes, availability of an attribute does not depend directly on State.

To avoid reading the wrong attribute, you can set its quality to invalid.

Same may happen for an attribute which value is not numeric:

 * HWErrors: No error, quality VALID
 * HWErrors: Errors received!, quality WARNING


##################################################

Docker to use? ... use debian-stretch (python2 Qt4)
https://hub.docker.com/r/cpascual/taurus-test/

Simulation Devices

Taurus docker

Fandango Scripts
Searching devices / attributes / properties
Start / stop of devices
Configuration from shell
Import / Export from files
Executing commands from shell
Python 3



I write you regarding the workshop in icalepcs. As we share 1 hour in the workshop agenda maybe we can start thinking in what we can be interested.

Some of my topics would be:

 - export/import of devices

 - massive change of configuration properties

 - simulators

 - dynamic devices


