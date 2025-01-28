def is_prime_number(num):
    if num <= 1:
        return False

    for divisor in range(2, num):
        if num % divisor == 0:
            return False

    return True


def save_numbers_in_file(numbers):
    txt_file = open('results.txt', 'w')
    txt_file.write('Prime numbers between 1 and 250:\n')
    txt_file.write(', '.join(str(n) for n in numbers))
    txt_file.write('\n')
    txt_file.close()

prime_numbers = []

for number in range(1, 251):
    if is_prime_number(number):
        prime_numbers.append(number)

save_numbers_in_file(prime_numbers)