### OSPFv3 Address Families Configuration Lab   
#### Lab Tasks
- Configure OSPFv3 for R3, R4, and R5 using the address families method
-
- All R3 interfaces are in Area 1
-
- R4's Gig 0/1 interface is in Area 1
-
- R4's Gig 0/2 interface is in Area 0
-
- All R5 interfaces are in Area 0
-
- R1 and R2 are already configured for routing

```
      hostname R1
      !
      logging console
      cdp run
      !
      no ip domain lookup
      ip cef
      ipv6 unicast-routing
      ipv6 cef
      !
      interface Loopback0
       ip address 1.1.1.1 255.255.255.255
      !
      interface GigabitEthernet0/0
       ip address 10.255.0.155 255.255.0.0
       no shutdown
       duplex auto
       speed auto
       media-type rj45
      !
      interface GigabitEthernet0/1
       ip address 192.168.1.1 255.255.255.0
       no shutdown
       duplex auto
       speed auto
       media-type rj45
       ipv6 address 2000:1::1/64
       ipv6 eigrp 1
      !
      interface GigabitEthernet0/2
       ip address 192.0.0.1 255.255.255.252
       no shutdown
       duplex auto
       speed auto
       media-type rj45
       ipv6 address 2000:2::1/64
       ipv6 eigrp 1
      !
      router eigrp 1
       network 0.0.0.0
      !
      ip forward-protocol nd
      !
      !
      no ip http server
      no ip http secure-server
      !
      ipv6 router eigrp 1
      !
      ipv6 ioam timestamp
      !
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
      no ip domain lookup
      ip cef
      ipv6 unicast-routing
      ipv6 cef
      !
      interface Loopback0
       no ip address
      !
      interface GigabitEthernet0/0
       ip address 10.255.0.156 255.255.0.0
       shutdown
       duplex auto
       speed auto
       media-type rj45
      !
      interface GigabitEthernet0/1
       ip address 192.0.0.2 255.255.255.252
       duplex auto
       speed auto
       media-type rj45
       ipv6 address 2000:2::2/64
       ipv6 eigrp 1
      !
      interface GigabitEthernet0/2
       ip address 192.0.2.1 255.255.255.252
       duplex auto
       speed auto
       media-type rj45
       ipv6 address 2000:3::1/64
       ipv6 ospf 1 area 1
       ospfv3 2 ipv4 area 1
      !
      router eigrp 1
       network 192.0.0.0 0.0.0.3
       redistribute ospf 1 metric 100000 10 255 1 1500
      !
      router ospfv3 2
       router-id 2.2.2.2
       !
       address-family ipv4 unicast
        redistribute eigrp 1
       exit-address-family
      !
      router ospf 1
       redistribute eigrp 1 subnets
       network 192.0.2.0 0.0.0.3 area 1
      !
      ip forward-protocol nd
      !
      no ip http server
      no ip http secure-server
      !
      ipv6 router eigrp 1
      !
      ipv6 router ospf 1
       router-id 2.2.2.2
       redistribute eigrp 1
      !
      ipv6 ioam timestamp
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
      no ip domain lookup
      ip cef
      ipv6 unicast-routing
      ipv6 cef
      !
      interface Loopback0
       no ip address
      !
      interface GigabitEthernet0/0
       ip address 10.255.0.157 255.255.0.0
       shutdown
       duplex auto
       speed auto
       media-type rj45
      !
      interface GigabitEthernet0/1
       ip address 192.0.2.2 255.255.255.252
       duplex auto
       speed auto
       media-type rj45
       ipv6 address 2000:3::2/64
      !
      interface GigabitEthernet0/2
       ip address 198.51.100.1 255.255.255.252
       duplex auto
       speed auto
       media-type rj45
       ipv6 address 2000:4::1/64
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
      hostname R4
      !
      logging console
      cdp run
      !
      no ip domain lookup
      ip cef
      ipv6 unicast-routing
      ipv6 cef
      !
      multilink bundle-name authenticated
      !
      interface Loopback0
       no ip address
      !
      interface GigabitEthernet0/0
       ip address 10.255.0.158 255.255.0.0
       shutdown
       duplex auto
       speed auto
       media-type rj45
      !
      interface GigabitEthernet0/1
       ip address 198.51.100.2 255.255.255.252
       duplex auto
       speed auto
       media-type rj45
       ipv6 address 2000:4::2/64
      !
      interface GigabitEthernet0/2
       ip address 203.0.113.1 255.255.255.252
       duplex auto
       speed auto
       media-type rj45
       ipv6 address 2000:5::1/64
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

```
      hostname R5
      !
      logging console
      cdp run
      !
      no ip domain lookup
      ip cef
      ipv6 unicast-routing
      ipv6 cef
      !
      interface Loopback0
       no ip address
      !
      interface GigabitEthernet0/0
       ip address 10.255.0.159 255.255.0.0
       shutdown
       duplex auto
       speed auto
       media-type rj45
      !
      interface GigabitEthernet0/1
       ip address 203.0.113.2 255.255.255.252
       no shutdown
       duplex auto
       speed auto
       media-type rj45
       ipv6 address 2000:5::2/64
      !
      interface GigabitEthernet0/2
       ip address 172.16.1.1 255.255.255.0
       no shutdown
       duplex auto
       speed auto
       media-type rj45
       ipv6 address 2000:6::1/64
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
      ip cef
      no ipv6 cef
      !
      spanning-tree mode pvst
      spanning-tree extend system-id
      !
      !
      interface GigabitEthernet0/0
       media-type rj45
       negotiation auto
      !
      interface GigabitEthernet0/1
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
   
