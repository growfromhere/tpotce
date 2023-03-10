from os import system,stat
from subprocess import check_output
import requests
import json
import time

print("Executing Logstash Monitoring")
slack_webhook="https://hooks.slack.com/services/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"
try:
    lastf = open("/data/SiteReliability/last_read_ptr.txt","r")
    read_from=lastf.read()
    lastf.close()
except:
    #lastf = open("myfile.txt","w")
    read_from=0
logf = open("/var/lib/docker/containers/4d3e8ceabd8915a0d0780425ed4e456c5bb992d3d260544617809a8894cb8268/4d3e8ceabd8915a0d0780425ed4e456c5bb992d3d260544617809a8894cb8268-json.log", "r")
logf.seek(0, 2)
last_read=logf.tell()
logf.seek(int(read_from))
all_logs=logf.readlines(last_read)
logf.close()
for line in all_logs:
    if("WARN" in line or "ERROR" in line or "FATAL" in line):
        if("[logstash.filters." not in line and "[logstash.codecs." not in line):
            line="Alert from Logstash-Honeypot-Docker: "+line
            response=requests.post(slack_webhook, json.dumps({'text': line}))
            #print(response.text)
            if("Pipeline worker error, the pipeline will be stopped" in line):
                time.sleep(5)
                response=system("docker restart logstash")
                #pidof_java=check_output(["pidof","java"]).strip().decode("utf-8")
                #response=system("kill -9 "+pidof_java)
                time.sleep(10)
                #pidof_java=check_output(["pidof","java"]).strip().decode("utf-8")
                slack_message="Restarted logstash Docker on Honeypot Server "
                response=requests.post(slack_webhook, json.dumps({'text': slack_message}))
            #print(line)
            #input()
lastf = open("/data/SiteReliability/last_read_ptr.txt","w")
lastf.write(str(last_read))
lastf.close()
print("Completed Logstash Monitoring")
