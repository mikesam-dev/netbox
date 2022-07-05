# Wireless LANs

A wireless LAN is a set of interfaces connected via a common wireless channel. Each instance must have an SSID, and may optionally be correlated to a VLAN. Wireless LANs can be arranged into hierarchical groups.

An interface may be attached to multiple wireless LANs, provided they are all operating on the same channel. Only wireless interfaces may be attached to wireless LANs.

An existing tenant may be attached to multiple wireless LANs. This can be done by using the netbox UI.
- Adding/Editing a Wireless LAN - Select an existing tenant's name in the drop-down field in the `Tenancy` section
- Wireless LAN Bulk Import - CSV data must include a field for `tenant`. The value must be a valid name for an existing tenant
    ```
    ssid,tenant
    my_ssid,my_name
    ```

Each wireless LAN may have authentication attributes associated with it, including:

* Authentication type
* Cipher
* Pre-shared key
