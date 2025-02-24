import inspect
import logging

import allure


def CustomLogger():
      #1.This is used to get the class /method name from where this customerlogger method is called
       logName=inspect.stack()[1][3]

      #2. Create the logging object and pass thr logName in it
       logger=logging.getLogger(logName)

      #3. Set the log level
       logger.setLevel(logging.DEBUG)

       #4. Create the fileHandler to save the logs in the file
       fileHandler =logging.FileHandler("../reports/Code2Lead.log", mode='a')

       #5.Set the loglevel for filehandler
       fileHandler.setLevel(logging.DEBUG)

       #6.Create the format in which you like to save the logs
       formatter=logging.Formatter('%(asctime)s-%(name)s- %(levelname)s : %(message)s',
                                datefmt='%d%m%y %I:%M%S %p %A')

       #7.Set the formatter to filehandler
       fileHandler.setFormatter(formatter)

       #8.Add filehandler to logging
       logger.addHandler(fileHandler)

       #finally return the logging object

       return logger

def allureLogs(text):
       with allure.step(text):
         pass

