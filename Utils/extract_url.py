# Code to extract PPG - "PLETH" and BP - "ABP" data from the MIMIC 2 waveform database
# Author - Subham Agrawal
# email - sagwl96@gmail.com
# date - 15-Oct-2020

# Finishing all the imports at the start of the program
import urllib.request as UR

# Important urls
base_url = "https://archive.physionet.org/physiobank/database/mimic2wdb/"  # Base URL for MIMIC 2 Waveform Database
records_waveform_url = "https://archive.physionet.org/physiobank/database/mimic2wdb/RECORDS-waveforms"  # URL for
# waveform database
records_adult_url = "https://archive.physionet.org/physiobank/database/mimic2wdb/RECORDS-adults"  # URL of only Adult
# Records


# function for opening url to check for available records
def url_contents(url):
    if (url == base_url) or (url == records_waveform_url) or (url == records_adult_url):
        file = UR.urlopen(url)
        content = file.readlines()
        file.close()
        return [line.decode("utf8").strip() for line in content]  # returning the list of records in usable format
    else:
        print("Entered wrong url, please check and try again")
        return 0


listAdultRecords = url_contents(records_adult_url)

def record_content(listRecord):
    f = open("c:/Users/Subham/Desktop/Code/Bandless/pleth_abp_mimic2_urls.txt","a")
    print("file creation should be about done now")
    for record in listRecord:
        url = base_url + record + "RECORDS"
        file = UR.urlopen(url)
        content = [line.decode("utf8").strip() for line in file.readlines()]
        file.close()
        for item in content:
            nURL = base_url + record + item + ".hea"
            file = UR.urlopen(nURL)
            cont = file.read().decode("utf8")
            if ("PLETH" in cont) and ("ABP" in cont):
                f.write(nURL+"\n")
    f.close()


record_content(listAdultRecords)
