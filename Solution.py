

# 1. Написать функцию, которая возвращает максимальную прибыль от одной сделки
# с одной акцией (сначала покупка, потом продажа). Исходные данные — массив
# вчерашних котировок stock_prices_yesterday с ценами акций.
#
# Информация о массиве:
#
#     Индекс равен количеству минут с начала торговой сессии (9:30 утра).
#     Значение в массиве равно стоимости акции в это время.
#
# Например: если акция в 10:00 утра стоила 20 долларов, то
# stock_prices_yesterday[30] = 20.
#
# Допустим, имеем некоторые условия:
# stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
#
# profit = get_max_profit(stock_prices_yesterday)
# вернет 6 (купили за 5, продали за 11)

# динамическое программирование:
# состояние(что храним в дп) -> база -> формулы перехода -> порядок обхода -> ответ

# stock_prices_yesterday = [10, 7, 5, 8, 11, 9] -> 6
# stock_prices_yesterday = [1, 3, 5, 8, 11, 20] -> 19
# stock_prices_yesterday = [1] -> 0
# stock_prices_yesterday = [2,  2, 2, 2,  2, 2] -> 0

class Solution:
    def get_max_profit(self, stock_prices_yesterday: [int]) -> int:

        if len(stock_prices_yesterday) < 2:
            return 0

        minPriceInPast = stock_prices_yesterday[0]
        Profit = 0
        for price in stock_prices_yesterday:

            if price < minPriceInPast:
                minPriceInPast = price

            if price - minPriceInPast > Profit:
                Profit = price - minPriceInPast

        return Profit


x = Solution()

stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
print(stock_prices_yesterday, '->', x.get_max_profit(stock_prices_yesterday))

stock_prices_yesterday = [1, 3, 5, 8, 11, 20]
print(stock_prices_yesterday, '->', x.get_max_profit(stock_prices_yesterday))

stock_prices_yesterday = [2, 2, 2, 2, 2, 2]
print(stock_prices_yesterday, '->', x.get_max_profit(stock_prices_yesterday))

stock_prices_yesterday = [1]
print(stock_prices_yesterday, '->', x.get_max_profit(stock_prices_yesterday))

stock_prices_yesterday = []
print(stock_prices_yesterday, '->', x.get_max_profit(stock_prices_yesterday))