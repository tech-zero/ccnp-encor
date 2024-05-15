### Solution
```
R3
!
router bgp 65001
bgp router-id 3.3.3.3
neighbor 10.1.1.2 remote-as 65001
neighbor 198.51.100.2 remote-as 65002
neighbor 198.51.100.6 remote-as 65004
network 10.1.1.0 mask 255.255.255.0
end
!
show ip bgp
ping 5.5.5.5
!
```

[BGP labs](../../)

[Lab exam items](../../../)
