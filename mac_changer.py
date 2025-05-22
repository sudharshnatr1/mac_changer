import subprocess
import argparse

def mac_chang(interface,mac_add):
        subprocess.call(['ifconfig',interface,'down'])
        subprocess.call(['ifconfig',interface,'hw','ether',mac_add])
        subprocess.call(['ifconfig',interface,'up'])
        print(f"the mac_address has been changed of {interface} to {mac_add}")
        subprocess.call(['ifconfig',interface])

if __name__ == "__main__":
        pars = argparse.ArgumentParser(description="change MAC address of a network interface ")
        pars.add_argument("-i",required =True , help=" network interface name (eg wlan0 )" )
        pars.add_argument("-mc",required =True, help=" new MAC address it should have 6 pairs (eg 11:22:33:44:55:66)" )
        args= pars.parse_args()

        mac_chang(args.i,args.mc)
