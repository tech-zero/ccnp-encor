# Day 1 Review Lab 2

## Objective
In this lab, we continue to review configuration and troubleshooting concepts covered in ENCOR 350-401 exam topics. 

## Topology
In this lab, you are responsible for completing the multi-VRF configuration of the network supporting sales users and HR users.  On completion, there should be full end-to-end rechability, and the two groups should not be able to communicate with each other.  Be careful to verify that your configurations meet the provided specifications and that the devices perform as required.  

For this lab, you need three routers (IOS, IOSv, or IOS XE), three switches (Layer 2/Layer 3), and four Windows or Linux PCs.

## Addressing Table
The following table provides the IPv4 and IPv6 addresses for all devices in this review lab.

**Review Lab 2 Addressing Table**
<table>
<tr><th>Device</th><th>Interface</th><th>IPv4 Address</th><th>IPv6 Address</th><th>IPv6 Link-Local</th></tr>
<tr><td>HQ<td>G0/0.1</td><td>172.16.10.1/24</td><td>2001:db8:172:10::1/64</td><td>fe80::1:1</td></tr>
<tr><td></td><td>G0/0.2</td><td>172.16.10.1/24</td><td>2001:db8:172:10::1/64</td><td>fe80::1:2</td></tr>
<tr><td></td><td>G0/1.1</td><td>172.16.101.1/24</td><td>2001:db8:172:101::1/64</td><td>fe80::1:3</td></tr>
<tr><td></td><td>G0/1.2</td><td>172.16.102.1/24</td><td>2001:db8:172:102::1/64</td><td>fe80::1:4</td></tr>
<tr><td>WAN<td>G0/0.1</td><td>172.16.10.2/24</td><td>2001:db8:172:10::2/64</td><td>fe80::2:1</td></tr>
<tr><td></td><td>G0/0.2</td><td>172.16.10.2/24</td><td>2001:db8:172:10::2/64</td><td>fe80::2:2</td></tr>
<tr><td></td><td>G0/1.1</td><td>172.16.11.2/24</td><td>2001:db8:172:11::2/64</td><td>fe80::2:3</td></tr>
<tr><td></td><td>G0/1.2</td><td>172.16.11.2/24</td><td>2001:db8:172:11::2/64</td><td>fe80::2:4</td></tr>
<tr><td>BR<td>G0/0.1</td><td>172.16.201.3/24</td><td>2001:db8:172:11::3/64</td><td>fe80::3:1</td></tr>
<tr><td></td><td>G0/0.2</td><td>172.16.202.3/24</td><td>2001:db8:172:11::3/64</td><td>fe80::3:2</td></tr>
<tr><td></td><td>G0/1.1</td><td>172.16.11.3/24</td><td>2001:db8:172:11::3/64</td><td>fe80::3:3</td></tr>
<tr><td></td><td>G0/1.2</td><td>172.16.11.3/24</td><td>2001:db8:172:11::3/64</td><td>fe80::3:4</td></tr>
<tr><td>PC1<td> NIC </td><td>172.16.101.50/24</td><td>2001:db8:172:101::50/64</td><td>EUI-64</td></tr>
<tr><td><td></td><td>DG: 172.16.101.1/24</td><td>DG: 2001:db8:172:101::1/64</td><td></td></tr>
<tr><td>PC2<td> NIC </td><td>172.16.201.50/24</td><td>2001:db8:172:201::50/64</td><td>EUI-64</td></tr>
<tr><td><td></td><td>DG: 172.16.201.3/24</td><td>DG: 2001:db8:172:201::3/64</td><td></td></tr>
<tr><td>PC3<td> NIC </td><td>172.16.102.50/24</td><td>2001:db8:172:102::50/64</td><td>EUI-64</td></tr>
<tr><td><td></td><td>DG: 172.16.102.1/24</td><td>DG: 2001:db8:172:102::1/64</td><td></td></tr>
<tr><td>PC4<td> NIC </td><td>172.16.202.50/24</td><td>2001:db8:172:202::50/64</td><td>EUI-64</td></tr>
<tr><td><td></td><td>172.16.202.3/24</td><td>DG: 2001:db8:172:202::3/64</td><td></td></tr>
</table>

### Tasks
The tasks for this review lab are broken up into four parts:
+ **Part 1:** Build the Network and Configure Basic Device Settings

+ **Part 2:** Configure VRF and Static Routing

+ **Part 3:** Configure Layer 2 Network

+ **Part 4:** Configure Secure Access
