#!/usr/bin/env python

import subprocess
import optparse
import re

def take_input():
	parser = optparse.OptionParser()
	parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address")
	parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
	(options, arguments) = parser.parse_args()
	if not options.interface:
		parser.error("wrong interface, use --help for more information.")
	elif not options.new_mac:
		parser.error("wrong MAC, use --help for more information.")
	return options

def mac_change(interface, new_mac): #changing Mac address
	print(" |#|#| Changing MAC adress for " + interface + " to " + new_mac + " |#|#| ")
	subprocess.call(["ifconfig", interface, "down"])
	subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
	subprocess.call(["ifconfig", interface, "up"])

def show_current_mac(interface):
	result = subprocess.check_output(["ifconfig", options.interface])
	search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", result)
	if search_result:
		return search_result.group(0)		
	else:
		print("Coud not find MAC address.")

def did_it_changed(interface, new_mac):
	current_mac = show_current_mac(options.interface)
	if current_mac == options.new_mac:
		print("Youre MAC was changed.")
	else:
		print("MAC did not changed.")

options = take_input()
current_mac = show_current_mac(options.interface)
print("Current MAC = " + str(current_mac))
mac_change(options.interface, options.new_mac) #Starting MAC change
did_it_changed(options.interface, options.new_mac)