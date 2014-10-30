from p1_2_2 import FrequentWords
from p1_11 import FasterFrequentCounter
from util import number_to_pattern, pattern_to_number

ffc = FasterFrequentCounter()

def lt_clumps(text, k, L, t):
    patterns = set()
    for i in range(len(text) - L + 1):
        patterns.update(ffc.FasterFrequentWords(text[i : i + L], k, t))
    return patterns

def ClumpFinding(Genome, k, L, t):
    FrequentPatterns = set()
    N = pow(4, k)
    RN = xrange(N)
    Clump = [0] * N
    Text = Genome[:L]
    FrequencyArray = ffc.ComputingFrequencies(Text, k, N)
    for j in RN:
        if FrequencyArray[j] >= t:
            Clump[j] = 1
    for i in range(1, len(Genome) - L + 1):
        FirstPattern = Genome[i - 1: i - 1 + k]
        j = pattern_to_number(FirstPattern)
        FrequencyArray[j] -= 1
        LastPattern = Genome[i + L - k : i + L]
        j = pattern_to_number(LastPattern)
        FrequencyArray[j] += 1
        if FrequencyArray[j] >= t:
            Clump[j] = 1
    for i in RN:
        if Clump[i] == 1:
            FrequentPatterns.add(number_to_pattern(i, k))
    return FrequentPatterns


if __name__ == "__main__":
    '''f = open(r"D:\soft\devProjects\bioinfproject\data\test.txt")
    Text = f.readline().strip()
    f.close()'''
    print ClumpFinding("GCACAAGGCCGACAATAGGACGTAGCCTTGAAGACGACGTAGCGTGGTCGCATAAGTACAGTAGATAGTACCTCCCCCGCGCATCCTATTATTAAGTTAATT", 4, 30, 3)