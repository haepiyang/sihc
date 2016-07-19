#!/usr/bin/python
import subprocess

print "Static IPv4 Configuration Helper v0.1"
print "Writen in Python3 by Haepi Yang"
print "\n"

sel = ''
while sel == '':
	print "Please select your OS:"
	print "1. Debian"
	print "2. Ubuntu"
	print "3. Fedora"
	print "4. Mint"
	print "5. Elementary"
	print "6. CentOS"
	print "7. OpenSUSE"
	sel = raw_input("\nNumber: ")

	if sel == '1' or sel == '2':
		print "\n"
		print "Removing old generated configuration file..."
		subprocess.call("sudo rm interfaces", shell=True)
		subprocess.call("sudo rm resolv.conf", shell=True)
		subprocess.call("touch interfaces", shell=True)
		subprocess.call("touch resolv.conf", shell=True)

		print "\n"
		print "IPv4 Configuration"

		print "\n"
		print "Please select your interface:"
		subprocess.call("ifconfig", shell=True)

		print "Note: Connection may be broken if you select or input wrong interface!"
		print "Support LAN Connection only"

		iface = ''
		while iface == '':
			iface = raw_input("Interface: ")
			pass

		print "\n"
		ip_addr = raw_input("IPv4 address: ")
		netmask = raw_input("Netmask: ")
		if netmask == '8':
			netmask = "255.0.0.0"
		elif netmask == '16':
			netmask = "255.255.0.0"
		elif netmask == '24':
			netmask = "255.255.255.0"
		elif netmask == '32':
			netmask = "255.255.255.255"
		gateway = raw_input("Default gateway: ")

		with open('interfaces', 'w') as ifacesconf:
			ifacesconf.write("#Interfaces Configuration file - Generated using SICH v0.1\n\n")
			ifacesconf.write("auto lo\niface lo inet loopback\n\n")
			if ip_addr == '':
				print "\nNo IP address was given. Using DHCP"
			else:
				ifacesconf.write("auto "); ifacesconf.write(iface)
				ifacesconf.write("\niface "); ifacesconf.write(iface); ifacesconf.write(" inet static\n")
				ifacesconf.write("\taddress "); ifacesconf.write(ip_addr); ifacesconf.write("\n")
				ifacesconf.write("\tnetmask "); ifacesconf.write(netmask); ifacesconf.write("\n")
				ifacesconf.write("\tgateway "); ifacesconf.write(gateway); ifacesconf.write("\n")
		ifacesconf.closed

		print "\n"
		print "DNS Configuration"
		print "Note: Leave blank if you want to use system default settings"

		print "\n"
		dns1 = raw_input("Preferred DNS Server: ")
		dns2 = raw_input("Alternate DNS Server: ")
		domain = raw_input("Domain: ")
		search = raw_input("Additional search domain: ")

		with open('resolv.conf', 'w') as dnsconf:
			dnsconf.write("#DNS Configuration file - Generated using SICH v0.1\n\n")
			if dns1 != '':
				dnsconf.write("nameserver ")
				dnsconf.write(dns1)
				dnsconf.write("\n")
			if dns2 != '':
				dnsconf.write("nameserver ")
				dnsconf.write(dns2)
				dnsconf.write("\n")
			if dns1 == '' and dns2 == '':
				proc = subprocess.Popen("netstat -r | grep default | awk '{print $2}'", shell=True, env=None, stdout=subprocess.PIPE)
				default_dns = proc.stdout.read()
				dnsconf.write("nameserver ")
				dnsconf.write(default_dns)
				dnsconf.write("\n")
			if domain != '':
				dnsconf.write("domain ")
				dnsconf.write(domain)
				dnsconf.write("\n")
			if search != '':
				dnsconf.write("search ")
				dnsconf.write(search)
				dnsconf.write("\n")
		dnsconf.closed

		print "Saving your configuration..."
		subprocess.call("sudo cp resolv.conf /etc/resolv.conf", shell=True)
		subprocess.call("sudo cp interfaces /etc/network/interfaces", shell=True)
		subprocess.call("sudo service networking restart", shell=True)
		subprocess.call("sudo service network-manager restart", shell=True)
		subprocess.call("sudo rm resolv.conf", shell=True, env=None)
		subprocess.call("sudo rm interfaces", shell=True, env=None)
		break

	elif sel == '3' or sel == '4' or sel == '5' or sel == '6' or sel == '7':
		print "Still in development... :3"
		break

	else:
		print "You have selected the wrong option!"
		sel = ''
	pass

print "\n"
raw_input("Press any key to exit...")
