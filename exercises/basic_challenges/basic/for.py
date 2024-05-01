# c = 0
# for i in range(3):
#     for j in range(3):
#         if i == j:
#             c += 1
# print(c)  # 3
# # What is the output of this code?
# # 3
# # Explanation:

# # The code is counting the number of times i is equal to j. The loop runs 3 times, and in each iteration, i is equal to j once. So, the value of c is incremented by 1 in each iteration. Therefore, the final value of c is 3.
# # The code can be simplified by using a single loop:


a = [1, 3, 5]
b = [1, 4, 6, 1000]
print(a > b)  # False
# Explanation:

# The comparison between two lists is done element-wise. The first elements of both lists are compared. If they are equal, the second elements are compared, and so on.
# If the elements are not equal, the comparison result is determined by the comparison of the elements. In this case, 1 is equal to 1, but 3 is less than 2.
# Therefore, the comparison result is False. The comparison stops at the first unequal element. The length of the lists is not considered in the comparison.
