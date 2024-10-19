- Dictionary
- Key & Value
- dict_name = {key:value}
```
phone = {'Ram':1234, 'Shyam':3456,'Mohan':111}
```
- Dictionaries are ordered from python 3.7
- key are immutable but values are mutable
- No error will be there but he last value assign to
- same key will be considered.
```
phone = {'Ram':1234, 'Shyam':3456,'Mohan':111,'Ram':1321}

phone = {
    'Ram': 'abd',
    'Shyam':3456,
    'Mohan':111,
    'Ram':1321}
```
#print(phone)

#access particular key
#print(phone['Ram'])

#creating dictionary object with dict function
phone_no=dict({
    'Ram': 1234,
    'Shyam': 3456,
    'Mohan': 8976
})
#print(phone_no)

#Updating the value of the dictionary
phone_no['Shyam']= 4212
#print(phone_no)

#we can add list of values
phone_no['Chakra'] = {121,1312,32}
#print(phone_no)
#Print more then 1 key
phone_no['Shyam']={'Shyam_home': 43224,'Shyam_work': 4444}
print(phone_no['Shyam']['Shyam_work'])

#Using get method to find the values of the key
print(phone_no.get('ram'))
#If incorrect value is passed to get method it will return error
#if get method is not used, it will throw key error

data= {1:'Jenny',
       2:'Ram',
       0: 'Mohan'}
print(data[0]) #this is not index, it will print the key

#To delete a key from dictionary
print(phone_no)
del phone_no['Shyam']
#we can also use pop and it will return the value
#print(phone_no.pop('Shyam'))
#to delete last item use popitem
#print(phone_no.popitem()), it return both key and value
print(phone_no)
#to clear the dict object
#print(phone_no.clear())
#to get keys and values
print(phone_no.keys())
print(phone_no.values())
#to print list of all items in the form of items
#print(phone_no.items())
#it will print a list with tuples inside
#a = phone_no.items()
#print(a)
#Below will only print keys
for i in phone_no:
    print(i)
#below will print keys and values
#for i in phone_no:
#    print(i)
#    print(phone_no[i])

#Below will print keys and values as a pair
for i in phone_no.items():
    print(i)
    break

#to copy dictionary
phone_no2 = phone_no.copy()
#to find length
print(len(phone_no2))
```
