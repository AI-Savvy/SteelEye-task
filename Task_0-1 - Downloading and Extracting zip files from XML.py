# Importing necessary Libraries
# %conda install wget

import pandas as pd
import numpy as np
import requests
import xml.etree.cElementTree as et
import wget as wg
import zipfile as z

# Setting URL 
URL = "https://registers.esma.europa.eu/solr/esma_registers_firds_files/select?q=*&fq=publication_date:%5B2021-01-17T00:00:00Z+TO+2021-01-19T23:59:59Z%5D&wt=xml&indent=true&start=0&rows=100"
response = requests.get(URL)
with open('task_0-1.xml', 'wb') as file:
    file.write(response.content)
    

# Implementing XML parser
dom = et.parse('task_0-1.xml')
content = dom.findall('result/doc/str')

# Locating URL to donwload .zip files
for url in content:
    if url.text.__contains__('/DLTINS'):
        link = url.text

        # Splitting url for file names
        fileName =  link.split("/")[-1] 
        print(fileName)

        # Downloading zip file
        wg.download(url.text)
        print(f"\nDownloaded: '{fileName}'\n")

        # Extracting file
        with z.ZipFile(fileName, 'r') as file:
            file.extractall()
            print(f'{fileName} extracted.')