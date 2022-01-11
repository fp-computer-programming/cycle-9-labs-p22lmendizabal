#author: LM (AMDG) 1/11/22
def add_foods(lst):
    sixth_letter= []
    not_foods= []
    short_foods= []
    for value in (lst):
        try:
            value[5] == sixth_letter.append()
            print("sixth_letter", sixth_letter)
        except IndexError:
            value = not_foods.append()
        except TypeError:
            value = short_foods.append()
    print("sixth_letter:", sixth_letter)

    add_foods(['potatoes', 'salsa', 'cherries', 'banana', 'apple'])
    