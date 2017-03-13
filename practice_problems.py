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

########################################################################

# def merge_sorted_lists(lst1, lst2):
#     # takes 2 sortes lists
#     # returns 1 sorted list
#     new_lst = []
#     i1 = 0
#     i2 = 0
    
#     while i1 < len(lst1) and i2 < len(lst2):
#         if lst1[i1] < lst2[i2]:
#             new_lst.append(lst1[i1])
#             i1 += 1
#         elif lst1[i1] == lst2[i2]:
#             new_lst.append(lst1[i1])
#             new_lst.append(lst2[i2])
#             i1 += 1
#             i2 += 1
#         else:
#             new_lst.append(lst2[i2])
#             i2 += 1

#     if i1 == len(lst1) and i2 < len(lst2):
#         for i in range(i2,len(lst2)):
#             new_lst.append(lst2[i]) 
#     elif i2 == len(lst2) and i1 < len(lst1):
#         for i in range(i1,len(lst1)):
#             new_lst.append(lst1[i])
    
#     return new_lst

# print merge_sorted_lists([1,3,5,9], [2,5,7,20])


########################################################################

# def longest_distance(astr):
#     # takes in a string and returns the longest distance between a repeating char
#     char_dist = {}  # {char: [index at pos1, index at pos2]}

#     for i in range(len(astr)):
#         char = astr[i]
#         char_dist[char] = char_dist.get(char, [i, i])
#         char_dist[char][1] = i

#     longest_distance = 0
#     character = None

#     for char in char_dist:
#         diff = char_dist[char][1] - char_dist[char][0]
#         if diff > longest_distance:
#             longest_distance = diff
#             character = char

#     return character, longest_distance

# print longest_distance("sabybada") #a, 6


##########################################################################
# Min Heaps (same things apply to Max Heaps, just opposite :) )
# practical applications: UBER/Lyft with closed car at the top, games: enemies closest

# Inserting a node into a heap: O(logn)
# when inserting a node into a min heap, it inserts breath first from the left most leaf. It bubbles up.
#      if it is smaller than it's parent: swap

# Deleting from a min heap:
# Swap the peak with the last leaf (breath first). Trim and return it.
# Look at the new peak. If it's larger than it's children, swap with it's smallest one. 
# Keep bubbling down

# A min heap/ binary tree can be represented by an array made with breath first search
# Can keep track of parents and children with indexes: Pi and Ci
# Ex. [4,7,5,9,10,6,8]
#    Pi: 0  Ci: 1,2
#    Pi: 1  Ci: 3,4
#    Pi: 2  Ci: 5,6
#   Relationship:  2n+1 (odd), 2n+2 (even)

# Doing insertion using an array:
#  - Push on the new element 1 onto the array. Ex. [4,7,5,9,10,6,8,1]
#  - The parent of 1 is 9 (index 7 has parent at index 3). 1 < 9 = swap  Ex. [4,7,5,1,10,6,8,9]
#  - The parent of 1 is now 7 (index 3 has parent at index 1). 1 < 7 = swap  Ex. [4,1,5,7,10,6,8,9]
#  - The parent of 1 is now 4 (index 1 has parent at index 0). 1 < 4 = swap  Ex. [1,4,5,7,10,6,8,9]


# Doing deletion using an array:  Ex. [1,4,5,7,10,6,8,9]
#  - Swap the first with last   Ex. [9,4,5,7,10,6,8,1]
#  - Take off the last one. Then swap the first with it's smaller child like above


# class MinHeap():
#     def __init__(self, alist=None):
#         self.alist = alist

#     def swap(self, i1, i2):
#         # given 2 indexes, it swaps the elements in the two indexes
#         self.alist[i1], self.alist[i2] = self.alist[i2], self.alist[i1]

#     def peak(self):
#         # return the topmost node
#         return self.alist[0]

#     def size(self):
#         # returns the length of the storage array
#         return len(self.alist)

#     def insert(self, value):
#         self.alist.append(value)
#         self.bubble_up(self.size() - 1)

