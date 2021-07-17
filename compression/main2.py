dna = input()
score = 1
z = 0
while z + 1 < len(dna):
    if dna[z] == dna[z + 1]:
        score += 1
    else:
        if score > 1:
            print(dna[z] + str(score), end='')
        else:
            print(dna[z], end='')
        score = 1
    z += 1
if score > 1:
    print(dna[z] + str(score))
else:
    print(dna[z])