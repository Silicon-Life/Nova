from .node import Node

class CommunicationManager:
    def __init__(self):
        self.nodes = []

    def register_node(self, node):
        self.nodes.append(node)

    def create_publisher(self, node_name, topic):
        node = self.get_node(node_name)
        return node.create_publisher(topic)

    def create_subscription(self, node_name, topic, callback):
        node = self.get_node(node_name)
        return node.create_subscription(topic, callback)

    def create_service(self, node_name, service_name, callback):
        node = self.get_node(node_name)
        return node.create_service(service_name, callback)

    def create_action(self, node_name, action_name, callback):
        node = self.get_node(node_name)
        return node.create_action(action_name, callback)

    def get_node(self, node_name):
        for node in self.nodes:
            if node.name == node_name:
                return node
        raise ValueError(f"Node {node_name} not found")
