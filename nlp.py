import string
from collections import Counter
from matplotlib import pyplot as plt
from tkinter import*
from tkinter import filedialog




window = Tk() 
window.title('Sentiment analyzer') 
window.iconbitmap('a.ico')
window.geometry("1000x500")
window.filename = filedialog.askopenfilename(initialdir="/C",title="Please select text files",filetypes=(("Text files","*.txt"),))
filenameopen = window.filename
print(filenameopen)
canvas = Canvas(window, width = 1000, height = 600)      
canvas.pack()

fopen=open(filenameopen)
fread=fopen.read()
datainlowercase=fread.lower()
datawithoutpunctuation = datainlowercase.translate(str.maketrans('','',string.punctuation))
sanitychacking=''
stopwords=["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
            "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
            "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
            "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
            "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
            "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
            "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
            "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
            "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
            "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
for dataelement in datawithoutpunctuation:
    if  dataelement!='\n' and dataelement!='    'and dataelement!='\r':
        sanitychacking+=dataelement
    else:
        continue
istofwords=sanitychacking.split()
#------ final words for NLP ------------------------------- stored in final words ---------
finalwords=[]
unnecessarywords=[]
for words in istofwords:
    if words in stopwords:
        unnecessarywords.append(words)
    else:
        finalwords.append(words)


# ------------------- Reading and storing clean emotions from emotions.txt -----------------
emotionfile= open('emotions.txt','r')
emotionlist=[]
for lines in emotionfile:
    lines=lines.replace("'",'').replace("\n",'').replace(",",'').strip()
    word , emotion = lines.split(':')
    if word in finalwords:
        emotionlist.append(emotion)
# ----------------------------------------------------------------------------------------------
frequencyofOccurance=Counter(emotionlist)


# ---------------------------------- plotting using matplotlib --------------------------------- 

fig , ax1 = plt.subplots()
ax1.bar(frequencyofOccurance.keys(),frequencyofOccurance.values())
fig.autofmt_xdate()
plt.savefig('generated.png')


img = PhotoImage(file="generated.png")      
canvas.create_image(100,100, anchor=NW, image=img)
window.mainloop() 



"""
if __name__ == "__main__":

    inputtext=input('Enter the document : ')
    listofip=inputtext.split('.')
    if listofip[1]=='txt':
        operationoftext(inputtext)
    elif listofip[1]=='docx':
        # here i have to read a .docx file and pass the contents to a new text file
        f=open('new.txt','w')
        f.write("I am having a bad day")
        f.close()
        fhand=open('new.txt').read()
        print(fhand)
    
"""
