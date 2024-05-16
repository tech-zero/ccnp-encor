◀️ [Parent directory](../) 

---
### vBond Orchestrator
The vBond orchestrator is a virtualized vEdge running a dedicated function of the vBond persona. Devices can locate the vBond through specific IP addresses or fully qualified domain names (FQDNs). Using an FQDN is preferred because it allows for horizontal scaling of vBond devices and flexibility if a vBond ever needs to change its IP address.
The major components of the vBond orchestrator are

- **Authentication:** The vBond is responsible for authenticating every device in the fabric. As a device comes online, it must authenticate to the vBond, which determines the eligibility to join the SD-WAN fabric. Basic authentication of an SD-WAN router is done using certificates and RSA cryptography.
  
- **NAT detection:** The vBond can detect when devices are being placed behind NAT devices using Session Traversal Utilities for NAT (STUN) [RFC 5389] mechanisms. Placing a vBond behind a NAT device is not recommended but requires a 1:1 static NAT if it is placed behind a NAT device.

- **Load balancing:** The vBond provides load balancing of sessions to fabrics that have multiple vSmart or vManage controllers.

Every vBond has a permanent control plane connection over a [Datagram Transport Layer Security (DTLS)](https://github.com/tech-zero/encor-study/blob/main/assets/terms/DTLS/README.md) tunnel with every vSmart controller. As edge devices authenticate with the vBond, they are directed to the appropriate vSmart and vManage device. NAT is detected, and then the edge device session is torn down. A session with vBond is formed across all edge device transports so that NAT detection can take place for every circuit.