#     def bubble_up(self, ci):
#         # given a child index ci, find parent, swap if needed
#         # pi = parent index
#         if ci % 2 == 0:
#             pi = (ci - 2)/2
#         else:
#             pi = (ci - 1)/2

#         while ci > 0 and self.alist[ci] < self.alist[pi]:
#             self.swap(ci, pi)
#             ci = pi
#             if ci % 2 == 0:
#                 pi = (ci - 2)/2
#             else:
#                 pi = (ci - 1)/2

#     def remove_peak(self):
#         self.swap(0, self.size() - 1)
#         minElement = self.alist.pop()
#         self.bubble_down(0)
#         return minElement

#     def bubble_down(self, pi):
#         ci1 = (2 * pi) + 1
#         ci2 = (2 * pi) + 2

#         # make sure the children is there.
#         # Indexes have to be within the len
#         if ci1 >= self.size():
#             return None
#         elif ci2 >= self.size():
#             mci = ci1  # master child index
#         elif self.alist[ci1] < self.alist[ci2]:  # find the smaller child
#             mci = ci1
#         else:
#             mci = ci2
#         while pi < (self.size()-1) and self.alist[pi] > self.alist[mci]:
#             self.swap(pi, mci)
#             pi = mci
#             ci1 = (2 * pi) + 1
#             ci2 = (2 * pi) + 2
#             if ci1 >= self.size():
#                 return None
#             elif ci2 >= self.size():
#                 mci = ci1
#             elif self.alist[ci1] < self.alist[ci2]:
#                 mci = ci1
#             elif self.alist[ci2] < self.alist[ci1]:
#                 mci = ci2

#     def remove(self, val):  # FIXIT!!
#         # remove things in the middle of the min heap
#         # takes in a value, finds the value in the array O(n)
#         # assign it to a min val
#         # bubble it down to remove it
#         if val in self.alist:
#             minVali = self.alist.index(val)
#             self.swap(minVali, self.size()-1)
#             result = self.alist.pop()
#             if minVali < self.size():
#                 self.bubble_down(minVali)
#             return result
#         else:
#             return None


# minheap = MinHeap([4,7,5,9,10,6,8])
# print minheap.alist
# minheap.swap(1,4)
# print minheap.alist
# peak = minheap.peak()
# print minheap.size()
# minheap.remove_peak()
# print minheap.alist
# minheap.insert(3)
# print "inserted", minheap.alist

##########################################################################

# given an unsorted array of unique integers, find the first missing positive integers
# 0 doesn't count as positive
# [-4, 5,1,3,4]  ->  2

# def find_pos(array):
#     i = 0
#     length = len(array)
#     while i < length:
#         if array[i] < 1:
#             array = array[:i] + array[i+1:]
#             length = len(array)
#         i += 1

#     lowest = min(array)
#     highest = max(array)
#     true_len = highest - lowest + 1
#     difference = true_len - len(array)

#     for each in range(difference):
#         array.append(None)

#     # touches each number ONCE to place them in the corresponding index location
#     i = 0
#     while i < true_len:
#         j = i
#         num = array[j]
#         num_i = array[j]-lowest
#         while not is_index(num_i, j) and num is not None: 
#             temp = array[num_i]
#             array[num_i] = num
#             j = num_i
#             num = temp
#         i += 1

#     print array
#     for i in range(len(array)):
#         if (array[i] - lowest) != i:
#             return (i + lowest)

#     return None


# def is_index(num1, num2):
#     if num1 == num2:
#         return True
#     else:
#         return False

# print "finding missing positive"
# print find_pos([-4, 5,1,3,4])

##########################################################################
# scale = {"I": ["I", "X", "C", "M"], "V": ["V", "L", "D"]}
# look_up = {0: "", 1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX"}


