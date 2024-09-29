def total_investment(n):
    """用于计算一共投资股票的总额"""
    if n <= 12:
        count = 0.5 * (n + n * n)
    else:
        year = n // 12
        month = n % 12
        count = year*78+0.5*(year*year-year)*12+(1+year)*month+0.5*(month*month-month)
    return count


n = int(input('请输入要投资股票持续的月份：'))
print(f'一共投资了{total_investment(n)}万元的股票')
