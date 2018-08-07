def soma_matrizes(m1, m2):
    if len(m1) == len(m2):
        res = []
        for i in range(len(m1)):
            row = []
            for j in range(len(m1[0])):
                row.append(m1[i][j] + m2[i][j])
            res.append(row)
        return res
    else:
        return False