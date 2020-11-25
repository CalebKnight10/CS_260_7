class TreeNode:
    def __init__(self,key,val,left=None,right=None,parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasChild(self):
        return self.rightChild or self.leftChild

    def hasBothChild(self):
        return self.rightChild and self.leftChild

    def splice(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasChild():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent

    def findSuccessor(self): # Not Recursive
        node = self
        found = False
        succ = None
        while not found:
            if node.hasRightChild():
                succ = node.rightChild.findMin()
                found = True
            elif not node.hasRightChild() and node.parent.leftChild == node:
                succ = node.parent
                found = True
            else:
                node.parent.rightChild = None
                node = node.parent
        return succ

    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current


class Binary_Search_Tree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def put(self,key,val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
        self.size = self.size + 1

    def _put(self,key,val,current):
        if key < current.key:
            if current.hasLeftChild():
                   self._put(key,val,current.leftChild)
            else:
                   current.leftChild = TreeNode(key,val,parent=current)
        else:
            if current.hasRightChild():
                   self._put(key,val,current.rightChild)
            else:
                   current.rightChild = TreeNode(key,val,parent=current)

    def __setitem__(self,k,v):
       self.put(k,v)

    def get(self,key):
       if self.root:
           res = self._get(key,self.root)
           if res:
                  return res.payload
           else:
                  return None
       else:
           return None

    def get_node(self,key):
       if self.root:
           res = self._get(key,self.root)
           if res:
                  return res
           else:
                  return None
       else:
           return None

    def _get(self,key,current):
       if not current:
           return None
       elif current.key == key:
           return current
       elif key < current.key:
           return self._get(key,current.leftChild)
       else:
           return self._get(key,current.rightChild)

    def __getitem__(self,key):
       return self.get(key)

    def __contains__(self,key):
       if self._get(key,self.root):
           return True
       else:
           return False

    def delete(self,key):
      if self.size > 1:
         node_Remove = self._get(key,self.root)
         if node_Remove:
             self.remove(node_Remove)
             self.size = self.size-1
         else:
             raise KeyError('Error, key not in tree')
      elif self.size == 1 and self.root.key == key:
         self.root = None
         self.size = self.size - 1
      else:
         raise KeyError('Error, key not in tree')

    def __delitem__(self,key):
       self.delete(key)

    def remove(self,current):
         if current.isLeaf(): #leaf
           if current == current.parent.leftChild:
               current.parent.leftChild = None
           else:
               current.parent.rightChild = None
         elif current.hasBothChild(): #interior
           succ = current.findSuccessor()
           succ.splice()
           current.key = succ.key
           current.payload = succ.payload

         else: # this node has one child
           if current.hasLeftChild():
             if current.isLeftChild():
                 current.leftChild.parent = current.parent
                 current.parent.leftChild = current.leftChild
             elif current.isRightChild():
                 current.leftChild.parent = current.parent
                 current.parent.rightChild = current.leftChild
             else:
                 current.replaceNodeData(current.leftChild.key,
                                    current.leftChild.payload,
                                    current.leftChild.leftChild,
                                    current.leftChild.rightChild)
           else:
             if current.isLeftChild():
                 current.rightChild.parent = current.parent
                 current.parent.leftChild = current.rightChild
             elif current.isRightChild():
                 current.rightChild.parent = current.parent
                 current.parent.rightChild = current.rightChild
             else:
                 current.replaceNodeData(current.rightChild.key,
                                    current.rightChild.payload,
                                    current.rightChild.leftChild,
                                    current.rightChild.rightChild)


def main():
    my_Tree = Binary_Search_Tree()
    my_Tree[2]="orange"
    my_Tree[5]="gray"
    my_Tree[4]="blue"
    my_Tree[7]="green"
    my_Tree[3]="at"
    print(my_Tree[1])
    print(my_Tree[4])
    print(my_Tree[7])
    print(my_Tree.get_node(5).findSuccessor().payload)
    print(my_Tree.get_node(4).payload)


if __name__ == '__main__':
    main()