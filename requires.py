from charms.reactive import scopes
from charms.reactive import RelationBase
from charmhelpers.core import hookenv
from charms.reactive import hook

class MonitoringRequires(RelationBase):
    scope = scopes.UNIT

    @hook('{requires:monitor}-relation-{joined,changed}')
    def changed(self):
        self.set_state('{relation_name}.available')

    @hook('{requires:monitor}-relation-{departed,broken}')
    def broken(self):
        self.remove_state('{relation_name}.available')

    def endpoint(self):
        """
        Returns the monitoring endpoint.
        """
        service = hookenv.remote_unit()
        if service:
            conv = self.conversation(scope=service)
            pa = conv.get_remote('hostname') or conv.get_remote('private-address')
            return pa
        else:
            return None
