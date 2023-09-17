def mergeLinkedLists(nodea,nodeb):
    if nodea is None:
        return nodeb
    if nodeb is None:
        return nodea
    if (nodea.data<nodeb.data):
        nodea.next_node=mergeLinkedLists(nodea.next_node,nodeb)
        return nodea
    else:
        nodeb.next_node=mergeLinkedLists(nodea,nodeb.next_node)
        return nodeb