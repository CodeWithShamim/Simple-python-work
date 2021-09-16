lis_t = set([10, 20, 30, 40, 50, 60])
se_t = {40, 50, 60, 70, 80, 90,200}

#add value...
se_t.add(100)

#remobe value..............
se_t.remove(200)

print("Boolean value check : ", 10 in lis_t)
print("Boolean value check : ", 10 not in lis_t)



print( "Common value and uncommon value : ", lis_t | se_t)
print("Common value :", lis_t & se_t)
print("Subtraction value :", lis_t - se_t)
