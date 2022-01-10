acronyms = ['LOL', 'IDK', 'SMH', 'TBH']

acronyms.append('BFN')
acronyms.append('IMHO')
print(acronyms)
word = 'BFN'
if word in acronyms:
    print( word +"" + 'Exists in List')
else:
    print ( word +"" +  'Does NOT Exist in List')
acronyms.remove('TBH')
print(acronyms)

for acronym in acronyms:
    print(acronym)

