text = input("Input the string of HTML document: ")

start = text.find('<')
while start != -1:
    end = text.find('>', start + 1)
    tag = text[start:end+1]
    print(tag, end = ' ')
    start = text.find('<', end + 1)