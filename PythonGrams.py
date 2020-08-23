from textblob import TextBlob
import io
import csv
import re
from sklearn.metrics import accuracy_score

algorithm = []
answer = []

with open('C:/Users/seanw/Downloads/training_data_debug.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)

    for line in csv_reader:
        at = ""
        for x in re.findall(r'[@]\w+', line[2]):
            at += x
        
        polarity = TextBlob(line[2].replace(at, '')).sentiment.polarity

        if polarity > 0:
            polarity = 1
        else:
            polarity = 0

        algorithm.append(polarity)

with open('C:/Users/seanw/Downloads/training_data_debug.csv') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)

    for line in csv_reader:
        answer.append(int(line[3]))

print("%" + str(accuracy_score(algorithm, answer) * 100))