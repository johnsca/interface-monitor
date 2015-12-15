# Overview

This interface layer handles the communication between any service and a service that
provides monitoring facilities (eg Ganglia).


# Usage

## Requires

Charms in need of an acces to a monitoring service require this interface.

This interface layer will set the following state, as appropriate:

  * `{relation_name}.available`   The relation to the monitoring service has been
    established. The charm can retrieve the IP of the monitorin service through a call to:
    * `endpoint()`.

For example, let's say that a charm wants to use the monitoring service. The charm should
specify the relation through which the monitoring service is becoming available, in this case
we call this relation ``ganglia''.

```python
@when('ganlia.available')
def setup_monitoring(ganglia):
    ip = ganglia.endpoint()
```

## Provides

A charm providing monitoring services should implement this interface.

As soon as a ``monitor'' relation is established the '{relation_name}.available' state is set.
The service provider can use the configure method to populate the 'hostname' relation data variable.
If the 'hostname' data variable is not set the consumer of the monitor service will fall back to use the
'private_address' of the relation.

# Contact Information

- <bigdata@lists.ubuntu.com>
