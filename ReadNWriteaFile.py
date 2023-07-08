with open('text.txt', 'r') as reader:
    con = reader.readlines()
    #reversed(con)


with open('text.txt', 'w') as writer:
    for line in reversed(con):
        writer.write(line)

