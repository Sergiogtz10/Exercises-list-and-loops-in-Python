arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]

#Your code go here:

def sumOdds(items):
    total_odds = 0
    for i in range(len(items)):
        if items[i]%2 != 0:
            total_odds += items[i]
    return total_odds


print(sumOdds(arr))


