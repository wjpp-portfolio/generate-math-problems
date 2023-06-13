import random

def gen_multiplication_table(calculation_limit, highest_times_table):
    """returns non-duplicating list of products up to the calcuation limit, including all times-tablesup to highest_times_table""" 
    multi_table = []

    for i in range(2, highest_times_table + 1):
        for j in range(1, calculation_limit):
            result = i * j

            if result > calculation_limit or result in multi_table:
                break
            else:
                multi_table.append(result)

    return sorted(multi_table)


def gen_prime_number_list(limit):
    """returns list of prime numbers up to limit"""
    list_of_primes = []

    for candidate_prime in range(3, limit + 1, 2):
        divisors = 0
        for j in range(1, candidate_prime + 1):
            if candidate_prime % j == 0:
                divisors += 1

        if divisors <= 2:
            list_of_primes.append(candidate_prime)
    
    return sorted(list_of_primes)


def generate_composite_number(limit):
    """returns a composite number below limit"""
    candidate = random.randrange(3, limit) # + 1 from limit omitted intentionally to not accidently go over limit should number be prime
    divisors = 0
    for i in range(1, candidate):
        if candidate%i == 0:
            divisors += 1

    if divisors > 2:
        return candidate 
    
    else:
        return candidate + 1
