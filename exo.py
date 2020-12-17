from random import randint

# # 1
# def calculate_average(seq):
#     calcultate = 0
#     for number in seq:
#         calcultate += number

#     return calcultate / len(seq)

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

# print(get_last_index((4, 9, 2, 6, 3, 2, 1), 3))


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
#         print(number)
#         result.append(number * k)

#     return result

# print(linear_mut([12, 4, 3, 7, 11, 9, 17, 16, 21, 8], 1.5))


# #8
# def permutation(seq, index_a, index_b):
#         number_a = seq[index_a]
#         number_b = seq[index_b]
#         seq[index_a] = number_b
#         seq[index_b] = number_a

#         return seq
    
# print(permutation([12, 4, 3, 7, 11], 1, 7))


# ## Unefficient and overly complicated but it works.
#9
# def pattern_seq(pattern, values):

#     result = []

#     for index in range(len(values)):
#         result += (pattern[index] * [values[index]])

#     return result

# print(pattern_seq((4, 2, 3), ('apple', 'pear', 'cherry')))


# # 10
# def rand_seq(a, b, n):
#     result = []
#     for i in range(n):
#         result.append(randint(a, b))

#     return result


# print(rand_seq(2, 600, 20))

# #11
# def reject_above(seq, f):
#     result = []
#     for number in seq:
#         if number <= f:
#             result.append(number)

#     return result

# print(reject_above((8, 5, 6, 2, 4, 6, 7, 9, 10, 11, 12, 23), 8))

# #12
# def reject_out_of(seq, bottom, top):
#     result = []
#     for number in seq:
#         if number >= bottom and number <= top:
#             result.append(number)

#     return result

# print(reject_out_of((8, 5, 6, 2, 4, 6, 7, 9, 10, 11, 12, 23), 9, 23))

#13
# def reject_duplicate_value(seq):
#     result = []
    
#     for element in seq:
#         is_in_sequence = False
#         for value in result:
#             if element == value:
#                 is_in_sequence = True

#         if is_in_sequence == False:         
#             result.append(element)

#     return result


# print(reject_duplicate_value((1, 2 , 7, 2, 4, 1, 5)))

#14
def merge(seq1, seq2):
    sequences = seq1 + seq2
    result = []

    for number in sequences:
        

print(merge((8, 3 , 7), (2, 3, 5, 9)))
