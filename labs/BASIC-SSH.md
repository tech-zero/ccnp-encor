# Router/Switch Basic SSH Configuration
### GNS3 NAT node GW (192.168.122.1) in-band network MGMT.
### Config with privilege-level settings
```
hostname XX1
enable secret xxxxx
username admin privilege 15 secret xxxxx
no ip domain-lookup
ip domain-name xxxxx.com
ipv6 unicast-routing
ipv6 cef
logging console
cdp run
! Router connected to GNS3 NAT node gateway
interface GigabitEthernet 0/0
 ip address 192.168.122.XXX 255.255.255.0
 no shutdown
exit
!
! Switch connected to GNS3 NAT node gateway
interface vlan 1
 ip address 192.168.122.XXX 255.255.255.0
 no shutdown
exit
!
crypto key gen rsa <1024>
line vty 0 4
 exec-timeout 0 0
 logging synchronous
 login local
 transport input ssh
exit
wr
```
