
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
 
class SLinkedList:
    def __init__(self):
        self.headval = None
 
# 添加节点
    def insert(self,middle_node,newdata):
        if not middle_node:
            print("The mentioned node is absent")
            return
 
        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode
 
# 打印列表
    def show(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval
 
 
li = SLinkedList()
li.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Thu")
 
li.headval.nextval = e2
e2.nextval = e3
 
li.insert(li.headval.nextval,"Tue")
 
li.show()
