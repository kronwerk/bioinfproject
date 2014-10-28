from consts import PAIRS

def reverse_complement(text):
    out = []
    for s in text:
        out.append(PAIRS[s])
    out.reverse()
    return "".join(out)

if __name__ == "__main__":
    f = open(r"D:\soft\devProjects\bioinfproject\data\dataset_3_2.txt")
    Text = f.readline().strip()
    f.close()
    print reverse_complement(Text)