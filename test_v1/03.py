def solution(N, number):
    S = [{N}]
    # print(S)
    for a in range(2, 9):
        list = [int(str(N) * a)]
        # print(a, ', ', list)
        for b in range(0, int(a/2)):
            # print(a, ', ', a/2, ', ', b, '/')
            for c in S[b]:
                print(b, ', ', c)
                for d in S[a - b - 2]:
                    list.append(c + d)
                    list.append(c - d)
                    list.append(d - c)
                    list.append(c * d)
                    # print("list:", list)

                    if c != 0:
                        list.append(d // c)
                    if d != 0:
                        list.append(c // d)

        if number in set(list):
            return a

        S.append(list)

    return -1

print(solution(5, 12))