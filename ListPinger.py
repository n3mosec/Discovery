import os

#File for list of IPs
IP_List = open("IP_List", "r")

List = IP_List.readlines()

for ip in List:
	response = os.system("ping -c 1 " + ip)
	if (response == 0):
		status = ip.rstrip() + " is up!"
	else:
		status = ip + " is down :("
	print(status)
