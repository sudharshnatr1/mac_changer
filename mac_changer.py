import subprocess
import argparse
import re
def mac_chang(interface,mac_add):
        subprocess.call(['ifconfig',interface,'down'])
        subprocess.call(['ifconfig',interface,'hw','ether',mac_add])
        subprocess.call(['ifconfig',interface,'up'])
        result=subprocess.check_output(['ifconfig',interface]).decode('utf-8')
        mac_result=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",result)
        if mac_result:
                if mac_add == mac_result.group(0):
                        print(f"the mac_address has been changed of {interface} to {mac_add}")
                        subprocess.call(['ifconfig',interface])
                else:
                        print("the mac has not been changed")
        else:
                print("mac address cannot be found")

if __name__ == "__main__":
        pars = argparse.ArgumentParser(description="change MAC address of a network interface ")
        pars.add_argument("-i",required =True , help=" network interface name (eg wlan0 )" )
        pars.add_argument("-mc",required =True, help=" new MAC address it should have 6 pairs (eg 11:22:33:44:55:66)" )
        args= pars.parse_args()
        mac_chang(args.i,args.mc)
