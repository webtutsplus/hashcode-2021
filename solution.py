M, T2, T3, T4 = map(int, input().split())

ings = []
for _ in range(M):
    ing = input().split()
    ings.append(ing[1:])

# print(T2, T3, T4)
# for ing in ings:
#     print(ing)


'''
2 
2 1 4 
3 0 2 3

2 
2 0 1 
3 2 3 4
'''

ans = []

# max((M/2), T2)
# N2, N3, N4 are number of team with 2, 3, 4 people respectibvely who gets the pizza
N2 = min(M//2, T2)
N3 = 0
N4 = 0
M -= N2*2

if M > 0:
    N3 = min(M//3, T3)

    M -= N3*3

    if M > 0:
        N4 = min(M//4, T4)


total_pizza = N2 + N3 + N4
print(total_pizza)

ind = 0

def print_list(lis):
    for l in lis:
        print(l, end =" ")
    print("")

if N2 > 0:
    for n in range(N2):
        list = [2]
        for i in range(ind , ind + 2):
            list.append(i)
        ind += 2
        print_list(list)

if N3 > 0:
    for n in range(N3):
        list = [3]
        for i in range(ind , ind + 3):
            list.append(i)
        ind += 3
        print_list(list)

if N4 > 0:
    for n in range(N4):
        list = [4]
        for i in range(ind , ind + 4):
            list.append(i)
        ind += 4
        print_list(list)



# if N3 > 0:
#     list = [3]
#     for i in range(ind , ind + N3):
#         list.append(i)
#     ind += N2
#     print(list)
#
# if N2 > 0:
#     list = [2]
#     for i in range(ind , ind + N2):
#         list.append(i)
#     ind += N2
#     print(list)







