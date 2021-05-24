# writing the logging function using the concept of oop

class Logger(object):
    """A file-based message logger with the following properties
    
    Attributes:
        file_name: a String representing the full path of the log file to which this logger will write its messages.

    """


    def __init__(self, file_name):
        """Return a Logger object whose file_name is *file_name*"""
        self.file_name = file_name

    def write_log(self, level, msg):
        """Writes a message to the file_name for a specific Logger Instance"""
        
        with open(self.file_name, "a") as log_file:
            log_file.write("[{0}] {1}\n".format(level, msg))
    

