#LIST -- mutable sequence of code
marks=[20,30,40,50,60]
print(marks)
print(f"lenght of list: {len(marks)}")

#index dia access kora jai

marks[3]=55
print(f"after replace: {marks}")

#multiple data type same list e rakha jai

new_list=[3,5,"abc",45.67,'v']
print(type(new_list))

#slicing--- list[str idx(def=0):end idx(def=len of the list)]
print(new_list[0:3])