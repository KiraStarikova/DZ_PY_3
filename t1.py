# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

elementsList = [1, 3.5, 'i', 8, 'g', 45, 'i', 1, 'k', 't', 3.5, 8, 'g', 4]
kit = set()
for x in elementsList:
    if elementsList.count(x) > 1 and x not in kit:
        kit.add(x)
print(elementsList)
print(kit)

#y =  ([i for  i in elementsList if elementsList.count(i) > 1])
#print(list (set ( ( [i for  i in elementsList if elementsList.count(i) > 1]))))
