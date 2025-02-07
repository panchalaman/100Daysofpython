def calculate_love_score(name1, name2):
    true = ['t', 'r', 'u', 'e']
    love = ['l','o','v', 'e']
    true1=0  # Initialize true1
    love1 = 0  # Initialize love1
    total_name = name1 + name2
    for letter in total_name:
        if letter in true:
            true1 += 1
    for letter in total_name:
        if letter in love:
            love1 += 1  # Increment love1 by 1
    print(f"Total in True = {true1}")
    print(f"Total in love = {love1}")
    print(true1 + love1)

calculate_love_score("aman","love")