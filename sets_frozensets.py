# sets and frozen sets practices - Vivi

print "initializing sets"
# duplications will not be keep in sets
vowels = set(["a", "e", "i", "o", "u", "u"])
letters = set(["x", "y", "z"])
print "letters: ", letters
print "vowels: ", vowels

print "====================="
print ""
print "adding elements"
# it's mutable
# add elements
letters.add("b")
letters.add("c")
letters.add("o")
letters.add("e")
print letters

# duplicates will not be added
letters.add("y")
print letters
print "===================="

print ""
print "removing elements"
# remove elements
letters.remove("x")
letters.remove("y")
print letters
print "==================="
print ""

# find intersection
print "intersection: ", letters.intersection(vowels)
print "==================="
print ""

# find differences
print "difference and difference update"
print vowels.difference(letters)
print letters.difference(vowels)

# find difference and discard them from the set
print "vowels:", vowels
print "letters:", letters
vowels.difference_update(letters)
print vowels
print letters
print "=================="
# see if the 2 lists has nothing in common
print vowels.isdisjoint(letters)


print "---------frozen sets ----------"
# frozen sets are imputable, i.e cannot add, remove..etc

frozen1 = frozenset("vivi")
frozen2 = frozenset("ashu")
frozen3 = frozenset(["ashu"])
frozen4 = frozenset(["vivi"])

#some operations on frozensets
print frozen1
print frozen2
print frozen3
print frozen4
print frozen1.difference(frozen2)
print frozen1.union(frozen2)
print frozen1.isdisjoint(frozen2)