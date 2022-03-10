import string

file = open("document.txt", encoding="utf8")
  
d = {}
  
for line in file:
    line = line.strip()
    
    line = line.lower()
      
    line = line.translate(line.maketrans("", "", string.punctuation))
 
    words = line.split(" ")
 
    for word in words:
       
        if word in d:
          
            d[word] = d[word] + 1
        else:
          
            d[word] = 1

    
sort_orders = sorted(d.items(), key=lambda x: (-x[1], x[0]))

first_five = list(sort_orders)[:5]

for i in first_five:
    print(i[0], ": ", i[1])


