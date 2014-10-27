# -*- coding: utf-8 -*-

def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text) - len(Pattern) + 1):
        if Text[i : i + len(Pattern)] == Pattern:
            count += 1
    return count

if __name__ == "__main__":
    f = open(r"D:\soft\devProjects\bioinfproject\data\dataset_2_6.txt")
    Text = f.readline().strip()
    Pattern = f.readline().strip()
    f.close()
    print len(Text), Text
    print Pattern
    print PatternCount(Text, Pattern)