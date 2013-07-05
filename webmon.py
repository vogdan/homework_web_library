#!/usr/bin/env python

from webmon_lib import *

CONFIG_FILE = "webmon.conf"
LOG_FILE = "webmon.log"

conf_l =  parse_config(CONFIG_FILE)
urlmon_l = []
for conf in conf_l:
    conf.append(LOG_FILE)
    urlmon_l.append(UrlMon(*conf))


for urlmon in urlmon_l:
    urlmon.do_request()
