with open("james.txt") as jaf:#Open the file.
    data=jaf.readline()#Read the line of data.
james=data.split(',') #split=Convert the data to a list.
""" if split() then output ['2-34,3:21,2.34,2.45,3.01,2:01,2:01,3:10,2-22'] 
means only 1 value and each value will not iterate 
therfore use split(',') = ['2-25', '2-55', '2.18', '2.58', '2:39', '2:54', '2:55', '2:55', '2:58'] """
with open("julie.txt") as ju:
    data = ju.readline()
julie=data.strip().split(',')
with open("mikey.txt") as mi:
    data = mi.readline()
mikey=data.strip().split(',')
with open("sarah.txt") as sa:
    data = sa.readline()
sarah=data.strip().split(',')
print(james)
print(type(sarah[0]))
print(sorted(sarah))
"""Hey, it looks like your data values are
not uniform. Is the problem with all those
periods, dashes, and colons?"""

"""Let’s create a function called sanitize(), which takes as input
a string from each of the athlete’s lists. The function then processes
the string to replace any dashes or colons found with a period and
returns the sanitized string. Note: if the string already contains a
period, there’s no need to sanitize it."""

def sanitize(string1):
    if '-' in string1:
        splitter='-'
    elif ':' in string1:
        splitter=':'
    else:
        return(string1)
    (a,b)=string1.split(splitter)
    return(a + '.' +b)
clean_james=[]
clean_julie=[]
clean_mikey=[]
clean_sarah=[]
for each in james:
    clean_james.append(sanitize(each))
for each in julie:
    clean_julie.append(sanitize(each))
for each in mikey:
    clean_mikey.append(sanitize(each))
for each in sarah:
    clean_sarah.append(sanitize(each))
print(sorted(clean_sarah))
"""Removing Duplicates"""
unique_sarah=[]
for each in clean_sarah:
    if each not in unique_sarah:# first2.55 append to unique then again 2.55 come this condition is True and it will not append
        unique_sarah.append(each)
print(sorted(unique_sarah))
print(sorted(unique_sarah[0:3])) #top three athlete
