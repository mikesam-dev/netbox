# NetBox v2.10

## v2.10-beta1 (FUTURE)

**NOTE:** This release completely removes support for embedded graphs.

### New Features

* [#1692](https://github.com/netbox-community/netbox/issues/1692) - Allow assigment of inventory items to parent items in web UI
* [#4956](https://github.com/netbox-community/netbox/issues/4956) - Include inventory items on primary device view
* [#5003](https://github.com/netbox-community/netbox/issues/5003) - CSV import now accepts slug values for choice fields
* [#5146](https://github.com/netbox-community/netbox/issues/5146) - Add custom fields support for cables, power panels, rack reservations, and virtual chassis

### Other Changes

* [#1846](https://github.com/netbox-community/netbox/issues/1846) - Enable MPTT for InventoryItem hierarchy
* [#4349](https://github.com/netbox-community/netbox/issues/4349) - Dropped support for embedded graphs
* [#4360](https://github.com/netbox-community/netbox/issues/4360) - Remove support for the Django template language from export templates
* [#4878](https://github.com/netbox-community/netbox/issues/4878) - Custom field data is now stored directly on each object
* [#4941](https://github.com/netbox-community/netbox/issues/4941) - `commit` argument is now required argument in a custom script's `run()` method

### REST API Changes

* dcim.Cable: Added `custom_fields`
* dcim.InventoryItem: The `_depth` field has been added to reflect MPTT positioning
* dcim.PowerPanel: Added `custom_fields`
* dcim.RackReservation: Added `custom_fields`
* dcim.VirtualChassis: Added `custom_fields`
* extras.ExportTemplate: The `template_language` field has been removed
* extras.Graph: This API endpoint has been removed (see #4349)