from netmiko import ConnectHandler

iosv_l3_R1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.177.132',
    'username': 'eddie',
    'password': 'cisco',
}

iosv_l3_R2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.177.134',
    'username': 'eddie',
    'password': 'cisco',
}

iosv_l3_R3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.177.133',
    'username': 'eddie',
    'password': 'cisco',
}


with open('R1-Sol2.ios') as f:
    lines = f.read().splitlines()
print (lines)

all_devices = [iosv_l3_R1]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output)


with open('R2-Sol2.ios') as f:
    lines = f.read().splitlines()
print (lines)

all_devices = [iosv_l3_R2]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output)
    

with open('R3-Sol2.ios') as f:
    lines = f.read().splitlines()
print (lines)

all_devices = [iosv_l3_R3]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output)
