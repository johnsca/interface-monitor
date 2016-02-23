from charms.reactive import scopes
from charms.reactive import RelationBase
from charms.reactive import hook


class MonitoringRequires(RelationBase):
    scope = scopes.UNIT

    @hook('{requires:monitor}-relation-joined')
    def joined(self):
        self.set_state('{relation_name}.available')

    @hook('{requires:monitor}-relation-departed')
    def departed(self):
        self.remove_state('{relation_name}.available')

    def endpoints(self):
        """
        Returns a list of monitoring hosts.
        """
        return [conv.get_remote('private-address') for conv in self.conversations()]

    def port(self):
        """
        Returns the port upon which the monitoring hosts are listening.
        """
        return 8649  # currently hard-coded in the Ganglia charm :(
