print("Executing DeleteFbeat.py")
import os
from os import system
 
file_size = os.path.getsize('/data/splunk/fbeatip.json')
if(file_size>100000000):
    os.remove("/data/splunk/fbeatip.json")
    system("touch /data/splunk/fbeatip.json")
    system("chmod 666 /data/splunk/fbeatip.json")
    system("docker restart logstash")
#print("File Size is :", file_size, "bytes")
