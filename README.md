# Overview

This interface layer handles the communication between any service and a service that
provides monitoring facilities (currently only Ganglia).


# Usage

## Requires

Charms in need of an access to a monitoring service require this interface.

This interface layer will set the following state, as appropriate:

  * `{relation_name}.available`   The relation to the monitoring service has been
    established. The charm can retrieve information about the monitoring service via:
    * `endpoints()`  Returns a list of monitoring hosts
    * `port()`  Returns the port the monitoring service is listening on

For example, let's say that a charm wants to use the monitoring service. The charm should
specify the relation through which the monitoring service is becoming available, in this case
we call this relation "ganglia".

```python
@when('ganglia.available')
def setup_monitoring(ganglia):
    for host in ganglia.endpoints():
        register_monitor(host, ganglia.port())
```

## Provides

The providing side of this relation currently does not explicitly send any data.

# Contact Information

- <bigdata@lists.ubuntu.com>
