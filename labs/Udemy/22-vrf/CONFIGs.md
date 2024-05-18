# VRF Lab
  
  ## Lab Tasks
  - Globally define three VRFs
  - Configure sub-interfaces for Gig 0/1 on the COMMON router
  - Assign sub-interfaces to VLAN and VRF instances
  - Associate an OSPF routing process with each VRF
  - TENANT A must be assigned to VLAN 2
  - TENANT B must be assigned to VLAN 3
  - TENANT C must be assigned to VLAN 4
 ````
      Building configuration...

      Current configuration : 2921 bytes
      !
      ! Last configuration change at 13:54:27 UTC Sat Jul 1 2023
      !
      version 15.9
      service timestamps debug datetime msec
      service timestamps log datetime msec
      no service password-encryption
      !
      hostname COMMON
      !
      boot-start-marker
      boot-end-marker
      !
      !
      no logging console
      !
      no aaa new-model
      !
      !
      !
      mmi polling-interval 60
      no mmi auto-configure
      no mmi pvc
      mmi snmp-timeout 180
      !
      !
      !
      !
      !
      !
      !
      !
      !
      !
      !
      no ip domain lookup
      ip cef
      no ipv6 cef
      !
      multilink bundle-name authenticated
      !
      !
      !
      !
      !
      redundancy
      !
      !
      !
      !
      !
      !
      !
      !
      !
      !
      !
      !
      !
      !
      !
      interface GigabitEthernet0/0
       no ip address
       shutdown
       duplex auto
       speed auto
       media-type rj45
      !
      interface GigabitEthernet0/1
       no ip address
       shutdown
       duplex auto
       speed auto
       media-type rj45
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
      Building configuration...

      Current configuration : 3100 bytes
      !
      ! Last configuration change at 13:54:18 UTC Sat Jul 1 2023
      !
      version 15.9
      service timestamps debug datetime msec
      service timestamps log datetime msec
      no service password-encryption
      !
      hostname TENANT-A
      !
      boot-start-marker
      boot-end-marker
      !
      !
      no logging console
      !
      no aaa new-model
      !
      !
      !
      mmi polling-interval 60
      no mmi auto-configure
      no mmi pvc
      mmi snmp-timeout 180
      !
      !
      !
      !
      !
      !
      !
      !
      !
      !
      !
      no ip domain lookup
      ip cef
      no ipv6 cef
      !
      multilink bundle-name authenticated
      !
      !
      !
      !
      !
      redundancy
      !
      !
      !
      !
      !
      !
      !
      !
      !
      !
      !
      !
      !
      !
      !
      interface GigabitEthernet0/0
       no ip address
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
      !
      interface GigabitEthernet0/2
       ip address 10.1.1.1 255.255.255.0
       duplex auto
       speed auto
       media-type rj45
      !
      router ospf 1
       network 0.0.0.0 255.255.255.255 area 0
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
      Building configuration...

      Current configuration : 3105 bytes
      !
      ! Last configuration change at 13:54:08 UTC Sat Jul 1 2023
      !
      version 15.9
      service timestamps debug datetime msec
      service timestamps log datetime msec
      no service password-encryption
      !
      hostname TENANT-B
      !
      boot-start-marker
      boot-end-marker
      !
      !
      no logging console
      !
      no aaa new-model
      !
      !
      !
      mmi polling-interval 60
      no mmi auto-configure
      no mmi pvc
      mmi snmp-timeout 180
      !
      !
      !
      !
      !
      !
      !
      !
      !
      !
      !
      no ip domain lookup
      ip cef
      no ipv6 cef
      !
      multilink bundle-name authenticated
      !
      !
      !
      !
      !
      redundancy
      !
      !
      !
      !
      !
      !
      !
      !
      !
      !
      !
      !
      !
      !
      !
      interface GigabitEthernet0/0
       no ip address
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
      !
      interface GigabitEthernet0/2
       ip address 172.16.1.1 255.255.255.0
       duplex auto
       speed auto
       media-type rj45
      !
      router ospf 1
       network 0.0.0.0 255.255.255.255 area 0
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
      Building configuration...

      Current configuration : 3105 bytes
      !
      ! Last configuration change at 13:54:11 UTC Sat Jul 1 2023
      !
      version 15.9
      service timestamps debug datetime msec
      service timestamps log datetime msec
      no service password-encryption
      !
      hostname TENANT-C
      !
      boot-start-marker
      boot-end-marker
      !
      !
      no logging console
      !
      no aaa new-model
      !
      !
      !
      mmi polling-interval 60
      no mmi auto-configure
      no mmi pvc
      mmi snmp-timeout 180
      !
      !
      !
      !
      !
      !
      !
      !
      !
      !
      !
      no ip domain lookup
      ip cef
      no ipv6 cef
      !
      multilink bundle-name authenticated
      !
      !
      !
      !
      !
      redundancy
      !
      !
      !
      !
      !
      !
      !
      !
      !
      !
      !
      !
      !
      !
      !
      interface GigabitEthernet0/0
       no ip address
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
       ip address 192.168.1.1 255.255.255.0
       duplex auto
       speed auto
       media-type rj45
      !
      router ospf 1
       network 0.0.0.0 255.255.255.255 area 0
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
      !
      hostname SW1
      !
      boot-start-marker
      boot-end-marker
      !
      !
      no logging console
      !
      no aaa new-model
      no process cpu extended history
      no process cpu autoprofile hog
      !
      !
      !
      !
      !
      !
      !
      !
      ip cef
      no ipv6 cef
      !
      !
      !
      spanning-tree mode pvst
      spanning-tree extend system-id
      !
      no cdp run
      !
      !
      !
      !
      !
      !
      !
      !
      !
      !
      !
      !
      !
      !
      interface GigabitEthernet0/0
       media-type rj45
       negotiation auto
       no cdp enable
      !
      interface GigabitEthernet0/1
       switchport trunk allowed vlan 2-4
       switchport trunk encapsulation dot1q
       switchport mode trunk
       media-type rj45
       negotiation auto
       no cdp enable
      !
      interface GigabitEthernet0/2
       switchport access vlan 2
       media-type rj45
       negotiation auto
       no cdp enable
      !
      interface GigabitEthernet0/3
       switchport access vlan 3
       media-type rj45
       negotiation auto
       no cdp enable
      !
      interface GigabitEthernet1/0
       switchport access vlan 4
       media-type rj45
       negotiation auto
       no cdp enable
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
      no service-routing capabilities-manager
      !
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
      line aux 0
      line vty 0 4
       exec-timeout 0 0
       login
      !
      !
      end

