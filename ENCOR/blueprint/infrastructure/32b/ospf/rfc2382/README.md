### OSPF Version 2 (OSPFv2)

Defined in [RFC 2382](https://datatracker.ietf.org/doc/html/rfc2382) and supports IPv4

### Broadcast

Broadcast media such as Ethernet are better defined as broadcast multi-access to distinguish them from non-broadcast multi-access (NBMA) networks. Broadcast networks are multi-access in that they are capable of connecting more than two devices, and broadcasts sent out one interface are capable of reaching all interfaces attached to that segment.

The OSPF network type is set to broadcast by default for Ethernet interfaces. A DR is required for this OSPF network type because of the possibility that multiple nodes can exist on a segment, and LSA flooding needs to be controlled. The hello timer defaults to 10 seconds, as defined in [RFC 2382](https://datatracker.ietf.org/doc/html/rfc2382).
The interface parameter command ip ospf network broadcast overrides the automatically configured setting and statically sets an interface as an OSPF broadcast network type.

