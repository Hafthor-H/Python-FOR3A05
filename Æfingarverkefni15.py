#A hluti 
USA = ["Ronald Reagan", "George H. W. Bush", "Billy Clinton", "George W. Bush, 9/11 AAAA", "Barrack Obama", "Donald Trump", "Joe Biden" ]


def mrPresident():
    spyrja = input("Viltu vita hverjir voru forsetar fyrir eða eftir 2000 Velja 1 fyrir 2000 eða 2 fyrir eftir 2000 ")

    if spyrja == "1":
        for i in USA[:3]:
            print(i)
    elif spyrja == "2":
        for i in USA[3::]:
            print(i)
    else:
        print("How did we get here")

#B hluti 

def mrPresidentGame():
    gameLoop = True
    while gameLoop: 
        quiz = input("Nefndu forseta Bandaríkjanna og ég skal athuga hvort hann sé í listanum ")
        if quiz in USA:
            spila = input("Hárétt, hann er á listanum\n Má bjóða þér að spila aftur(J). Ýttu á einhvern takka til að hætta ")
            if spila == "J":
                continue
            else:
                break
        else:
            spila = input("Hann er ekki í listanum :/\n Má bjóða þér að spila aftur(J). Ýttu á einhvern takka til að hætta ")
            if spila == "J":
                continue
            else:
                break
            
#C hluti

def mrPresidentGameImproved():
        flag = False
        gameLoop = True
        while gameLoop:
            quiz = input("Nefndu forseta Bandaríkjanna og ég skal athuga hvort hann sé í listanum ")
            firstThree = quiz[:3]

            for i in USA:
                if firstThree == i[:3]:
                    flag = True

            if flag:
                spila = input("Hárétt, hann er á listanum\n Má bjóða þér að spila aftur(J). Ýttu á einhvern takka til að hætta ")
                if spila == "J":
                    continue
                else:
                    break
            else:
                spila = input("Hann er ekki í listanum :/\n Má bjóða þér að spila aftur(J). Ýttu á einhvern takka til að hætta ")
                if spila == "J":
                    continue
                else:
                    break
                

#D hluti

def addPresident():
    question = input("Hver var forseti á undan Ronald Reagan? ")
    USA.insert(0, question)
    print("Hér er nýji listinn : ", USA)
    question2 = input("Hver var forseti á eftir Joe Biden? ")
    USA.append(question2)
    print("Hér er nýji listinn : ", USA)



addPresident()
