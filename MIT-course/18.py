# Problem Set 2:
# calcular qual é o valor mínimo necessário a ser pago por mês para pagar toda a fatura em 12 meses.
# neste programa não estaremos lidando com uma taxa mínima de pagamento mensal.
# terá as variáveis balance = o saldo devedor no cartão de crédito e anualInterestRate = taxa de juros anual (em decimal)
# o programa deve printar o menor valor mensal possível para pagar o valor da dívida em 12 meses. Lowest Payment: 180. (e.g.)
# juros compostos em cima do valor que ainda precisa ser pago cada mes.
# o pagamento mensal deve ser múltiplo de 10 e o mesmo em todos os meses.
# é possível que o saldo se torne negativo usando este esquema de pagamento, o que é normal.

# unpaid balance is the balance minus the minimum fixed monthly payment
# interest is the unpaid balance times annual interest rate divided by 12
# balance is unpaid balance plus the interest

balance = 3926
annualInterestRate = 0.2

minimumMonthlyPayment = 10
monthlyInterestRate = annualInterestRate / 12.0

while True:
    month = 0
    unpaidBalance = balance
    while month < 12 and unpaidBalance > 0:
        unpaidBalance -= minimumMonthlyPayment
        interest = monthlyInterestRate * unpaidBalance
        unpaidBalance += interest
        month += 1

    if unpaidBalance <= 0:
        print(round(minimumMonthlyPayment, 2))
        break
    else:
        minimumMonthlyPayment += 10



