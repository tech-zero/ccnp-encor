:arrow_backward: [Parent directory](../)

---

### Solution:
```
R1
!
conf t
 ip flow export version 9
!
interface gi0/1
 ip flow ingress
 ip flow egress
exit
!
ip flow-export destination 10.1.1.5 9999
exit
!
show ip flow interface
show ip flow export
end
!
show ip cache flow

PC1
ping 172.16.10.1
!

R1
!
show ip cache flow
!
```

---

:arrow_forward: [Next lab](../../../labs/rspan/README.md)
