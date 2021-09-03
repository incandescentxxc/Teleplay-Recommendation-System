import sys

def reduce():
    ratings_list = []
    lastKey = False
    for line in sys.stdin:
        line = line.strip()
        record = line.split(",")
        curKey = str(record[0])
        rating = float(record[1])
        if lastKey and curKey != lastKey:
            print(lastKey, sum(ratings_list)/len(ratings_list))
            lastKey = curKey
            ratings_list = [rating]
        else:
            lastKey = curKey
            ratings_list.append(rating)
    if lastKey:
        print(lastKey, sum(ratings_list)/len(ratings_list))




if __name__ == "__main__":
    reduce()