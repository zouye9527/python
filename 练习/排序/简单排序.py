# ls=[2,5,3,1,6,7,4,9,8,10]
# ls2=[]
# while len(ls)>0:
#     for i in range(len(ls)):
#         if ls[i]==max(ls):
#             n=0
#             ls2.append(max(ls))
#             n=i
#     del ls[n]
# print(ls2)

ls=[2,5,3,1,6,7,4,9,8,10]
ls2=[]
while len(ls)>0:
    for i in ls:
        if i==max(ls):
            ls2.append(max(ls))
            ls.remove(max(ls))
print(ls2)