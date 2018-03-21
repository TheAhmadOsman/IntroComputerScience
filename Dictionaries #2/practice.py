#Englidh to Spanish
translate = {'red':'7amra', 'blue':'Zarqa', 'yellow':'Safra', 'white':'Beda'}
print("Red in Arabic is", translate['red'])
print(translate)

print()
myD = {'firstname':'Ahmad', 'lastname':'Osman', 'age':21}
print(myD)
print(myD['firstname'], myD['lastname'], myD['age'])
myD['age'] += 5
print(myD['age'])

print()
newD = myD
newD['lastname'] = 'Magdy'
print(myD, hex(id(myD)))
print(newD, hex(id(newD)))

print()
#To keep the original dictionary - make a copy
aCopy = myD.copy()
anotherCopy = dict(myD)

print(aCopy, hex(id(aCopy)))
print(anotherCopy, hex(id(anotherCopy)))

print()
myD['lastname'] = 'Osman'
print(myD, hex(id(myD)))
print(aCopy, hex(id(aCopy)))
print()

#####################################
#phoneNum{''}

#######################
band = {6:'Six', 'instrument':'Trombone', 7:'seventy'}

#Print out ---- senty-six trombones
print(band[7].capitalize() + '-' + band[6], band['instrument'])

testScores = {'Ethan' : [70, 75, 78]}
print(sum(testScores['Ethan'])/len(testScores['Ethan']))