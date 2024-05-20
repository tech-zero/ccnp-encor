### BGP for IPv6 Lab
#### Lab Tasks
- Create a route map to advertise next-hop IPv6 address
    
- Configure BGP routing process

- Create IPv4 and IPv6 address families

- Activate IPv6 address family neighbor

- Associate route map with neighbor, apply outbound
  
```
      hostname R1
      !
      logging console
      cdp run!
      !
      !
      no ip domain lookup
      ip cef
      ipv6 cef
      !
      multilink bundle-name authenticated
      !
      interface GigabitEthernet0/0
       ip address 10.255.1.147 255.255.0.0
       shutdown
       duplex auto
       speed auto
       media-type rj45
      !
      interface GigabitEthernet0/1
       ip address 172.16.1.1 255.255.255.0
       no shutdown
       duplex auto
       speed auto
       media-type rj45
      !
      router bgp 65001
       bgp router-id 1.1.1.1
       bgp log-neighbor-changes
       network 172.16.1.0 mask 255.255.255.0
       neighbor 172.16.1.2 remote-as 65001
      !
      no ip http server
      no ip http secure-server
      !
      ipv6 ioam timestamp
      !
      !
      banner exec ^^
      banner incoming ^^
      banner login ^^
      !
      line con 0
       exec-timeout 0 0
       logging synchronous
      line aux 0
      line vty 0 4
       exec-timeout 0 0
       password cisco
       login
       transport input none
      line vty 5 15
       exec-timeout 0 0
       password cisco
       login
       transport input none
      !
      no scheduler allocate
      !
      end
```

```
      hostname R2
      !
      logging console
      cdp run
      !
      !
      no ip domain lookup
      ip cef
      ipv6 cef
      !
      !
      interface GigabitEthernet0/0
       ip address 10.255.1.148 255.255.0.0
       shutdown
       duplex auto
       speed auto
       media-type rj45
      !
      interface GigabitEthernet0/1
       ip address 172.16.1.2 255.255.255.0
       no shutdown
       duplex auto
       speed auto
       media-type rj45
      !
      interface GigabitEthernet0/2
       ip address 10.1.1.2 255.255.255.0
       no shutdown
       duplex auto
       speed auto
       media-type rj45
      !
      router bgp 65001
       bgp router-id 2.2.2.2
       bgp log-neighbor-changes
       network 10.1.1.0 mask 255.255.255.0
       network 172.16.1.0 mask 255.255.255.0
       neighbor 10.1.1.1 remote-as 65001
       neighbor 172.16.1.1 remote-as 65001
      !
      ip forward-protocol nd
      !
      !
      no ip http server
      no ip http secure-server
      !
      ipv6 ioam timestamp
      !
      !
      !
      control-plane
      !
      banner exec ^^
      banner incoming ^^
      banner login ^^
      !
      line con 0
       exec-timeout 0 0
       logging synchronous
      line aux 0
      line vty 0 4
       exec-timeout 0 0
       password cisco
       login
       transport input none
      line vty 5 15
       exec-timeout 0 0
       password cisco
       login
       transport input none
      !
      no scheduler allocate
      !
      end
```

```
      hostname R3
      !
      logging console
      cdp run
      !
      no aaa new-model
      !
      no ip domain lookup
      ip cef
      ipv6 unicast-routing
      ipv6 cef
      !
      interface Loopback1
       no ip address
       ipv6 address 2000:1::1/64
      !
      interface GigabitEthernet0/0
       ip address 10.255.1.149 255.255.0.0
       shutdown
       duplex auto
       speed auto
       media-type rj45
      !
      interface GigabitEthernet0/1
       ip address 10.1.1.1 255.255.255.0
       no shutdown
       duplex auto
       speed auto
       media-type rj45
      !
      interface GigabitEthernet0/2
       ip address 198.51.100.1 255.255.255.252
       no shutdown
       duplex auto
       speed 10
       media-type rj45
      !
      interface GigabitEthernet0/3
       ip address 198.51.100.5 255.255.255.252
       no shutdown
       duplex auto
       speed 100
       media-type rj45
       ipv6 address 2000:2::1/64
      !
      ip forward-protocol nd
      !
      !
      no ip http server
      no ip http secure-server
      !
      ipv6 ioam timestamp
      !
      !
      !
      control-plane
      !
      banner exec ^^
      banner incoming ^^
      banner login ^^
      !
      line con 0
       exec-timeout 0 0
       logging synchronous
      line aux 0
      line vty 0 4
       exec-timeout 0 0
       password cisco
       login
       transport input none
      line vty 5 15
       exec-timeout 0 0
       password cisco
       login
       transport input none
      !
      no scheduler allocate
      !
      end
```

