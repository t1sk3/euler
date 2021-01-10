"""import itertools

def compute():
	# Set up initial array of known/unknown minimum operation counts
	LIMIT = 200
	minoperations = [0, 0] + [None] * (LIMIT - 1)
	numunknown = [LIMIT - 1]  # Use list instead of scalar to work around Python 2's broken scoping
	
	# Recursively builds up chains and compares them to chain lengths already found.
	def explore_chains(chain, maxops):
		# Depth-based termination or early exit
		if len(chain) > maxops or numunknown[0] == 0:
			return
		
		# Try all unordered pairs of values in the current chain
		max = chain[-1]  # Peek at top
		for i in reversed(range(len(chain))):
			for j in reversed(range(i + 1)):
				x = chain[i] + chain[j]
				if x <= max:
					break  # Early exit due to ascending order
				if x <= LIMIT:
					# Append x to the current chain and recurse
					chain.append(x)
					if minoperations[x] is None:
						# For each unique value of x, we set minoperations[x] only once
						# because we do progressive deepening in the depth-first search
						minoperations[x] = len(chain) - 1
						numunknown[0] -= 1
					explore_chains(chain, maxops)
					chain.pop()
	
	
	# Perform bounded depth-first search with incrementing depth
	for ops in itertools.count(1):
		if numunknown[0] == 0:
			# Add up the results
			return str(sum(minoperations))
		explore_chains([1], ops)


if __name__ == "__main__":
	print(compute())
"""


def compute(k):
    if k in res:
        return len(res[k])
    highest = 999999
    lstGood = []
    for i in res:
        for j in res:
            if i + j == k:
                if i != 1 and j != 1:
                    lst1 = []
                    for l in res[i]:
                        if l not in lst1:
                            lst1.append(l)
                    for l in res[j]:
                        if l not in lst1:
                            lst1.append(l)
                    lst1.append([i, j])
                    if len(lst1) < highest:
                        highest = len(lst1)
                        lstGood = lst1
                        #if k == 12:
                            #print("test", i, j, res[i], res[j])
                    if len(lst1) == highest and i == j:
                        highest = len(lst1)
                        lstGood = lst1
                        #if k == 12:
                            #print("test", i, j, res[i], res[j])
    res[k] = lstGood
    return highest

res = {1: [], 2: [[1,1]], 3: [[1, 1],[2,1]], 4: [[1,1],[2,2]]}
lst = []
for i in range(1,201):
    value = compute(i)
    lst.append(value)
#print(lst)
print(sum(lst))
print(res)

