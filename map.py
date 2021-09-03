import sys
def map():
    for csv_line in sys.stdin: 
        csv_line = csv_line.strip()
        record = csv_line.split(',')
        teleplay_id = str(record[1])
        rating = float(record[2])
        if(rating != -1):
            print(",".join([teleplay_id, str(rating)]))


if __name__ == "__main__":
    map()
