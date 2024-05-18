### Review Lab 1

#### Router EDGE

```
hostname EDGE
ipv6 unicast-routing
no ip domain lookup
banner motd # EDGE, 31 Days ENCOR - Review Lab 1 #
line con 0
 exec-timeout 0 0
 logging synchronous
 exit
interface g0/0/0
 ip address 198.51.100.1 255.255.255.252
 ipv6 address fe80::1:1 link-local
 ipv6 address 2001:db8:198:51::1/64
 no shutdown
 exit
interface g0/0/1
 ip address 172.16.11.1 255.255.255.0
 ipv6 address fe80::1:2 link-local
 ipv6 address 2001:db8:172:11::1/64
 no shutdown
 exit
interface g0/0/2
 ip address 172.16.13.1 255.255.255.0
 ipv6 address fe80::1:3 link-local
 ipv6 address 2001:db8:172:13::1/64
 no shutdown
 exit

```

#### Router ISP
```
hostname ISP
ipv6 unicast-routing
no ip domain lookup
banner motd # ISP, 31 Days ENCOR - Review Lab 1 #
line con 0
 exec-timeout 0 0
 logging synchronous
 exit
interface g0/0/0
 ip address 198.51.100.2 255.255.255.252
 ipv6 address fe80::2:1 link-local
 ipv6 address 2001:db8:198:51::2/64
 no shutdown
 exit
interface Loopback 0
 ip address 203.0.113.1 255.255.255.255
 ipv6 address fe80::2:3 link-local
 ipv6 address 2001:db8:203:113::1/128
 no shutdown
 exit

```

#### Router HQ

```
hostname HQ
ipv6 unicast-routing
no ip domain lookup
banner motd # HQ, 31 Days ENCOR - Review Lab 1 #
line con 0
 exec-timeout 0 0
 logging synchronous
 exit
interface g0/0/1
 ip address 172.16.10.1 255.255.255.0
 ipv6 address fe80::3:2 link-local
 ipv6 address 2001:db8:172:10::1/64
 no shutdown
 exit
interface g0/0/2
 ip address 172.16.13.2 255.255.255.0
 ipv6 address fe80::3:3 link-local
 ipv6 address 2001:db8:172:13::2/64
 no shutdown
 exit
```

#### Switch DIST1

```
hostname DIST1
ip routing
ipv6 unicast-routing
no ip domain lookup
banner motd # DIST1, 31 Days ENCOR - Review Lab 1 #
line con 0
 exec-timeout 0 0
 logging synchronous
 exit
vlan 100
 name Management
 exit
vlan 101
 name HR
 exit
vlan 102
 name Sales
 exit
vlan 999
 name NATIVE
 exit
interface g1/0/11
 no switchport
 ip address 172.16.11.2 255.255.255.0
 ipv6 address fe80::d1:1 link-local
 ipv6 address 2001:db8:172:11::2/64
 no shutdown
 exit
interface vlan 100
 ip address 172.16.100.1 255.255.255.0
 ipv6 address fe80::d1:2 link-local
 ipv6 address 2001:db8:172:100::1/64
 no shutdown
 exit
interface vlan 101
 ip address 172.16.101.1 255.255.255.0
 ipv6 address fe80::d1:3 link-local
 ipv6 address 2001:db8:172:101::1/64
 no shutdown
 exit
interface vlan 102
 ip address 172.16.102.1 255.255.255.0
 ipv6 address fe80::d1:4 link-local
 ipv6 address 2001:db8:172:102::1/64
 no shutdown
 exit
ip dhcp excluded-address 172.16.101.1 172.16.101.109
ip dhcp excluded-address 172.16.101.141 172.16.101.254
ip dhcp excluded-address 172.16.102.1 172.16.102.109
ip dhcp excluded-address 172.16.102.141 172.16.102.254
ip dhcp pool VLAN-101
 network 172.16.101.0 255.255.255.0
 default-router 172.16.101.254
 exit
ip dhcp pool VLAN-102
 network 172.16.102.0 255.255.255.0
 default-router 172.16.102.254
 exit
```

#### Switch DIST2
```
hostname DIST2
ip routing
ipv6 unicast-routing
no ip domain lookup
banner motd # DIST2, 31 Days ENCOR - Review Lab 1 #
line con 0
 exec-timeout 0 0
 logging synchronous
 exit
vlan 100
 name Management
 exit
vlan 101
 name HR
 exit
vlan 102
 name Sales
 exit 
vlan 999
 name NATIVE
 exit
interface g1/0/11
 no switchport
 ip address 172.16.10.2 255.255.255.0
 ipv6 address fe80::d1:1 link-local
 ipv6 address 2001:db8:172:10::2/64
 no shutdown
 exit
interface vlan 100
 ip address 172.16.100.2 255.255.255.0
 ipv6 address fe80::d2:2 link-local
 ipv6 address 2001:db8:172:100::2/64
 no shutdown
 exit
interface vlan 101
 ip address 172.16.101.2 255.255.255.0
 ipv6 address fe80::d2:3 link-local
 ipv6 address 2001:db8:172:101::2/64
 no shutdown
 exit
interface vlan 102
 ip address 172.16.102.2 255.255.255.0
 ipv6 address fe80::d2:4 link-local
 ipv6 address 2001:db8:172:102::2/64
 no shutdown
 exit
ip dhcp excluded-address 172.16.101.1 172.16.101.209
ip dhcp excluded-address 172.16.101.241 172.16.101.254
ip dhcp excluded-address 172.16.102.1 172.16.102.209
ip dhcp excluded-address 172.16.102.241 172.16.102.254
ip dhcp pool VLAN-101
 network 172.16.101.0 255.255.255.0
 default-router 172.16.101.254
 exit
ip dhcp pool VLAN-102
 network 172.16.102.0 255.255.255.0
 default-router 172.16.102.254
 exit
```

#### Switch ASW1
```
hostname ASW1
no ip domain lookup
banner motd # ASW1, 31 Days ENCOR - Review Lab 1 #
line con 0
 exec-timeout 0 0
 logging synchronous
 exit
vlan 100
 name Management
 exit
vlan 101
 name HR
 exit
vlan 102
 name Sales
 exit
vlan 999
 name NATIVE
 exit
interface vlan 100
 ip address 172.16.100.3 255.255.255.0
 ipv6 address fe80::a1:1 link-local
 ipv6 address 2001:db8:172:100::3/64
 no shutdown
 exit
```
