import re

with open("input.txt", "r") as request, open("answer1.txt", "a") as answer:
    tests = int(request.readline())
    for test in range(tests):
        dna = request.readline().strip()
        pattern = request.readline().strip()
        pointer = 0
        for i in range(len(re.findall(pattern, dna))):
            pointer = dna.find(pattern, pointer) + 1
            answer.write(str(pointer) + " ")
        answer.write("\n")
