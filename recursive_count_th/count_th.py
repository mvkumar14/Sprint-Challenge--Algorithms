'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word):
    count = 0
    if len(word) < 2:
        return 0
    if word[0:2] == 'th':
        count += 1
    count += count_th(word[1:])
    return count

# Below is a try at a different implimentation
# 1) I'm not sure its actually faster
# 2) it fails because of where you cut the array
# somtimes you cut a th and don't count it.

# def count_th(word):
#     if len(word) <= 2:
#         if word == 'th':
#             return 1
#         else:
#             return 0
#     half = len(word)//2
#     half_shift = half + 1
#     part1 = word[0:half]
#     part2 = word[half:]
#     count = 0 
#     my_list = [part1,part2]
#     for i in my_list:
#         if type(i) == str:
#             count += count_th(i)
#     return count

#     # divide the word along the half line
#     # and along the half + 1 line
#     # divide until you have two letter segments
#     # if that two letter segment is "th" then return 1
#     # if it isn't th return 0

print(count_th('abcthxyz'))
