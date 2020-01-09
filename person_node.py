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

	def are_connected(self,person1,person2):
		"""Checks to see if two freinds are connected using bredth first search"""
		possible_nodes = []
		accounted_for = set()


		possible_nodes.append(person1)
		accounted_for.add(person1)

		while len(possible_nodes) != 0:

			person = possible_nodes.pop(0)
			if person == person2:
				return True
			else:
				for friend in person.adjacent - accounted_for:
					possible_nodes.append(friend)
					accounted_for.add(friend)

		return False




	def connection_level(self,person1,person2):
			"""Checks two nodes level of connecton, first connection, second connection etc."""
			
			if self.are_connected(person1,person2):

				possible_nodes = []
				accounted_for = set()

				connection = 1

				possible_nodes.append(person1)
				accounted_for.add(person1)

				added = 0
				popped = 0

				while len(possible_nodes) != 0:
					
					person = possible_nodes.pop(0)
					popped += 1

					if person == person2:
						f"{person1.name} and {person2.name} are {connection} connections"
					else:
						for friend in person.adjacent - accounted_for:
							possible_nodes.append(friend)
							accounted_for.add(friend)
							added += 1

					if added == popped:

						connection += 1

				return f"{person1.name} and {person2.name} are {connection} connections"

			else:

				return f"{person1.name} and {person2.name} are not connected."









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



print(friends.connection_level(harry,ron))
print(friends.connection_level(ron,trevor))
print(friends.connection_level(harry,draco))




