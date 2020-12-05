# Title -> Alphacode
# Description -> spoj.com/problems/ACODE/en/

word = raw_input()
while (word != '0'):
    encryption = map(int, list(word))
    results = [1]

    aux = int(''.join(map(str, encryption[:2])))
    aux_value = 2 if aux <= 26 and aux >= 10 else 1

    if len(encryption) >= 2 and encryption[1] == 0:
        results[0] = 0
        aux_value = 1

    if len(encryption) > 2 and encryption[2] == 0:
        aux_value = 1

    results.append(aux_value)

    for i in range(2, len(encryption)):
        value = (encryption[i - 1] * 10) + encryption[i]
        following = ''.join(map(str, encryption[i: i + 2]))

        if encryption[i] == 0:
            results.append(results[i - 1])
            results[i - 2] = 0
        elif value <= 26 and value >= 10 and not following in ['10', '20']:
            results.append(results[i - 1] + results[i - 2])
        else:
            results.append(results[i - 1])

    print(results[len(results) - 1])
    word = raw_input()
