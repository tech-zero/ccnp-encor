### Rapid PVST+ Lab 
#### Lab Tasks
- Configure Rapid PVST+ on all switches
    
- VLANs 100, 300 Primary Root = SW1, Secondary Root = SW3
    
- VLAN 200 Primary Root = SW3, Secondary Root = SW1
    
- Configure Gig 0/3 as an edge port type

---
```
      hostname SW2
      !
      boot-start-marker
      boot-end-marker
      !
      vtp mode transparent
      !
      ip cef
      no ipv6 cef
      !
      spanning-tree mode mst
      spanning-tree extend system-id
      !
      spanning-tree mst configuration
       instance 1 vlan 100, 300
       instance 2 vlan 200
      !
      !
      vlan 100
       name ACCT
      !
      vlan 200
       name SALES
      !
      vlan 300
       name DATA
      no cdp run
      !
      !
      interface GigabitEthernet0/0
       media-type rj45
       negotiation auto
       no cdp enable
      !
      interface GigabitEthernet0/1
       switchport trunk encapsulation dot1q
       switchport mode dynamic desirable
       media-type rj45
       negotiation auto
       no cdp enable
      !
      interface GigabitEthernet0/2
       switchport trunk encapsulation dot1q
       switchport mode trunk
       media-type rj45
       negotiation auto
       no cdp enable
      !
      interface GigabitEthernet0/3
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
      hostname SW1
      !
      boot-start-marker
      boot-end-marker
      !
      !
      logging console
      !
      no aaa new-model
      no process cpu extended history
      no process cpu autoprofile hog
      !
      vtp mode transparent
      !
      ip cef
      no ipv6 cef
      !
      spanning-tree mode mst
      spanning-tree extend system-id
      !
      spanning-tree mst configuration
       instance 1 vlan 100, 300
       instance 2 vlan 200
      !
      spanning-tree mst 1 priority 24576
      spanning-tree mst 2 priority 28672
      !
      !
      vlan 100
       name ACCT
      !
      vlan 200
       name SALES
      !
      vlan 300
       name DATA
      cdp run
      !
      !
      interface GigabitEthernet0/0
       media-type rj45
       negotiation auto
       no cdp enable
      !
      interface GigabitEthernet0/1
       switchport access vlan 100
       switchport trunk encapsulation dot1q
       switchport mode dynamic desirable
       media-type rj45
       negotiation auto
       no cdp enable
      !
      interface GigabitEthernet0/2
       switchport access vlan 100
       switchport trunk encapsulation dot1q
       switchport mode dynamic desirable
       media-type rj45
       negotiation auto
       no cdp enable
      !
      interface GigabitEthernet0/3
       switchport access vlan 300
       media-type rj45
       negotiation auto
       no cdp enable
      !
      interface GigabitEthernet1/0
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
      no service-routing capabilities-manager
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
      hostname SW3
      !
      logging console
      !
      vtp mode transparent
      !
      ip cef
      no ipv6 cef
      !
      spanning-tree mode mst
      spanning-tree extend system-id
      spanning-tree mst configuration
       instance 1 vlan 100, 300
       instance 2 vlan 200
      !
      spanning-tree mst 1 priority 28672
      spanning-tree mst 2 priority 24576
      !
      vlan 100
       name ACCT
      !
      vlan 200
       name SALES
      !
      vlan 300
       name DATA
      cdp run
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
      interface GigabitEthernet0/2
       media-type rj45
       negotiation auto
       no cdp enable
      !
      interface GigabitEthernet0/3
       media-type rj45
       negotiation auto
       no cdp enable
      !
      interface GigabitEthernet1/0
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
