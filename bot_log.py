import logging
from time import gmtime, strftime
logname=strftime("%Y-%m-%d %H:%M:%S", gmtime())
logname='bot_'+logname
logging.basicConfig(filename=logname,level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.Formatter("Prabhat")