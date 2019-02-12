import subprocess
import time
import os

shell_file = os.getcwd()+"/ip_getter.sh"
xx = open('test_file.txt','w')
xx.write(os.getcwd())
xx.close()

while True:
    # get my ip address:
    subprocess.call(shell_file,shell=True)
    f_new = open('new_ip.txt','r')
    f_old = open('old_ip.txt','r')

    ip_new = f_new.readline()
    ip_old = f_old.readline()

    f_new.close()
    f_old.close()
    if (ip_new == ""):
        time.sleep(10)
        continue
    if (ip_new != ip_old):
        script_file = os.getcwd()+"/tg_sendip.sh \""+ip_new+"\""
        subprocess.call(script_file,shell=True)
        f = open('old_ip.txt','w')
        f.write(ip_new)
        f.close()
    time.sleep(120)
    print("New IP is: "+ip_new)
    print("Old IP is: "+ip_old)

