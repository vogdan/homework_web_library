from urllib2 import urlopen, URLError
from time import time
from re import search
from datetime import datetime 

def read_file(file_name):
    with open(file_name, 'r') as f:
        return f.readlines()

def append_file(file_name, message):
    with open(file_name, 'a+') as f:
        f.write(message)

def parse_config(config_file):
    """ Return a list of lists. Each sub-list contains 
    url, content requirement text and checking period
    """
    lines = read_file(config_file)
    ret_l , aux_l = [], []
    
    for line in lines:
        if line != "\n":
            aux_l.append(line.strip())
        else:
            ret_l.append(aux_l)
            aux_l = []

    ret_l.append(aux_l)
    return ret_l

def get_ms_time():
	return int(round(time() * 1000))

class UrlMon:
    def __init__(self, url, check_string, check_interval, log_file):
        self.url = url
        self.check_string = check_string
        self.check_interval = int(check_interval)
        self.log_file = log_file
        self.last_check = 0
        self.url_load_time = 0
        self.last_check_status = "None"

    def do_request(self):
        since_last_check = get_ms_time() - self.last_check
        if since_last_check > self.check_interval:
            self.do_check()
            self.put_log()

    def do_check(self):
         try:
            start_msecs = get_ms_time() 
            page = urlopen(self.url)
            self.last_check = get_ms_time()
            self.url_load_time = self.last_check - start_msecs 
             
            page_contents = page.read()
            if search(self.check_string, page_contents):
                self.last_check_status = "MATCH!MATCH!MATCH!"
            else:
                self.last_check_status = "NO MATCH!"
         except URLError:
             self.last_check = get_ms_time()
             self.last_check_status = "Huston, we have a problem!" 

    def put_log(self):
        log_string = "\n###### {} ##################\n\
URL: {}\n\
Check String: {}\n\
Load time: {}\n\
RESULT: {}\n".format(str(datetime.now()),
                      self.url, self.check_string, 
                      self.url_load_time,
                      self.last_check_status)
        append_file(self.log_file, log_string)

