from Node import Node

class Input(Node):
    def __init__(self):
        # An input node that has no inbound nodes,
        # so no need to pass anything to the Node initiator
        Node.__init__(self)

        # NOTE: Input node is the only node where the value
        # may be passed as an argument to forward()
        #
        # All other node implementations should get the value
        # of the previous node from self.inbound_nodes
        #
        # Example:
        # val0 = self.inbound_nodes[0].value