import logging
import collections

print(__name__)
logging.basicConfig(format='%(levelname)s %(name)s %(asctime)s %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)
#logger.setLevel(logging.DEBUG)

class LoggingDict(dict):
   def __init__(self):
      pass
   
   def __setitem__(self, k, v):
      logger.info(f'Adding key {k} with value {v}')
      super().__setitem__(k, v)


my_dict = LoggingDict()
my_dict[1] = 2
my_dict['map'] = False
my_dict[0] = 'Zero'
print(my_dict)

class LoggingOD(LoggingDict, collections.OrderedDict):
   pass

my_od = LoggingOD()
my_od['one'] = 1
my_od['two'] = 2
my_od['three'] = 3
print(my_od)

import sound.effects.echo

assert my_od['one'] == 1