# def roman_num(num):
#     # converts digit to roman numeral
#     result = ""
#     i = 0
#     num = str(num)
#     for n in range(len(num)-1, -1, -1):
#         curr = num[n]
#         curr = look_up[int(curr)]
#         for m in range(len(curr)-1, -1, -1):
#             each = curr[m]
#             if each == "X":
#                 each = scale["I"][i+1]
#             elif each == "I":
#                 each = scale["I"][i]
#             elif each == "V":
#                 each = scale["V"][i]
#             result = each + result
#         i += 1

#     return result


# vals = [1, 5, 10, 50, 100, 500, 1000]
# roms = ["I", "V", "X", "L", "C", "D", "M"]

# def roman_num(num):
#     result = ""

#     for i in range (len(vals)-1,-1,-1):
#         while vals[i]<=num:
#             num -= vals[i]
#             result = result + roms[i]
#     for i in range (len(roms)-2,-1,-1):
#         old_t = roms[i]+roms[i]+roms[i]+roms[i]
#         new_t = roms[i]+roms[i+1]
#         result = result.replace(old_t, new_t)
#     for i in range (len(roms)-3,-1,-1):
#         old_t = roms[i+1]+roms[i]+roms[i+1]
#         new_t = roms[i]+roms[i+2]
#         result = result.replace(old_t, new_t)
#     return result



# print roman_num(4)
# print roman_num(8)
# print roman_num(9)
# print roman_num(19)
# print roman_num(49)
# print roman_num(410)
# print roman_num(90)
# print roman_num(900)
# print roman_num(394)
# print roman_num(3999)

###########
# def is_happy(n):
#     visited = set()
#     visited.add(n)
#     while n != 1:
#         curr = 0
#         for num in str(n):
#             curr += int(num) * int(num)
#         if curr in visited:
#             return False
#         else:
#             visited.add(curr)
#             n = curr
            
#     return True

# print is_happy(7)
# print is_happy(25)

###############################################################################
# def isUgly(num):
#     while True:
#         if num == 1:
#             return True
#         elif num % 2 == 0:
#             num = num / 2
#         elif num % 3 == 0:
#             num = num / 3
#         elif num % 5 == 0:
#             num = num / 5
#         else:
#             return False

#     # uglies = [2, 3, 5]
#     #     i = 0
#     #     while i < len(uglies):
#     #         while num % uglies[i] == 0:
#     #             num = num / uglies[i] 
#     #         i += 1 
#     #     if num == 1:
#     #         return True
            
#     #     return False

# print isUgly(25)
# pr
# print isUgly(66)

###############################################################################
# uggos = {1:2}
# def nthUgly(n):
#     i = 0
#     curr = 1
#     while i < n:
#         print uggos[1]
#         if ((i+1) == n) and is_ugly(curr):
#             return curr
#         elif is_ugly(curr):
#             i += 1
#             curr += 1
#         else:
#             curr += 1


# def is_ugly(num):
#     uglies = [2, 3, 5]
#     uggs = len(uglies)
#     i = 0
#     while i < uggs:
#         while num % uglies[i] == 0:
#             num /= uglies[i]
#         i += 1
#     if num == 1:
#         return True
#     return False

# print nthUgly(10)
# print nthUgly(9)
# print nthUgly(11)
# print nthUgly(231)
###############################################################################
# def pascal_triangle2(n):
#     result = [[0,1,0]]
#     i = 0

#     while i < n-1:
#         curr = result[i]
#         new = [0]
#         for pos in range(len(curr)-1):
#             new.append(curr[pos] + curr[pos + 1])
#         new.append(0)
#         result.append(new)
#         i += 1

#     for i in range(len(result)):
#         result[i] = result[i][1:-1]


#     return result

# #######
# def pascal_triangle(n):
#     result = []

#     for i in range(n):
#         if i == 0:
#             curr = []
#         else:
#             curr = result[i-1][:]
#         curr.append(0)
#         new = [1]
#         for pos in range(len(curr)-1):
#             new.append(curr[pos] + curr[pos + 1])
#         result.append(new)


#     return result


# print pascal_triangle(-1)
# print pascal_triangle(0)
# print pascal_triangle(1)
# print pascal_triangle(2)
# print pascal_triangle(3)
# print pascal_triangle(4)
# print pascal_triangle(5)

