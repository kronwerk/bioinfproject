# -*- coding: utf-8 -*-

def pattern_pos(Text, Pattern):
    positions = []
    for i in range(len(Text) - len(Pattern) + 1):
        if Text[i : i + len(Pattern)] == Pattern:
            positions.append(i)
    return positions

if __name__ == "__main__":
    # f = open(r"D:\soft\devProjects\bioinfproject\data\dataset_3_5.txt")
    f = open(r"D:\soft\devProjects\bioinfproject\data\test.txt")
    Pattern = f.readline().strip()
    Text = f.readline().strip()
    f.close()
    for p in pattern_pos(Text, Pattern):
        print p,