# def check_seq(biglist, smalllist):
#     # checks to see if the elements in small list are in big list
#     # elements must be in order
#     # big list will always be larger than small list
#     len_to_check = len(biglist) - len(smalllist) + 1
#     for bi in range(len_to_check):
#         for si in range(len(smalllist)):
#             print biglist[bi+si], smalllist[si]
#             if biglist[bi+si] == smalllist[si]:
#                 if si == len(smalllist)-1:
#                     return True
#             else:
#                 break
#     return False        
    
#####################################################################

# https://www.hackerrank.com/challenges/two-characters
# def check_two_char(astr):
#     # returns the max len of the final string with alternate 2 characters.
#     # Ex: acbfatbagb returns 6 (ababab)
#     char_count = {}  # {character:count of charater}
#     for char in astr:
#         char_count[char] = char_count.get(char, 0) + 1
#     if len(char_count) < 2:  # checks to see if there is more than 1 char
#         return None
#     counts = []  # stores all counts of existing characters [2,3,4,4]
#     count_char = {}  # {count:[char1,char2]}
#     for char_key in char_count:
#         counts.append(char_count[char_key])
#         count_char[char_count[char_key]] = count_char.get(char_count[char_key], None)
#         if count_char[char_count[char_key]] is None:
#             count_char[char_count[char_key]] = [char_key]
#         else:
#             count_char[char_count[char_key]].append(char_key)
#     counts = list(set(counts))
#     counts.sort(reverse=True)
#     flag = False
#     i = 0
#     ans = []
#     for i in range(len(counts) - 1):
#         if counts[i] - counts[i+1] < 2:
#             possible_chars = []
#             possible_chars.extend(count_char[counts[i]])
#             possible_chars.extend(count_char[counts[i+1]])
#             for i in range(len(possible_chars)-1):
#                 word = get_alternate_str(possible_chars[i], possible_chars[i+1], astr)
#                 if word is not None:
#                     ans.append(len(word))
#                     flag = True
#                     break
#                 else:
#                     continue
#             i += 1
#         else:
#             i += 1
#             continue
#     if flag is False:
#         print 0
#     else:
#         print ans[0]  # Hackerrank wanted a print statement, not return


# def get_alternate_str(char1, char2, aword):
#     # takes 2 characters and arranges them according to their appearance in aword
#     # returns the new arrangement
#     # Ex: (a,b, bcatbgoa) returns "baba"
#     char1 = char1[0]
#     char2 = char2[0]
#     lst_str = ""
#     for khar in aword:
#         if khar == char1 or khar == char2:
#             lst_str = lst_str + khar
#     if is_alternating(lst_str) is True:
#         return lst_str
#     else:
#         return None


# def is_alternating(astr):
#     # takes a string and checks to see if the characters alternate
#     # returns True to False
#     char_1 = [astr[0]]
#     char_2 = [astr[1]]
#     for i in range(2, len(astr)):
#         if i % 2 == 0:
#             char_1.append(astr[i])
#         else:
#             char_2.append(astr[i])
#     if len(set(char_1)) > 1 or len(set(char_2)) > 1:
#         return False
#     else:
#         return True

#####################################################################
# def rotate_matrix(old_matrix):
#     # take a matrix that is n x m and rotates it 90 degrees clockwise
#     # returns the new matrix
#     if old_matrix:
#         n = len(old_matrix)
#         m = len(old_matrix[0])
#         new = [[] for i in range(m)]

#         for k in range(n-1, -1, -1):
#             for j in range(m):
#                 new[j].append(old_matrix[k][j])

#         print new
#     else:
#         print None

# rotate_matrix([[1,2,3],[4,5,6], [7,8,9]])
# rotate_matrix([[1,2,3],[4,5,6]])
# rotate_matrix([[]])
# rotate_matrix([])
