import nltk
sent="hi there i am charan from cse charan is a good boy charan is lazy lazy in the sense he doesnot do home work her sleeps all the day he is fucking grazy"
tokens=nltk.word_tokenize(sent)
from nltk.corpus import stopwords
w=[]
l=stopwords.words()
for i in tokens:
    if(i not in l):
        w.append(i)
from nltk.stem import WordNetLemmatizer
lemma=WordNetLemmatizer()
q=[]
for i in w:
   q.append(lemma.lemmatize(i))
r=[]
for i in q:
    if(i not in r):
        r.append(i)
s=[]
for i in r:
    s.append([])
    s[len(s)-1].append(i)
    s[len(s)-1].append(q.count(i))

for i in range(0,len(s)):
        print(s[i][0],"=",s[i][1])
x=[]
y=[]
for i in range(0,len(s)):
    x.append(s[i][0])
    y.append(s[i][1])
import matplotlib.pyplot as plt
c=["b","r","k","darkorange","royalblue","maroon"]
plt.bar(x,y,width=0.5,color=c)
plt.xticks(x,rotation="vertical")
plt.show()

