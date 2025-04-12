if __name__ == '__main__':
    scores = []
    record = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.append(score)
        record.append([name,score])
    seted = sorted(set(scores))
    second = seted[1]
    namesec = [name for name, score in record if score == second]
    for name in sorted(namesec):
        print(name)
