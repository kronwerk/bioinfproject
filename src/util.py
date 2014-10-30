from consts import P_TO_N4
from consts import N_TO_P4
from consts import BASE4

def hamming(s1, s2):
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1
    return count

def pattern_to_number(pattern):
    if not pattern:
        return 0
    return pattern_to_number(pattern[:-1]) * BASE4 + P_TO_N4[pattern[-1]]

def number_to_pattern(number, k):
    if k < 1:
        return ''
    return "".join([number_to_pattern(number / BASE4, k-1), N_TO_P4[number % BASE4]])

def count_mismatched(Text, Pattern, d = 0):
    count = 0
    for i in range(len(Text) - len(Pattern) + 1):
        if hamming(Text[i : i + len(Pattern)], Pattern) <= d:
            count += 1
    return count

if __name__ == "__main__":
    print hamming("CTACAGCAATACGATCATATGCGGATCCGCAGTGGCCGGTAGACACACGT", "CTACCCCGCTGCTCAATGACCGGGACTAAAGAGGCGAAGATTATGGTGTG")
    print count_mismatched("CATGCCATTCGCATTGTCCCAGTGA", "CCC", 2)