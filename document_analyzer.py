import string

def document_analyzer():
    file = open("document.txt", encoding="utf8")
   
    for line in file:
        line = line.translate(line.maketrans("", "", string.punctuation))
        words = line.split()
    
    d = {}
    for word in words:
        if word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 1
    
    sort_orders = sorted(d.items(), key=lambda x: (-x[1], x[0]))
    first_five = list(sort_orders)[:5]
    for i in first_five:
        print(f'{i[0]}: {i[1]}')
  

document_analyzer()




