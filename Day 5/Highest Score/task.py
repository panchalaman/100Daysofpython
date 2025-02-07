student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
max_score = 0
for num in student_scores:
    if num > max_score:
        max_score = num
print(max_score)

my_list = [1, 2, 3, 4, 5]
index = 0
while index < len(my_list):
    element = my_list[index]
    print(element)
    index += 1