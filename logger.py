import logging

# Set up the logging configuration
logging.basicConfig(filename="example.log", level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s')

# Python levels
# DEBUG - Detailed information, typically of interest only when diagnosing problems
# INFO - Confirmation that things are working as expected
# WARNING - Indicate that somethign unexpected happened, or indicative of some problem in the near future(e.g. disk space low). The software still working as expected
# ERROR - More serious problem, software not able to perform some function
# CRITICAL - A serious error, program may b unable to continue running
## Reference: https://docs.python.org/3/howto/logging.html


def divide(a, b):
    try:
        result = a / b
        logging.debug('Division successful: %d/%d = %f', a,b,result)
        return result
    except ZeroDivisionError:
        logging.error('Division by zero!')

print(divide(10,5))
print(divide(10,0))