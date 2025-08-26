def convert(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s

    rows = [''] * numRows
    cur_row, direction = 0, 1

    for c in s:
        rows[cur_row] += c
        if cur_row == 0:
            direction = 1
        elif cur_row == numRows - 1:
            direction = -1
        cur_row += direction

    return ''.join(rows)
