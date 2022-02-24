from collections import OrderedDict

print("This is a Dict \n")
dict = {}

dict['a'] = 1
dict['b'] = 2
dict['c'] = 3
dict['d'] = 4

dict.pop('c')

dict['e'] = 444

for key, value in dict.items():
    print("key: {} value: {}".format(key, value))

print("\n This is Ordered Dict \n")
ordered_dict = OrderedDict()

ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4

ordered_dict.pop('a')

for key, value in ordered_dict.items():
    print("key: {} value : {}".format(key, value))
