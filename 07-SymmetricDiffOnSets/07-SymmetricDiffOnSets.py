m_count = input() # Nubmer of elements in the first set
set_m =  set() 
m = input() # Elements of the first set space seperated 
mlist =  m.split() 
mlist_new = list(map (int , mlist))
for i in range(int(m_count)):
    set_m.add(mlist_new[i])

n_count = input() # Number of elements in the second set
set_n =  set()
n = input() # Elements of the first set space seperated
nlist =  n.split()
nlist_new = list(map (int , nlist))
for i in range(int(n_count)):
    set_n.add(nlist_new[i])
    
l_m  = list(set_n.difference(set_n))
l_n = list(set_n.difference(set_n))
l_m.extend(l_n)
l_m.sort()
for i in range (len(l_m)): 
    print(l_m[i])
