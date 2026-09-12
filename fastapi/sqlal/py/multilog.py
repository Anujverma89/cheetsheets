import logging 

# logging is the root logger 

parentLog = logging.getLogger("parent") # child log of root 
child = logging.getLogger("parent.child") # child log of parent
childd = logging.getLogger("parent.childd") # child log of parent
child2 = logging.getLogger("parent.child.child") # child log of child2

handler1 = logging.FileHandler("multilog.log") # we can create handler and attach to the logger 
parentLog.addHandler(handler1)

formatter = logging.Formatter(
    fmt= "%(asctime)s | %(thread)s %(message)s"
)
handler1.setFormatter(formatter)



logging.basicConfig(
    filename="multilog.log", level= logging.NOTSET
)


parentLog.debug("this is debug one", exc_info= True, stack_info= True)
child2.debug(" this is child2 debug")

for i in parentLog.getChildren():
    print(i)


def onemore(*args,**kwargs):
    print(f'{args}{kwargs["status"]}')

onemore("anuj","verma","class", status = "Moh")


#logging.error("mess", exc_info = "Exception info", stack_info = "", stack_level="", extra="")

# logger : logs the error based on specific level .
# handler : routes the error and prints it based on handler .
# Formatter : formats the message for better understanding . 