##############################################################################



# def countPrimes(n):
#     numbers = [None]*(n)
    
#     for i in range(2, n):
#         if numbers[i] is None:
#             numbers[i] = isPrime(i)
#         for m in range(i, n, i):
#             if numbers[m] is None:
#                 if (m) % i == 0:
#                     numbers[m] = False
                    
#     numbers = numbers[2:]
#     result = []
#     for i in range(len(numbers)):
#         if numbers[i] is True:
#             result.append(i+2)
#     print result
#     return sum(numbers)
        
# def isPrime(i):
#     if i <= 1:
#         return False
#     if i == 2 or i == 3:
#         return True
#     for num in range(2, i/2):
#         if i % num == 0:
#             return False
#     return True


# print countPrimes(5)
# print countPrimes(23)
# print countPrimes(200)
# print countPrimes(40000)

##############################################################################
# total Hamming distance


# def total_Ham(arr):
#     bits = {}

#     def get_bits(num):
#         result = ''
#         num2 = num
#         for i in range(30):
#             if num in bits:
#                 extra = len(result)
#                 result = bits[num] + result
#                 result = result[extra:]
#                 break
#             else:
#                 r = num % 2
#                 num /= 2
#                 result = str(r) + result

#         bits[num2] = result
#         return result

#     def get_diff(numA, numB):
#         count = 0
#         for i in range(30):
#             if numA[i] != numB[i]:
#                 count += 1
#         return count

#     for i in arr:
#         if i not in bits:
#             print i
#             bits[i] = get_bits(i)

#     result = 0
#     print bits

#     # fix this O(n^2) loops so that we are looking at each bit individually. 
#     # remember the if we have four 0's and 2 1's, whats the Hamming distance
#     for l in range(len(arr)):
#         for m in range(l, len(arr)):
#             if l != m:
#                 result += get_diff(bits[arr[l]], bits[arr[m]])
#     return result

# print total_Ham([6,1,8,6,8])
##############################################################################
# is leap year
# is divisible by 4. if divisible by 100, not leap year unless also divisible by 400

# def is_leap1(year):
#     leap = False
#     if year % 4 == 0:
#         leap = True
#     if year % 100 == 0:
#         leap = False
#     if year % 400 == 0:
#         leap = True
#     return leap

# def is_leap(year):
#     return ((year%4==0 and year%100!=0) or (year%400==0))

# print is_leap(1995)
# print is_leap(2000)
# print is_leap(1900)
# print is_leap(2004)
# print is_leap(2016)
# print is_leap(1600)
# print is_leap(2008)
# print is_leap(1996)
##############################################################################
# find single non-Duplicate in array

# def singleNonDuplicate1(arr):
#     length = len(arr)
#     mid = length/2
#     if length == 1:
#         return arr[0]

#     while True:
#         length = len(arr)
#         mid = length/2
#         if arr[mid-1] == arr[mid]:
#             if mid == 1:
#                 return arr[mid+1]
#             else:
#                 arr = arr[:mid-1]
#         elif arr[mid] == arr[mid+1]:
#             if mid == 1:
#                 return arr[mid-1]
#             else:
#                 arr = arr[mid+2:]
#         else:
#             return arr[mid]


# def singleNonDuplicate(arr):
#     l = 0
#     r = len(arr)-1

#     while True:
#         m = (r+l)/2
#         if l == m:
#             return arr[m]

#         if r-l == 2:
#             if arr[m-1] == arr[m]:
#                 return arr[m+1]
#             elif arr[m] == arr[m+1]:
#                 return arr[m-1]

#         if arr[m-1] == arr[m]:
#             r = m-2
#         elif arr[m] == arr[m+1]:
#             l = m+2
#         else:
#             return arr[m]



# print singleNonDuplicate([1,1,2,2,3,3,4,5,5])
# print singleNonDuplicate([1,1,2,3,3,4,4,5,5])
# print singleNonDuplicate([1,1,2,3,3,5,5,6,6,7,7,8,8])
##############################################################################
