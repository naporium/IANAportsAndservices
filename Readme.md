### Motivation:
 Learning Web-Scrapping with Python 3 __(requests and beautiful soup 4)__<br>
 Training Python Scriptng

### Module description:

1. We will try to scrap __IANA.ORG__, with python requests package<br>
   __Extract__ ( WELL KNOW PORTS | IANA -Service Name and Transport Protocol Port Number Registry )__DATA__ from html table<br>
   and __store the data__ in csv file.

2. We will use pandas to get the file (similar to __curl__)
     
__In both situations we store the data in csv format__  

- [Page where to start to extract data from](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml?&page=1)

### Requirements:
  -[x] pip install requests
  -[x] pip beautifulsoup4 
  -[x] pip install pandas

### References:
 - [RHEL ports and services @MIT.EDU](https://web.mit.edu/rhel-doc/4/RH-DOCS/rhel-sg-en-4/ch-ports.html)
 - [beautifull @PYPY](https://pypi.org/project/beautifulsoup4/)
 - [beautifull documentation @READTHEDOCS](https://readthedocs.org/projects/beautiful-soup-4/downloads/pdf/latest/)
 - [requests.org](https://docs.python-requests.org/en/master/)
 - [Scrapping tutorial @Digital Ocean](hhttps://www.digitalocean.com/community/tutorials/how-to-work-with-web-data-using-requests-and-beautiful-soup-with-python-3)
 - [web-scraping-html-tables @towardDatascience](https://towardsdatascience.com/web-scraping-html-tables-with-python-c9baba21059)
 - [lxml @PYPY](https://pypi.org/project/lxml/#history)
 - [lxml @lxml.de](https://lxml.de/)
 - [lxml Documentation](https://lxml.de/apidoc/index.html)
 - [Tutorials Pandas DataFrames @ thispointer.com](https://thispointer.com/how-to-get-check-data-types-of-dataframe-columns-in-python-pandas/)
 - [Pandas @Geeksforgeeks.org](https://www.geeksforgeeks.org/python-pandas-series-str-find/)
 - [Pandas Documentation @Pandas.pydata.org](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html)
 - []()
 - []()

 
 Useful commands:
   -[x] Command to clear all variables and imports in python interactive console
        - \>>> globals().clear()
        - cat /etc/services 
    

### Conclusion
    - We could accelerate the process, 
      -  making more requests per second
      -  using threads or multiprocessing
    - We can get all the data with 'curl' and pull the csv file to python
         
    ************************************************************************
    * PLEASE NOTE THE FOLLOWING:                                           *
    *                                                                      *
    * ASSIGNMENT OF A PORT NUMBER DOES NOT IN ANY WAY IMPLY AN             *
    * ENDORSEMENT OF AN APPLICATION OR PRODUCT, AND THE FACT THAT NETWORK  *
    * TRAFFIC IS FLOWING TO OR FROM A REGISTERED PORT DOES NOT MEAN THAT   *
    * IT IS "GOOD" TRAFFIC, NOR THAT IT NECESSARILY CORRESPONDS TO THE     *
    * ASSIGNED SERVICE. FIREWALL AND SYSTEM ADMINISTRATORS SHOULD          *
    * CHOOSE HOW TO CONFIGURE THEIR SYSTEMS BASED ON THEIR KNOWLEDGE OF    *
    * THE TRAFFIC IN QUESTION, NOT WHETHER THERE IS A PORT NUMBER          *
    * REGISTERED OR NOT.                                                   *
    ************************************************************************
    
    # The latest IANA port assignments can be gotten from
    #       http://www.iana.org/assignments/port-numbers
    # The Well Known Ports are those from 0 through 1023.
    # The Registered Ports are those from 1024 through 49151
    # The Dynamic and/or Private Ports are those from 49152 through 65535


 - [x] We Should consider running Nmap and check for nmap ports tables...
 - [x] We Should consider running Wireshark/Tshark and check for ports ... 

### FOR CSV DATA, check this later, Aligator:
- SOURCE : https://security.stackexchange.com/questions/165032/can-a-csv-contain-malicious-code 
- The system validates (amongst other things) that all CSV files can be parsed by an RFC 4180 compliant parser, and are valid UTF-8. It ensures that when files are downloaded, they have Content-Type: text/csv; charset=utf-8, and Content-Disposition: attachment; filename="download.csv".
 - __A concern has been raised that the system could be used to transmit malware or malicious code.__
    - The parser of said CSV, just values seperated by commas, would need to have a vulnerability, which the file would need to exploit. Unlikely.
    - __From the first link, the suggested fix is that if a column starts with =, @, +, or -, escape it with a single quote (') before it.__
    - anything that starts with one of those prefixes and contains | (and maybe also = with DDE, to mitigate
    
 - LOL;)
   - Example - Create a CSV file with the following 2 lines -
    <br>
    User name,Email,Designation<br>
    =2+5+cmd|' /C calc'!A0,a@b.com,SSE<br>
   Save it and open using MS excel. <br>Calculator will open in your Windows system.
   
### Further reading:
 - [x] csv_injection
 - [x] csv_injection mitigations
     - https://owasp.org/www-community/attacks/CSV_Injection
     - https://nvd.nist.gov/vuln/detail/CVE-2014-3524 (Apache openoffice Version 4.1) __(Patched)__
 
 -  https://datatracker.ietf.org/doc/html/rfc4180
   - from IETF:
     - Security considerations:

      CSV files contain passive text data that should not pose any
      risks.  However, it is possible in theory that malicious binary
      data may be included in order to exploit potential buffer overruns
      in the program processing CSV data.  Additionally, private data
      may be shared via this format (which of course applies to any text
      data).

### USAGE CASES
     
 #### [STEP 1] pull csv data from IANA. and and b cases == same result
 a)

     # use panda to pull the data
     $ python IANAWriteCSVFileWithPandas.py

 b) 

    # use python requets to pull the data 
    $ python IANAScrapper.py  

 #### [STEP 2] Read/Search the data
 a) using cat and grep  

    $ cat CollectedData/<downloadedfile.csv> |grep "dhcp"| cut -d "," -f 2,3,4
    
 b) using python script

    # 1 E.G.
    $ python IANACmdSearchTool.py --protocol udp
    # 2 E.G.
    $  python IANACmdSearchTool.py --service_name=rje
    # 3 E.G.
    $  python IANACmdSearchTool.py --port 53
    
