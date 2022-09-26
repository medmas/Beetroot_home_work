# i = tuple(range(1, 11))
# new_list = [i, tuple(j**2 for j in i)]
# print(new_list)


stat_one = [i for i in range(1, 11)]
stat_two = [j ** 2 for j in stat_one]

new_list = [(i, j) for j, i in zip(stat_one, stat_two)]
print(new_list)

# i = tuple(range(1, 11))
# j = tuple(j**2 for j in i)
# new_list = [i, j]
# print(new_list)