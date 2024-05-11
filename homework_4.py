immutable_var=(1, 2.5, 'apple')
print(immutable_var)
#immutable_var[0]= 5 -объект 'tuple' не поддерживает назначение элементов
#immutable_var.append(orange)- объект 'tuple' не имеет атрибута 'append'
mutable_list= [3,5.5,'orange']
print(mutable_list)
mutable_list[1]= "five point five"
mutable_list.append('red')
print(mutable_list)