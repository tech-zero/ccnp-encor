## Day 2 Review Lab 1

### Objective
This lab reviews some of the configuration and troubleshooting concepts covered in the ENCOR 350-401 Exam Topics.  

### Topology
In this lab, complete the configuration of the network so that:  
+ There is full end-to-end reachability.  All PCs should be able to ping Loopback 0 on the ISP router.
+ Hosts have reliable default gateway support in the event of a failure at the distribution layer.
+ Management protocols such as NetFlow, SNMP, syslog, NTP, and AAA are operational within the HQ Network part of the topology.

Be careful to verify that your configurations meet the provided specifications and that the devices perform as required.   

For this review lab, you need three routers (IOS, IOSv, or IOS XE), three switches (Layer 2/Layer 3), and four Windows or Linux PCs.

🔽 [Download the gns3 lab](./d2lab1.gns3project.zip)

---
![Lab topology](https://github.com/tech-zero/assets/blob/main/images/gns3-img2.png)

---

### Addressing Table - provides the IPv4 and IPv6 addresses for all devies in this review lab.
![Lab topology](https://github.com/tech-zero/assets/blob/main/images/2address-table.png)

---

### Tasks
The tasks for this review lab are broken up into six parts:
+ [**Part 1:** Build the Network and Configure Basic Device Settings and Interface Addressing](https://github.com/tech-zero/assets/blob/main/d2lab1/part1/README.md)

+ [**Part 2:** Configure the Layer 2 Network and Host Support](https://github.com/tech-zero/assets/blob/main/d2lab1/part2/README.md)

+ [**Part 3:** Configure Routing Protocols](https://github.com/tech-zero/assets/blob/main/d2lab1/part3/README.md)

+ [**Part 4:** Configure First-Hop Redundancy and IP SLA Functionality](https://github.com/tech-zero/assets/blob/main/d2lab1/part4/README.md)

+ [**Part 5:** Configure Secure Access](https://github.com/tech-zero/assets/blob/main/d2lab1/part5/README.md)

+ [**Part 6:** Configure Network Management Features](https://github.com/tech-zero/assets/blob/main/d2lab1/part6/README.md)
