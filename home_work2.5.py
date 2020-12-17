rating = [7, 5, 3, 3, 2]


n = int(input('Введите новый элемент рейтинга: '))
for i in range(0, len(rating)):
    if n >= max(rating):
        rating.insert(0,n)
        break
    elif n < min(rating):
        rating.append(n)
        break
    elif n == rating[i]:
        rating.insert(i,n)
        break
    elif rating[i-1] > n > rating[i]:
        rating.insert(i,n)
        break
print(rating)



