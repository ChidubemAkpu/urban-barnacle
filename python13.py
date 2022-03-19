#Collatz 3n + 1 sequence
sequence = int(input("What is the first term? "))

collatz_container = [sequence]
while sequence > 1:
    
    if sequence % 2 == 0:
        sequence = sequence // 2
        collatz_container.append(sequence)
    else:
        sequence = 3 * sequence + 1
        collatz_container.append(sequence)

print(collatz_container)




    
