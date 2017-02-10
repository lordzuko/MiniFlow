class Node(object):
    def __init__(self, inbound_nodes=[]):
        # Node(s) from which this node recieves values
        self.inbound_nodes = inbound_nodes
        #Node(s) to which this Node passes values
        self.outbound_nodes = []
        # For each inbound node here, add this Node as an outbound Node to _that_Node
        for n in self.inbound_nodes:
            n.outbound_nodes.append(self)
        # A calculated value
        self.value = None

    def forward(self):
        """
        Forward Propagation

        Compute the output value based on `inbound_nodes` and
        store the result in self.value
        :return:
        """
        raise NotImplemented

    