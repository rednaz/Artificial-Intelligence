import Edge

class Graph:
    def __init__(self):
        self.Nodes = list()

    def AddNode(self, node):
        self.Nodes.Add(node)

    def AddDirected(self, startNode, endNode):
        startNode.Edges.Add(Edge(endNode))

    def AddBiDirectedEdge(self, startNode, endNode):
        self.AddDirectedNode(startNode, endNode)
        self.AddDirectedNode(endNode, startNode)