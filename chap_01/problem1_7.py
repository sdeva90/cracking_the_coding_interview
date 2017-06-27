def rotate_matrix(matrix):
    if not matrix or len(matrix) != len(matrix[0]):
        return False

    n = len(matrix)
    for layer in range(n // 2):
        left, right = layer, n - layer - 1
        for i in range(left, right):

            # top = matrix[layer][i]
            # right = matrix[i][- layer - 1]
            # bottom = matrix[-layer - 1][-i - 1]
            # left = matrix[-i - 1][layer]

            (matrix[layer][i],
             matrix[i][- layer - 1],
             matrix[-layer - 1][-i - 1],
             matrix[-i - 1][layer]) = (
                matrix[-i - 1][layer],
                matrix[layer][i],
                matrix[i][- layer - 1],
                matrix[-layer - 1][-i - 1],
            )

    return matrix

if __name__ == "__main__":
    matrix = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]
    ]
    import pprint
    pprint.pprint(matrix)
    print('')
    pprint.pprint(rotate_matrix(matrix))
