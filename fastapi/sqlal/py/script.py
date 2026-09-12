import logging
from loger import doLoger, somework
import sys

FORMAT = '%(asctime)s %(clientip)-15s %(user)-8s %(message)s'
logging.basicConfig(
    filename="server.log",
    level= logging.DEBUG,
    format= FORMAT    
)


d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
logger = logging.getLogger(__name__)


def main():
    logger.warning("running file", exc_info=sys.exc_info(), extra= d)
    print("running after logging")
    doLoger()
    logger.error("completed", extra= d)

obj = somework()
print(len(obj))

if __name__ == "__main__":
    main()


