import re
from Constants import CURRENCY_DETAILS, DEFAULT_CURRENCY

def get_salary(salary):
    max_salary = 0
    cleaned_salary = ""
    for word in salary.split(' '):
        digitMatch = re.search(r"\d", word)
        if digitMatch:
            try:
                k = 1
                if("k" in word):
                    k = 1000
                cleaned_salary = re.sub(r'[^0-9.]|\.(?=.*\.)', '',word)
                max_salary = max(max_salary,float(cleaned_salary)*k)
            except ValueError:
                print("error occured :(") 
    return max_salary                        

def get_total_salary(base_salary,bonus,stock,signing_bonus=""):
    total_salary = get_salary(base_salary) + get_salary(bonus) + get_salary(stock) + get_salary(signing_bonus)
    return total_salary


def get_currency(known_currency,other_currency):
    if(other_currency):
        return (other_currency[:3])
    else:
        return (known_currency[:3])

def get_currency_from_salary(salary):
    for currency_detail in CURRENCY_DETAILS:
        currency_symbol = currency_detail['symbol']
        currency_code = currency_detail['cc']
        if currency_code in salary:
            return currency_code
        elif currency_symbol in salary:
            return currency_code
    return DEFAULT_CURRENCY

def get_city(address):
    return (address.split(',')[0]).split('/')[0].split('')[0]

