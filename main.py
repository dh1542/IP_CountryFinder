import re
import geoip2.webservice
import geoip2.database
import requests



# Country from IP Lookup – Enter an IP address and find the country that IP is registered in.


# A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 0 <= xi <= 255 and xi cannot contain leading zeros. For example, 
# "192.168.1.1" and "192.168.1.0" are valid IPv4 addresses but "192.168.01.1", while "192.168.1.00" and "192.168@1.1" are invalid IPv4 addresses.



# Method to validate ip address
def validate_IP(IP):
	if "." in IP:
		nums = IP.split('.')
		if(len(nums) == 4):
			for e in nums:

				if(e.isnumeric() == False):
					return False
				elif(len(e) != 1 and int(e) == 0):
					return False
				elif(len(e) >= 4 or len(e) <= 0 or int(e) > 255 or int(e) < 0):
					return False
				
			return 4
		else:
			return False
	# A valid IPv6 address is an IP in the form "x1:x2:x3:x4:x5:x6:x7:x8" where: 1 <= xi.length <= 4xi is a hexadecimal string which may contain digits, 
	# lower-case English letter ('a' to 'f') and upper-case English letters ('A' to 'F'). Leading zeros are allowed in xi.
	elif ":" in IP:
		nums = IP.split(':')
		if(len(nums) == 8):
			for e in nums:
				if(len(e) <= 0 or len(e) > 4):
					return False
				if(e.isnumeric() == False):
					if(re.search('[a-fA-F]', e) == False):
						return False
			return 6

	else:
		return False

				

ip = "179.58.96.128"

# /Users/dominik/Documents/Projects/IP_CountryFinder/GeoLite2-City_20210309/GeoLite2-City.mmdb
with geoip2.database.Reader('/Users/dominik/Documents/Projects/IP_CountryFinder/GeoLite2-City_20210309/GeoLite2-City.mmdb') as reader:
	response = reader.city(ip)
	print(response.country.iso_code)
	print(response.city.name)
	
		

















