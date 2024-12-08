word = input()


word = word.replace('c=','C')
word = word.replace('c-','C')
word = word.replace('dz=','D')
word = word.replace('d-','D')
word = word.replace('lj','L')
word = word.replace('nj','N')
word = word.replace('s=','S')
word = word.replace('z=','Z')

print(len(word))