homework_web_library
====================

Program that monitors web sites and reports their availability.

###Running the program###
(you need python 2.7):
      
      bogdan@blap:[...]/homework_web_library$ ./webmon.py


###How it works###
  The program runs in an infnite loop that can be stopped by hitting CTRL+C
    
###Input###
  URLs, content requirement strings and checking periods are read from the config file (webmon.conf).
  In the config file, each URL section contains 3 lines: URL, match string and period in milliseconds.
  Each different URL sections must be separaded by an empty line.

    The project includes an example config file.
  
###Output###
  The program writes timestamp, URL, content requirement string, load time and request resutl to the log file (webmon.log).
  The information from multiple program runs will be appended to the same log file.
    
  Example log file contents:
  
        ###### 2013-07-05 13:44:25.044511 ##################
        URL: http://www.google.ro
        Check String: google
        Load time: 230
        RESULT: MATCH!MATCH!MATCH!
        
        ###### 2013-07-05 13:44:26.095225 ##################
        URL: http://www.yahoo.com
        Check String: protopopitoricescovici
        Load time: 884
        RESULT: NO MATCH!
        
        ###### 2013-07-05 13:44:26.318057 ##################
        URL: http://sdfasdfdsgdsffgdfsg.lol
        Check String: kcuf
        Load time: 0
        RESULT: Huston, we have a problem!
        
        ###### 2013-07-05 13:44:29.011237 ##################
        URL: http://www.yahoo.com
        Check String: protopopitoricescovici
        Load time: 906
        RESULT: NO MATCH!


