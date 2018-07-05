class Node:
	def __init__(self, letter, fullStr, branches, word):
		self.letter = letter
		self.fullStr = fullStr
		self.branches = branches
		self.word = word
		
def printTree(currNode):
	if currNode.word:
		print(currNode.fullStr)
		
	if len(currNode.branches) == 0:
		return
	else:
		for node in currNode.branches:
			printTree(node)

def findNode(headNode, str):
	currNode = headNode
	for letter in str:
		found = False
		for node in currNode.branches:
			if letter == node.letter:
				found = True
				currNode = node
				if currNode.fullStr == str:
					return currNode
		if not found:
			return None	
	return None
	
file = open('wordlist.txt', 'r')
headNode = Node('', '', [], False)
for line in file:
	word = line.strip()
	currNode = headNode
	for i in range(len(word)):
		inNode = False
		for node in currNode.branches:
			if word[i] == node.letter:
				currNode = node
				inNode = True
		if inNode == False:
			newNode = Node(word[i], word[:i+1], [], False)
			currNode.branches.append(newNode)
			currNode = newNode
		if i == len(word)-1:
			currNode.word = True

catNode = findNode(headNode, 'cat')
printTree(catNode)
			

			