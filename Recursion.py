# def fact(n):
#     if(n == 0 or n == 1):
#         return 1;
#     else:
#         return n*fact(n-1)
    
# print(fact(4));



# def sum(n):
#     if(n == 0):
#         return 0;
#     return n + sum(n-1);

# print(sum(6))



def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx]);
    print_list(list,idx+1);

num = [2, 3, 5, 6, 8];
print_list(num)