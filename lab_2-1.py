#author: LM (AMDG) 1/10/22

def double_stuff(lst):
    for index, value in enumerate(lst):
        lst[index] = 2 * value
    return lst
        
print(double_stuff([10, 5, 1]) == ([20, 10, 2]))
print(double_stuff(["a", "b", "c"]) == (['aa', 'bb', 'cc']))
print(double_stuff([10.2, "a", 1]) == ([20.4, "aa", 2]))