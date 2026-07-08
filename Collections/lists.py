Student_marks =[70, 80, 95]
total = sum(Student_marks)
average = total / sum(Student_marks)
print("average marks :", average)

list = [50, 60, 15, 17, 20, 1, 24, 70, 80]
list.append(15)          #append
print("append_list is : ", list)
list.extend([74])     #extend
print("extend_list is :", list)
list.insert(0, 22)   #insert
print("insert_list is :" , list)
list.remove(70)    #remove
print("remove_list is : ", list)
list.pop(2)  #pop
print("pop_list is : ", list)
print("index_list is : ", list.index(15)) #index
print("count_list is : ", list.count(80)) #count
list.sort()        #sort
print("sort_list is :", list)
copy_list = list.copy()    #copy
print("copy_list is : ", copy_list)
list.reverse()  #reverse
print("reverse_list is :", list)
list.clear()    #clear
print("clear_list is :", list)


# create & read a tuple
colors = ("Red", "Blue", "Black", "White")
print("Example of tuple Color :",colors.count('Red'))
print("Example of tuple Color :",colors.index('White'))
