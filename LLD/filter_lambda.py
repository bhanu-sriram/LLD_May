from traceback import print_tb

mul = lambda x,y: x*y
print(mul(2,3))

lambda x : 'even' if x%2==0 else 'odd'

sqaure = lambda x:x*x


listele = [1,2,3,4,5]
for i in listele:
    print(sqaure(i))

result = list(map(lambda x:x*x,listele))
print(result)

stringlist = ["naman","karan","abc"]
newfunc = list(map(lambda x: "Mr."+str(x),stringlist))
print(newfunc)

is_prime = lambda x: 'prime' if x

maxele = reduce(lambda x,y: max(x,y),listele)
print(maxele)