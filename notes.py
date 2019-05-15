"""That data.strip().split(',') line looks a little weird. Can you explain what’s going on?

A: That’s called method chaining. The first method, strip(), is applied to the line in data, which removes any unwanted whitespace
from the string. Then, the results of the stripping are processed by the second method, split(','), creating a list. The resulting list is
then applied to the target identifier in the previous code. In this way, the methods are chained together to produce the required result. It helps
if you read method chains from left to right.
"""

"""By default, both the sort() method and the sorted()
BIF order your data in ascending order. To order your data in
descending order, pass the reverse=True argument to
either sort() or sorted() and Python will take care of
things for you."""


"""The sort() method changes the
ordering of lists in-place.
 The sorted() BIF sorts most any data
structure by providing copied sorting.
 Pass reverse=True to either
sort() or sorted() to arrange your
data in descending order.
 When you have code like this:
new_l = []
for t in old_l:
new_l.
append(len(t))
rewrite it to use a list comprehension,
like this:
new_l = [len(t) for t
in old_l]
 To access more than one data item from
a list, use a slice. For example:
my_list[3:6]
accesses the items from index location 3
up-to-but-not-including index location 6.
 Create a set using the set() factory
function."""