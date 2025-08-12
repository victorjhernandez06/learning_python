# Creamos una variable que va a pedir el numero

def luhn_check(card_num):

    digits = [int(x) for x in str(card_num)][::-1]

    for i in range(1, len(digits),2):
        digits[i] *=2
        if digits[i] > 9:
            digits[i] -=9

    total_sum  = sum(digits)
    return total_sum / 10

tarjeta = luhn_check(4400663762999293)
print(tarjeta)

tarjeta2 = luhn_check(4031631289432525)
print(tarjeta2)

tarjeta3 = luhn_check(4815820395677576)
print(tarjeta3)