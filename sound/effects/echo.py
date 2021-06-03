import logging
#logging.basicConfig(format='%(levelname)s %(name)s %(asctime)s %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)
#logger.setLevel(logging.DEBUG)
logger.info('hi from sound.effect.echo')
print('This is from echo')

class MyEchoEffect:
   logger = logging.getLogger('MyEchoEffect')
#   logger.setLevel(logging.DEBUG)
   def __init__(self):
      logger.info(f'global logger: initializing {__name__}')   # This refers to the global logger
      #MyEchoEffect.logger.info(f'initializing {__name__}')     # This refers to the class level logger
      self.logger.info(f'initializing {__name__}')

print(dir(MyEchoEffect))
MyEchoEffect()

