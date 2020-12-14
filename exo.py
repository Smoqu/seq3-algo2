# # 1
# calculate_average = lambda seq : sum(seq) / len(seq)
# print(calculate_average((7,8,7.5,10,9)))


# # 2
# def get_min(seq):
#     lowest = 20000000
#     for item in seq:
#         if lowest > item:
#             lowest = item

#     return lowest

# print(get_min((10,8,7,10,9)))


# # 3
# def get_max(seq):
#     highest = 0
#     for item in seq:
#         if item > highest:
#             highest = item

#     return highest

# print(get_max((7,8,7.5,10,9)))

# ## Probably a better way
# # 4
# def get_last_index(seq, seek):
#     results = []
#     for index in range(len(seq)):
#         if seek == seq[index]:
#             results.append((seq[index], index))
            
#     if len(results) == 0:
#         return (False, -1)
#     else:
#         return (True, results[-1][1])

# print(get_last_index((4, 9, 2, 6, 3, 2, 1), 18))


# ## Probably a better way
# # 5
# def get_last_index(seq, seek):
#     results = []
#     for index in range(len(seq)):
#         if seek == seq[index]:
#             results.append((seq[index], index))
            
#     if len(results) == 0:
#         return (False, -1)
#     else:
#         return (True, results[0][1])

# print(get_last_index((4, 9, 2, 6, 3, 2, 1), 2))

# # 6
# def value_count(seq, seek):
#     count = 0
#     for number in seq:
#         if number == seek:
#             count+=1
    
#     return count


# print(value_count([12, 4, 3, 7, 11, 9, 4, 5, 4, 8], 4))

# # 7
# def linear_mut(seq, k):
#     result = []
#     for number in seq:
#         result.append(number * k)

#     return result

# print(linear_mut([12, 4, 3, 7, 11, 9, 17, 16, 21, 8], 1.5))


# #8
# def permutation(seq, index_a, index_b):

#     try:
#         number_a = seq[index_a]
#         number_b = seq[index_b]
#         seq[index_a] = number_b
#         seq[index_b] = number_a

#         return seq

#     except:
#         return -1
    
# print(permutation([12, 4, 3, 7, 11], 1, 7))


# ## Unefficient and overly complicated but it works.
# #9
# def pattern_seq(pattern, values):
#     ephe = []
#     result = []
#     for index in range(len(pattern)):
#         test = str(f"{pattern[index] * (values[index] + ' ')}").split(' ')
#         test.pop(-1)
#         ephe.append(test)

#     for item in ephe:
#         for item2 in item:
#             result.append(item2)

#     return result

# print(pattern_seq((4, 2, 3), ('apple', 'pear', 'cherry')))


# 10
# def rand_seq(a, b, n):
