
mac_changer.py
==============

Description
-----------
`mac_changer.py` is a Python script that allows users to change the MAC (Media Access Control) address of a specified network interface on Unix/Linux systems. This tool can be useful for anonymity, security testing, or bypassing MAC address filters.

Requirements
------------
- Python 3.x
- Root or sudo privileges
- `ifconfig` installed (typically part of the `net-tools` package)

Usage
-----
Run the script with the following arguments:

    sudo python3 mac_changer.py -i <interface> -ma <new_mac_address>

Arguments
---------
- `-i` : Network interface name (e.g., `eth0`, `wlan0`)
- `-ma`: New MAC address to assign (e.g., `11:22:33:44:55:66`)

Example
-------
    sudo python3 mac_changer.py -i wlan0 -ma 00:11:22:33:44:55

How It Works
------------
The script performs the following actions:
1. Brings the specified network interface down.
2. Changes the MAC address using the `ifconfig` command.
3. Brings the interface back up.
4. Displays the current configuration using `ifconfig`.

Warning
-------
Changing your MAC address may disconnect you from the network or violate network policies. Use this tool responsibly and only on networks you own or have permission to test.

Note
----
If `ifconfig` is not installed, you can install it using:

    sudo apt install net-tools

License
-------
This script is provided as-is for educational and ethical purposes.
