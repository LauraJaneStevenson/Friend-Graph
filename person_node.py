class PersonNode(object):

	def __init__(self,name, adjecent = None):

		self.name = name
		if not adjecent:
			adjacent = set()
		# throw error if adjacent isn't a set
		assert isinstance(adjacent, set), \
			"adjacent must be a set!"
            
		self.adjacent = adjacent 


	def __repr__(self):
		"""Returns a human readable node obj"""

		return f"<PersonNode: {self.name}>"



class FriendGraph(object):

	def __init__(self):

		self.nodes = set()

	def __repr__(self):

		return f"<FriendGraph: {[friend.name for friend in self.nodes]}>"

	def add_friend(self,friends):
		"""add friend node to graph"""

		for friend in friends:
			self.nodes.add(friend)

	def connect_friends(self, person1, person2):
		"""connect two person nodes"""

		person1.adjacent.add(person2)
		person2.adjacent.add(person1)



harry = PersonNode("Harry")
hermione = PersonNode("Hermione")
ron = PersonNode("Ron")
neville = PersonNode("Neville")
trevor = PersonNode("Trevor")
fred = PersonNode("Fred")
draco = PersonNode("Draco")
crabbe = PersonNode("Crabbe")
goyle = PersonNode("Goyle")

friends = FriendGraph()
friends.add_friend([harry, hermione, ron, neville, fred, draco, crabbe, goyle])

friends.connect_friends(harry, hermione)
friends.connect_friends(harry, ron)
friends.connect_friends(harry, neville)
friends.connect_friends(hermione, ron)
friends.connect_friends(neville, hermione)
friends.connect_friends(neville, trevor)
friends.connect_friends(ron, fred)
friends.connect_friends(draco, crabbe)
friends.connect_friends(draco, goyle)





