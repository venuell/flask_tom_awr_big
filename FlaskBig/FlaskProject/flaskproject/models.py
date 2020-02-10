import subprocess
from flask import flash
import time

tomcatShutdownPeriod = 10

def isProcessRunning(server_name):
    pStatus = True
    tProcess = subprocess.Popen(["ssh",server_name,"ps -ef | grep -v grep | grep 'jmxremote.port=' | wc -l"], stdout=subprocess.PIPE)
    out, err = tProcess.communicate()
    if out=='':
        flash("could not connect/execute on server" +server_name ,"error")
        return
    elif int(out) <1:
        pStatus = False
    return pStatus

def status(server_name):
    if isProcessRunning(server_name):
        tPid = subprocess.Popen(["ssh",server_name,"ps -ef | grep -v grep | grep 'jmxremote.port=' | awk \'{print $2}\'"], stdout=subprocess.PIPE)
        out, err = tPid.communicate()
        flash ("Tomcat process on " +server_name +" is running with PID " + str(out),"success")
    else:
        flash ("Tomcat process on " +server_name +" is not running", "error")



def start(server_name):
    if isProcessRunning(server_name):
        flash ("Tomcat process on " +server_name +"  is already running", "success")
    else:
        flash ("Starting the tomcat on " +server_name, "success")
        subprocess.call(["ssh",server_name,"service tomcat_xe_DPD8_8100 start"])
        status(server_name)

def stop(server_name):
    if isProcessRunning(server_name):
        flash ("Stopping the tomcat on " +server_name,"success" )
        subprocess.call(["ssh",server_name,"service tomcat_xe_DPD8_8100 stop"])
        #time.sleep(tomcatShutdownPeriod)
        status(server_name)
        if isProcessRunning(server_name):
            tPid = subprocess.Popen(["ssh",server_name,"ps -ef | grep -v grep | grep 'jmxremote.port=///' | awk \'{print $2}\'"], stdout=subprocess.PIPE)
            out, err = tPid.communicate()
            subprocess.Popen(["kill -9 " + out])
            flash ("Tomcat on " +server_name +" failed to shutdown, so killed with PID " + out,"success")
    else:
        flash("Tomcat process on " +server_name +" is not running","success")

def restart(server_name):
    stop(server_name)
    start(server_name)

