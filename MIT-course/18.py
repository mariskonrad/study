# Problem Set 2:
# calcular qual é o valor mínimo necessário a ser pago por mês para pagar toda a fatura em 12 meses.
# neste programa não estaremos lidando com uma taxa mínima de pagamento mensal. 
# terá as variáveis balance = o saldo devedor no cartão de crédito e anualInterestRate = taxa de juros anual (em decimal)
# o programa deve printar o menor valor mensal possível para pagar o valor da dívida em 12 meses. Lowest Payment: 180. (e.g.)
# juros compostos em cima do valor que ainda precisa ser pago cada mes.
# o pagamento mensal deve ser múltiplo de 10 e o mesmo em todos os meses.
# é possível que o saldo se torne negativo usando este esquema de pagamento, o que é normal.


balance = 1000
monthlyPayment = 10 
month = 0
annualInterestRate = 0.18 / 12.0
totalPayment = 0

while month < 12:
    unpaidBalance = balance - monthlyPayment
    interest = annualInterestRate * unpaidBalance
    updatedBalance = unpaidBalance + annualInterestRate  * unpaidBalance
    totalPayment += monthlyPayment + annualInterestRate
    month += 1
    if totalPayment > updatedBalance:
            print(monthlyPayment)
    else:
        unpaidBalance = updatedBalance
        monthlyPayment += 10
