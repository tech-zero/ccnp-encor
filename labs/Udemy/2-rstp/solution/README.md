◀️ [Parent directory](../) 

---

### Solution:

```
SW1
!
show spanning-tree summary
!
config term
 spanning-tree mode rapid-pvst
end
!
show spanning-tree summary
!
config term
 spanning-tree vlan 100,300 root primary
 spanning-tree vlan 200 root secondary
end
!
show spanning-tree summary
!
show spanning-tree vlan 300
!
config term
 interface gi0/3
  spanning-tree portfast  
end
!  
Show 

SW2
config term
 spanning-tree mode rapid-pvst
end
!  

SW3
config term
 spanning-tree mode rapid-pvst
end
!
config term
 spanning-tree vlan 200 root primary
 spanning-tree vlan 100,300 root secondary
end
!
show spanning-tree summary
!
```

---

▶️ [Next lab](../../../README.md)
