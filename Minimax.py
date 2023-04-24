import  math

def minimax(cd, node, maxtd, score, td):
    if cd == td:
        return score[node]

    if maxtd:
        return max(minimax(cd +1, node*2, False, score, td), minimax(cd+1, node * 2+1, False, score, td))

    else:
        return min (minimax(cd+1, node*2, True, score,td), minimax(cd+1, node*2+1, True, score, td))


score = []
n = int(input("Number of leaf: "))
for i in range(n):
    l = int(input('Enter leaf: '))
    score.append(l)

cd = int(input("Enter current depth: "))

td = math.log(len(score),2)

node = int(input("Enter start node: "))

print(minimax(cd, node, True, score, td))
