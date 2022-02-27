class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        
        self.parent_id = parent_id
class Node:

    def __init__(self, node_id):
        
        self.node_id = node_id
        
        self.children = []
        
def BuildTree(records) -> Node:
    
    records.sort(key = lambda record: record.record_id)

    if len(records) == 0:

        return None
        
    if records[-1].record_id != len(records) - 1:
        
        raise ValueError('Record id is invalid or out of order.')

    tree = []
    
    for record in records:
        if record.record_id < record.parent_id:

            raise ValueError("Node record_id should be smaller than it's parent_id.")
            
        if record.record_id == record.parent_id and record.record_id != 0:
            
            raise ValueError("Only root should have equal record and parent id.")

        node = Node(record.record_id)
        
        tree.append(node)

        if node.node_id != 0:

            tree[record.parent_id].children.append(node)

    return tree[0]