with open("james.txt") as jaf:#Open the file.
    data=jaf.readline()#Read the line of data.
james=data.split(',') #split=Convert the data to a list.
with open("julie.txt") as ju:
    data = ju.readline()
julie=data.strip().split(',')
with open("mikey.txt") as mi:
    data = mi.readline()
mikey=data.strip().split(',')
with open("sarah.txt") as sa:
    data = sa.readline()
sarah=data.strip().split(',')
def sanitize(string1):
    if '-' in string1:
        splitter='-'
    elif ':' in string1:
        splitter=':'
    else:
        return(string1)
    (a,b)=string1.split(splitter)
    return(a + '.' +b)
print(sorted(set([sanitize(each) for each in sarah]))[0:3])