````
 
```
    Building configuration...

      Current configuration : 2879 bytes
      !
      ! Last configuration change at 13:54:38 UTC Sat Jul 1 2023
      !
      version 15.2
      service timestamps debug datetime msec
      service timestamps log datetime msec
      no service password-encryption
      service compress-config
      !
      hostname Switch
      !
      boot-start-marker
      boot-end-marker
      !
      !
      no logging console
      !
      no aaa new-model
      no process cpu extended history
      no process cpu autoprofile hog
      !
      !
      !
      !
      !
      !
      !
      !
      ip cef
      no ipv6 cef
      !
      !
      !
      spanning-tree mode pvst
      spanning-tree extend system-id
      !
      no cdp run
      !
      !
      !
      !
      !
      !
      !
      !
      !
      !
      !
      !
      !
      !
      interface GigabitEthernet0/0
       media-type rj45
       negotiation auto
       no cdp enable
      !
      interface GigabitEthernet0/1
       media-type rj45
       negotiation auto
       no cdp enable
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
      no service-routing capabilities-manager
      !
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
      line aux 0
      line vty 0 4
       exec-timeout 0 0
       login
      !
      !
      end

````

```      
      Building configuration...

      Current configuration : 2879 bytes
      !
      ! Last configuration change at 13:54:38 UTC Sat Jul 1 2023
      !
      version 15.2
      service timestamps debug datetime msec
      service timestamps log datetime msec
      no service password-encryption
      service compress-config
      !
      hostname Switch
      !
      boot-start-marker
      boot-end-marker
      !
      !
      no logging console
      !
      no aaa new-model
      no process cpu extended history
      no process cpu autoprofile hog
      !
      !
      !
      !
      !
      !
      !
      !
      ip cef
      no ipv6 cef
      !
      !
      !
      spanning-tree mode pvst
      spanning-tree extend system-id
      !
      no cdp run
      !
      !
      !
      !
      !
      !
      !
      !
      !
      !
      !
      !
      !
      !
      interface GigabitEthernet0/0
       media-type rj45
       negotiation auto
       no cdp enable
      !
      interface GigabitEthernet0/1
       media-type rj45
       negotiation auto
       no cdp enable
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
      no service-routing capabilities-manager
      !
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
      line aux 0
      line vty 0 4
       exec-timeout 0 0
       login
      !
      !
      end

```

```  
      Building configuration...

      Current configuration : 2735 bytes
      !
      ! Last configuration change at 13:54:51 UTC Sat Jul 1 2023
      !
      version 15.2
      service timestamps debug datetime msec
      service timestamps log datetime msec
      no service password-encryption
      service compress-config
      !
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
      !
      !
      !
      !
      !
      !
      !
      ip cef
      no ipv6 cef
      !
      !
      !
      spanning-tree mode pvst
      spanning-tree extend system-id
      !
      !
      !
      !
      !
      !
      !
      !
      !
      !
      !
      !
      !
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
      !
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
      line aux 0
      line vty 0 4
       exec-timeout 0 0
       login
      !
      !
      end

```
