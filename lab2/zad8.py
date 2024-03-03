mixed_arr = [2, 5, 'a', 3, 'b', 1, 'f', 'd', 2, 'f', 2]
my_dict = {}

for i in mixed_arr:
    my_dict[i] = mixed_arr.count(i)
    
for key in my_dict.copy():
    if type(key) is not int:
        del(my_dict[key])
        
print(my_dict)