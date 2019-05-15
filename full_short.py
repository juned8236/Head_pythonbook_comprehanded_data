"""programe to take athlete data from txt file and print top three athlete time"""
def get_athlet_data(filename):
    try:
        with open(filename) as f:
            data=f.readline()
        return (data.strip().split(','))
    except IOError:
        print("File error" + str(IOError))
        return None
sarah=get_athlet_data('sarah.txt')
james=get_athlet_data('james.txt')
julie=get_athlet_data('julie.txt')
mikey=get_athlet_data('mikey.txt')

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
print(sorted(set([sanitize(each) for each in james]))[0:3])
print(sorted(set([sanitize(each) for each in julie]))[0:3])
print(sorted(set([sanitize(each) for each in mikey]))[0:3])