#把要收尋的關鍵字拿出來
list2=[]
for word in open('tree.txt','r', encoding='utf-8-sig'):
    list2.append(word.strip())


import numpy as np
import math
class TreeNode:
    def __init__(self, value):
        self.left = None;
        self.right = None;
        self.data = value;

class Tree:
    def __init__(self):
        self.root = None;

    def addNode(self, node, value):

        if(node==None):
            self.root = TreeNode(value);
        else:
            if(value<node.data):
                if(node.left==None):
                    node.left = TreeNode(value)
                else:
                    self.addNode(node.left, value);
            else:
                if(node.right==None):
                    node.right = TreeNode(value)
                else:
                    self.addNode(node.right, value);
    def printlevel(self, node):
        if(node!=None):
            print(node.data, end="")
            file.write(node.data+"")
            if(node.left==None and node.right==None):
                pass    
            else:
                print("(", end="")
                file.write("("+"")
                if(node.left==None):
                    print("-", end="")
                    file.write("-"+"")
                else:
                    self.printlevel(node.left)
                print(" ", end="")
                file.write(" "+"")
                if(node.right==None):
                    print("-", end="")
                    file.write("-"+"")
                else:   
                    self.printlevel(node.right)
                print(")", end="")
                file.write(")"+"")
        return
        
    def maxDepth(self, node):
        global height
        if node is None :
            return 0
        else :
            ldepth = self.maxDepth(node.left)
            rdepth = self.maxDepth(node.right)

            if (ldepth>rdepth):
                height=ldepth +1
                return height
            else :
                height=rdepth +1
                return height
    def level(self, node):
        global height
        global m
        global buf
        temp=[]
        temp=buf[height-1]
        if(node!=None):
            #print(height, end=" ")
            #print(node.data)
            temp.append(node.data)
            buf[height-1]=temp
            #print(buf)
            height=height-1
            self.level(node.left)
            self.level(node.right)
            height=height+1
        if(node==None):
            #print("-")
            temp.append("  ")
            buf[height-1]=temp
        return buf
    
    def aaaaa(self, node):
        global height
        global ff
        global levelnumber
        if(node!=None):
            #print(node.data, end="")
            ff.append(node.data)
            levelnumber.append(height)
            if(node.left==None and node.right==None):
                pass    
            else:
             #   print("(", end="")
                height=height-1
                if(node.left==None):
              #      print("-", end="")
                    ff.append("#")
                    levelnumber.append(height)
                    
                else:
                    
                    self.aaaaa(node.left)
                 
               # print(" ", end="")
         
                if(node.right==None):
                #    print("-", end="")
                    ff.append("#")
                    levelnumber.append(height)
                else:   
                    
                    self.aaaaa(node.right)
                height=height+1
               # print(")", end="")
      
        return



#已完成(1.
file = open('parenthesis_representation.txt','w')
for j in range(100):
    height=0
    testTree = Tree()
    z=0
    m=math.ceil((len(list2[j]))/3)
    for  i in range(m):
        a=list2[j][z]+list2[j][z+1]
        testTree.addNode(testTree.root, a)
        z=z+3
    testTree.printlevel(testTree.root)
    print("")
    file.write("\n")
file.close()



# Definition for a  binary tree node
class TreeNode2:
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        ret = '[' + str(self.val) + '] Left -> '
        if self.left:
            ret += str(self.left.val)
        else:
            ret += 'None'

        if self.right:
            ret += ' Right -> ' + str(self.right.val)
        else:
            ret += ' Right -> None'
        return ret


