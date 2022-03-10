import string

file = open("document.txt", encoding="utf8")
  
d = {}
  
for line in file:
    line = line.strip()
    # Remove the punctuation marks from the line
    line = line.translate(line.maketrans("", "", string.punctuation))
    # Split the line into words
    words = line.split(" ")
    # Iterate over each word in line
    for word in words:
        # Check if the word is already in dictionary
        if word in d:
            # Increment count of word by 1
            d[word] = d[word] + 1
        else:
            # Add the word to dictionary with count 1
            d[word] = 1

    
sort_orders = sorted(d.items(), key=lambda x: (-x[1], x[0]))

first_five = list(sort_orders)[:5]

for i in first_five:
    print(i[0], ": ", i[1])


