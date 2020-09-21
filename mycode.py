import array as arr

a=arr.array('i',[2,24,78,99])

print (sorted(set(a))[-2])


h_letters=[]

for letter in 'human':
    h_letters.append(letter)


my_list=[20,25,142,143,57690,5489,2450]

even_no=[x for x in my_list if x%2!=0]
print(even_no)
print(h_letters)