```
      hostname ISP1
      !
      logging console
      cdp run
      !
      no ip domain lookup
      ip cef
      no ipv6 cef
      !
      !
      interface GigabitEthernet0/0
       ip address 10.255.1.145 255.255.0.0
       shutdown
       duplex auto
       speed auto
       media-type rj45
      !
      interface GigabitEthernet0/1
       ip address 198.51.100.2 255.255.255.252
       no shutdown
       duplex auto
       speed auto
       media-type rj45
      !
      interface GigabitEthernet0/2
       ip address 203.0.113.1 255.255.255.252
       no shutdown
       duplex auto
       speed auto
       media-type rj45
      !
      router bgp 65002
       bgp router-id 4.4.4.4
       bgp log-neighbor-changes
       network 198.51.100.0 mask 255.255.255.252
       network 203.0.113.0 mask 255.255.255.252
       neighbor 198.51.100.1 remote-as 65001
       neighbor 203.0.113.2 remote-as 65003
      !
      ip forward-protocol nd
      !
      !
      no ip http server
      no ip http secure-server
      !
      ipv6 ioam timestamp
      !
      !
      !
      control-plane
      !
      banner exec ^^
      banner incoming ^^
      banner login ^^
      !
      line con 0
       exec-timeout 0 0
       logging synchronous
      line aux 0
      line vty 0 4
       exec-timeout 0 0
       password cisco
       login
       transport input none
      line vty 5 15
       exec-timeout 0 0
       password cisco
       login
       transport input none
      !
      no scheduler allocate
      !
      end
```
```
      hostname ISP2
      !
      logging console
      cdp run
      !
      no ip domain lookup
      ip cef
      ipv6 unicast-routing
      ipv6 cef
      !
      interface Loopback1
       no ip address
       ipv6 address 2000:3::1/64
      !
      interface GigabitEthernet0/0
       ip address 10.255.1.146 255.255.0.0
       shutdown
       duplex auto
       speed auto
       media-type rj45
      !
      interface GigabitEthernet0/1
       ip address 198.51.100.6 255.255.255.252
       no shutdown
       duplex auto
       speed auto
       media-type rj45
       ipv6 address 2000:2::2/64
      !
      interface GigabitEthernet0/2
       ip address 203.0.113.6 255.255.255.252
       no shutdown
       duplex auto
       speed auto
       media-type rj45
      !
      ip forward-protocol nd
      !
      ipv6 ioam timestamp
      !
      !
      !
      control-plane
      !
      banner exec ^^
      banner incoming ^^
      banner login ^^
      !
      line con 0
       exec-timeout 0 0
       logging synchronous
      line aux 0
      line vty 0 4
       exec-timeout 0 0
       password cisco
       login
       transport input none
      line vty 5 15
       exec-timeout 0 0
       password cisco
       login
       transport input none
      !
      no scheduler allocate
      !
      end
```


```
      hostname Switch
      !
      logging console
      cdp run
      !
      no aaa new-model
      !
      ip cef
      no ipv6 cef
      !
      spanning-tree mode pvst
      spanning-tree extend system-id
      !
      interface GigabitEthernet0/0
       media-type rj45
       negotiation auto
      !
      interface GigabitEthernet0/1
       media-type rj45
       negotiation auto
      !
      interface GigabitEthernet0/2
       media-type rj45
       negotiation auto
      !
      ip forward-protocol nd
      !
      no ip http server
      no ip http secure-server
      !
      ip ssh server algorithm encryption aes128-ctr aes192-ctr aes256-ctr
      ip ssh client algorithm encryption aes128-ctr aes192-ctr aes256-ctr
      !
      control-plane
      !
      banner exec ^^
      banner incoming ^^
      banner login ^^
      !
      line con 0
       exec-timeout 0 0
      line aux 0
      line vty 0 4
       exec-timeout 0 0
       login
      !
      !
      end
```

```
      hostname Switch
      !
      boot-start-marker
      boot-end-marker
      !
      !
      no logging console
      !
      no aaa new-model
      !
      ip cef
      ipv6 cef
      !
      spanning-tree mode pvst
      spanning-tree extend system-id
      !
      interface GigabitEthernet0/0
       media-type rj45
       negotiation auto
      !
      interface GigabitEthernet0/1
       media-type rj45
       negotiation auto
      !
      interface GigabitEthernet0/2
       media-type rj45
       negotiation auto
      !
      ip forward-protocol nd
      !
      no ip http server
      no ip http secure-server
      !
      ip ssh server algorithm encryption aes128-ctr aes192-ctr aes256-ctr
      ip ssh client algorithm encryption aes128-ctr aes192-ctr aes256-ctr
      !
      line con 0
       exec-timeout 0 0
      line aux 0
      line vty 0 4
       exec-timeout 0 0
       login
      !
      !
      end
```
    
```
      hostname INET
      logging console
      cdp run
      !
      no ip domain lookup
      ip cef
      ipv6 cef
      !
      interface Loopback0
       ip address 5.5.5.5 255.255.255.0
      !
      interface GigabitEthernet0/0
       ip address 10.255.1.144 255.255.0.0
       shutdown
       duplex auto
       speed auto
       media-type rj45
      !
      interface GigabitEthernet0/1
       ip address 203.0.113.2 255.255.255.252
       duplex auto
       speed auto
       media-type rj45
      !
      interface GigabitEthernet0/2
       ip address 203.0.113.5 255.255.255.252
       duplex auto
       speed auto
       media-type rj45
      !
      router bgp 65003
       bgp router-id 5.5.5.5
       bgp log-neighbor-changes
       network 5.5.5.0 mask 255.255.255.0
       network 203.0.113.0 mask 255.255.255.252
       network 203.0.113.4 mask 255.255.255.252
       neighbor 203.0.113.1 remote-as 65002
       neighbor 203.0.113.6 remote-as 65004
      !
      ip forward-protocol nd
      !
      !
      no ip http server
      no ip http secure-server
      !
      ipv6 ioam timestamp
      !
      line con 0
       exec-timeout 0 0
       logging synchronous
      line aux 0
      line vty 0 4
       exec-timeout 0 0
       password cisco
       login
       transport input none
      line vty 5 15
       exec-timeout 0 0
       password cisco
       login
       transport input none
      !
      no scheduler allocate
      !
      end
```
