scores = [('English', 100), ('Science', 90), ('Maths', 80)]
sort_scores = sorted(scores, key = lambda t:(-t[1], t[0]))
print(sort_scores)