# Part of case-study #2: Dumplings
# Developers: Komissarov P., Shevchenko A., Greshnova S., Tropin T.
#

import importlib

languages = {"1": "ru_local", "2": "simalung"}

def select_language():
    '''
    Allows the user to select a language
    '''
    
    print("Выберите язык / Pilih bahasa:")
    print("1 - Русский")
    print("2 - Simalungun")
    
    choice = input("Введите номер (1/2) / Masukkon nomor (1/2): ")
    return languages.get(choice) 

meat_per_mant = 60
dough_per_mant = 40
weight_mant = 100
calories_mant = 266

meat_per_buuza = 30
dough_per_buuza = 15
weight_buuza = 45
calories_buuza = 185

meat_per_dumpling = 1
dough_per_dumpling = 0.6
weight_dumpling = 1.6
calories_dumpling = 4.24

def calculate_dishes(total_meat, total_dough, percentage_manti, percentage_buuzy, serving_size):
    '''
    Function characterizing the resource allocation and calculates the number of dishes, servings and calories per serving
    '''

    meat_manti = total_meat * percentage_manti / 100
    dough_manti = total_dough * percentage_manti / 100

    manti_count = int(min(meat_manti // meat_per_mant, dough_manti // dough_per_mant))

    used_meat_manti = manti_count * meat_per_mant
    used_dough_manti = manti_count * dough_per_mant

    buuzy_meat = total_meat * percentage_buuzy / 100
    buuzy_dough = total_dough * percentage_buuzy / 100

    buuzy_count = int(min(buuzy_meat // meat_per_buuza, buuzy_dough // dough_per_buuza))

    used_meat_buuzy = buuzy_count * meat_per_buuza
    used_dough_buuzy = buuzy_count * dough_per_buuza
    
    remaining_meat = total_meat - used_meat_manti - used_meat_buuzy
    remaining_dough = total_dough - used_dough_manti - used_dough_buuzy

    dumplings_count = int(min(remaining_meat // meat_per_dumpling, remaining_dough // dough_per_dumpling))

    total_dishes = (manti_count +
                    buuzy_count +
                    dumplings_count)

    total_weight = (manti_count * weight_mant +
                    buuzy_count * weight_buuza +
                    dumplings_count * weight_dumpling)

    total_calories = (manti_count * calories_mant +
                      buuzy_count * calories_buuza +
                      dumplings_count * calories_dumpling)

    servings = int(total_weight // serving_size) if serving_size else 0 
    calories_per_serving = total_calories // servings if servings else 0

    return manti_count, buuzy_count, dumplings_count, total_dishes, servings, calories_per_serving

def main():
    '''
    Main function
    :return: None
    '''

    lang_module = select_language()
    lol = importlib.import_module(lang_module)

    print(lol.TASK_CONDITION)
    total_meat = float(input(lol.AMOUNT_MEAT))
    total_dough = float(input(lol.AMOUNT_DOUGH))
    percentage_manti = float(input(lol.PERCENT_MANTI))
    percentage_buuzy = float(input(lol.PERCENT_BUUZY))
    serving_size = float(input(lol.SERVING_SIZE))

    manti_count, buuzy_count, dumplings_count, total_dishes, servings, calories_per_serving = calculate_dishes(total_meat, total_dough, percentage_manti, percentage_buuzy, serving_size)

    print(lol.AMOUNT_MANTI, manti_count)
    print(lol.AMOUNT_BUUZY, buuzy_count)
    print(lol.AMOUNT_DUMPLINGS, dumplings_count)
    print(lol.AMOUNT_DISHES, total_dishes)
    print(lol.AMOUNT_SERVINGS, servings)
    print(lol.AMOUNT_CALORIES, calories_per_serving)

if __name__ == "__main__":
    main()