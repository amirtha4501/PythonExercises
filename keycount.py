count = 0
a = str(input("\nEnter string keyword to check: "))
b = str(input("\nEnter word to replace the first word: "))
with open("keyreplace.txt","r") as f:
    for i in f:
        # print('hi')
        line = i.strip()
        #print(line)
        lower = line.lower()
        # print(lower)
        word = lower.split()
        # print(word)
        # for j in word:
        #if a.lower() in word:
        for i in range(len(word)):
            if(word[i]==a):
                word[i]=b.title()
                # for k in word:
                # j = b
                count  = count + 1
        new_str=" ".join(word)
        # print(new_str)
        # f.write(new_str)
            # f.write(s)
# return 1

with open("keyreplace.txt","w") as fr:
    fr.write(new_str)

        # strlist = ""
        # strlist1 = strlist.join(word)
        # strlist2 = strlist1.join(word)
        # strlist3 = strlist2.join(word)
    # for k in word: 
    #     strlist = ""
    #     strlist = strlist + k
print("\nThe word given is",count,"times present in the file")
# print("\nThe file after replacement: ")
# print(strlist1)