# -*- coding: utf-8 -*-
from p1_2_1 import PatternCount

def FrequentWords(Text, k):
        FrequentPatterns = set()
        Count = []
        for i in range(len(Text) - k + 1):
            Pattern = Text[i : i + k]
            Count.append(PatternCount(Text, Pattern))
        maxCount = max(Count)
        for i in range(len(Text) - k + 1):
            if Count[i] == maxCount:
                FrequentPatterns.add(Text[i : i + k])
        #remove duplicates from FrequentPatterns
        return FrequentPatterns

if __name__ == "__main__":
    f = open(r"D:\soft\devProjects\bioinfproject\data\dataset_2_9.txt")
    Text = f.readline().strip()
    k = f.readline().strip()
    f.close()
    print len(Text), Text
    print k
    for s in FrequentWords(Text, int(k)):
        print s,