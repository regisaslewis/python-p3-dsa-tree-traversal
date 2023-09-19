class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    ids = []
    nodes_to_check = [n for n in self.root["children"]]

    while len(nodes_to_check) > 0:
      node = nodes_to_check.pop(0)
      ids.append(node)
      nodes_to_check = node["children"] + nodes_to_check

    for n in ids:
      if n["id"] == id:
        return n
    
    return None