◀️ [Parent directory](../) 

#️⃣ [lab configs](./rfilter.yaml)

In this lab, take a look at how to filter routes coming in from another area and this topology already has OSPF and EIGRP configured as shown in the diagram.

Connect to R5 and do a show ip route.  Notice that we see two inter-area routes being learned from area 1.
192.0.2.0 and 198.51.100.0

Your goal for this lab is to filter these two interarea routes that are being learned from OSPF Area 1.  That filtering will be done on the area border router (ABR), which in this topology will be R4.  Perform that filtering using a prefix list and we want to apply that prefix list so that we filter advertisements going into area zero.

---

### OSPF Route Filtering Lab

![Lab topology](https://github.com/tech-zero/assets/blob/main/images/rfilter.png)

### Lab Tasks:
- Filter out two inter-area routes learned from OSPF Area 1
- Setup prefix list on ABR (R4)

---

:white_check_mark: [CLI reference](https://github.com/tech-zero/assets/blob/main/solutions/32b-ospf-rfilter.md)
