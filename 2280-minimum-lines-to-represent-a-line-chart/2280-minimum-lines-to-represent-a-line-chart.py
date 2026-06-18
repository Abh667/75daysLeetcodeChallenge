class Solution:
    def minimumLines(self, stockPrices):
        n = len(stockPrices)

        if n == 1:
            return 0

        stockPrices.sort()

        lines = 1

        prev_dx = stockPrices[1][0] - stockPrices[0][0]
        prev_dy = stockPrices[1][1] - stockPrices[0][1]

        for i in range(2, n):
            dx = stockPrices[i][0] - stockPrices[i - 1][0]
            dy = stockPrices[i][1] - stockPrices[i - 1][1]

            if prev_dy * dx != dy * prev_dx:
                lines += 1

            prev_dx = dx
            prev_dy = dy

        return lines
        