class BinaryTree:
    def __init__(self, serial=None):
        self.__size = 0
        self.__root = None
        self.__height = 0
        if serial:
            if isinstance(serial, list):
                self.construct(serial)
            elif isinstance(serial, TreeNode2):
                self.set_tree(serial)

    # serial should be a list
    def construct(self, serial):
        self.__root = TreeNode2(serial[0])
        self.__height = 1
        self.__size = 1
        que = [[self.__root, 0], [None, 0]]
        newLevel = True
        i = 1
        while i < len(serial):
            top = que[0]
            if newLevel:
                self.__height += 1
                newLevel = False
            if top[0] is None:
                # change level
                newLevel = True
                que = que[1:]
                que.append([None, 0])
                continue
            else:
                # left node
                if top[1] == 0:
                    top[1] = 1
                    if serial[i] != '#':
                        top[0].left = TreeNode2(serial[i])
                        que.append([top[0].left, 0])
                        self.__size += 1
                # right node
                else:
                    que = que[1:]
                    if serial[i] != '#':
                        top[0].right = TreeNode2(serial[i])
                        que.append([top[0].right, 0])
                        self.__size += 1
                i += 1

    def __str__(self):
        level = self.__height
        # leading, margin
        que = [self.__root, None]
        first = True
        item_line = []
        #slash_layer = int( 2** (level - 2))
        slash_layer = int( 1** (level - 2))
        slash_line = [[] for i in range(slash_layer)]
        printed = 0

        ret = ""

        while len(que) > 0 and printed <= self.__height:
            top = que[0]
            que = que[1:]
            if top is None:
                # print items
                ret += ''.join(item_line) #+ '\n'
                # print slash
                for line in slash_line:
                    ret += ''.join(line) + '\n'
                printed += 1
                first = True
                level -= 1
                item_line = []
                slash_layer = int(1 ** (level - 2))
                slash_line = [[] for i in range(slash_layer)]
                if len(que) > 0:
                    que.append(None)
                continue
            if first:
                # print leading SPACE
                item_line.append(' ' * int(2 ** (level - 1) - 1))
                for y in range(slash_layer):
                    slash_line[y].append(' ' * int(2 ** (level - 2) - 1))
                first = False
            if isinstance(top, TreeNode2):
                item_line.append(str(top.val))
                que.append(top.left if top.left else '#')
                que.append(top.right if top.right else '#')
                for line in range(len(slash_line)):
                    for i in range(slash_layer + 1):
                        if i == slash_layer - 1 - line:
                            slash_line[line].append('  ' if top.left else '  ')
                        else:
                            slash_line[line].append(' ')
                for line in range(len(slash_line)):
                    for i in range(slash_layer + int(2 ** (level - 1)) - 1):
                        if i == line:
                            slash_line[line].append('  ' if top.right else ' ')
                        else:
                            slash_line[line].append(' ')
            else:
                que.append('#')
                que.append('#')
                item_line.append(' ')
                for line in slash_line:
                    line.append(' ' * int(2 ** level))
            item_line.append(' ' * int(2 ** level - 1))
        return ret

    def display(self):
        print (str(self))
        file.write(str(self))

    def root(self):
        return self.__root

    def height(self):
        return self.__height

    def set_tree(self, root):
        self.__root = root
        self.__height = 1
        self.__size = 0
        que = [root, None]
        while len(que) > 1:
            top = que.pop(0)
            if top is None:
                que.append(None)
                self.__height += 1
            else:
                self.__size += 1
                if top.left:
                    que.append(top.left)
                if top.right:
                    que.append(top.right)



#2.)  textual_printing.txt
file = open('textual_printing.txt','w')
for j in range(100):
    height=0
    ff=[]
    levelnumber=[]
    testTree = Tree()
    z=0
    m=math.ceil((len(list2[j]))/3)
    for  i in range(m):
        a=list2[j][z]+list2[j][z+1]
        testTree.addNode(testTree.root, a)
        z=z+3
    testTree.maxDepth(testTree.root)
    testTree.aaaaa(testTree.root)
    n,=np.shape(levelnumber)
    kk=[[]]*n
    k=0
    for i in range(height,0,-1):
        #print(height)
        for j in range(n):
            #print (levelnumber[j])
            if levelnumber[j]==height:
                kk[k]=ff[j]
                #print(ff[j],levelnumber[j])
                k=k+1
        height=height-1     
    t1 =BinaryTree(kk)
    t = BinaryTree(t1.root())
    r = t.root()
    t.display()
    print("")
    file.write("\n")
    print("")
    file.write("\n")
    #print("----------------------------------------------------------")
    #file.write("----------------------------------------------------------")
    print("")
    file.write("\n")
file.close()



#已完成 3).
file = open('left_boundary..txt','w')
for j in range(100):
    height=0
    testTree = Tree()
    z=0
    m=math.ceil((len(list2[j]))/3)
    for  i in range(m):
        a=list2[j][z]+list2[j][z+1]
        testTree.addNode(testTree.root, a)
        z=z+3
    testTree.maxDepth(testTree.root)
    buf = [[] for _ in range(height)]
    m=height
    testTree.level(testTree.root)
    answer=[]
    n,=np.shape(buf)
    for i in range(n):
        if buf[i][0]=="  ":
            m,=np.shape(buf[i])
            for j in range(m-1):
                if buf[i][j]!="  ":
            #print(buf[i][1])
                    answer.append(buf[i][j])
                    break
        else:
            #print(buf[i][0])
            answer.append(buf[i][0])
    n,=np.shape(answer)
    for i in range(n):
        file.write(str(answer[i])+" ")
    file.write("\n")
file.close()