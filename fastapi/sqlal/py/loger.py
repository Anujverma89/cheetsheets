import logging


logger = logging.getLogger(__name__)
child = logging.getLogger(f'{__name__}.child')

logger.setLevel(logging.DEBUG)
d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}


print(dir(logger))
print(logger.parent.name)

def doLoger():
    child.debug("THis is child debug", extra=d)
    logger.info("this is info log", extra=d)
    logger.debug("THis is debug log",extra=d)
    logger.warning("Adding warning log",extra=d)
    logger.error("THis is error log",extra=d)
    logger.critical("THis is critical",extra=d)
    print(1)


class somework:
    def __init__(self):
        self.arr = [1,2,3,3,4]

    def __len__(self):
        return len(self.arr)

    
class otherwork:
    def __init__(self):
        self.arr = [1,2,3,3,4]

