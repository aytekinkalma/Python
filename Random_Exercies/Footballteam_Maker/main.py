# players = [["Aytekin", 7.95], ["Musa", 8.25], ["Sadik", 7.95], ["Yakup" ,6.95], ["Omer Abi" ,5.90], ["Selman", 6.50], ["Hasan" ,8.95],
#            ["Cagri", 5.10], ["Gabit Hoca", 6.00], ["Zuhrettin", 6.55], ["Mustafa Abi", 6.75], ["Siriman" ,7.65]]
# ["Mustafa Anestezi", 6.35], ["Hadi Abi", 6.65], ["Osman", 4.30], ["Ahmet", 7.00], ["Ebubekir", 7.60]]

import random

while True:
        players = [["Aytekin", 7.95], ["Musa", 8.25], ["Sadik", 7.95], ["Yakup",6.95], ["Omer Abi",5.90], ["Selman", 6.50], ["Hasan",8.95],
                    ["Cagri", 5.10], ["Gabit Hoca", 6.00], ["Zuhrettin", 6.55], ["Mustafa Abi", 6.75], ["Siriman",7.65]]
        a_team=[]
        b_team=[]
        a = []
        b = []
        orta = 0
        ortb = 0
        totala = 0
        totalb = 0
        asayac=0
        bsayac=0
        asayac1 = 0
        bsayac1 = 0
        asayac2 = 0
        bsayac2 = 0
        i = 0

        while len(a) < 6:
                asayac = 0
                bsayac = 0
                asayac1 = 0
                bsayac1 = 0
                asayac2 = 0
                bsayac2 = 0

                sonuc = random.choice(players)
                a.append(sonuc)
                players.remove(sonuc)
                sonuc = random.choice(players)
                b.append(sonuc)
                players.remove(sonuc)
        while i < 6:
                totala += a[i][1]
                totalb += b[i][1]
                i += 1
        orta = totala / 6
        ortb =totalb / 6
        for i in range(0,len(a)):
                if a[i][0]=='Aytekin':
                        asayac+=1
                if a[i][0]=='Hasan':
                        asayac+=1
        for i in range(0, len(a)):
                if b[i][0]== 'Aytekin':
                        bsayac += 1
                if b[i][0]== 'Hasan':
                        bsayac += 1

        for i in range(0, len(a)):
                if a[i][0] == 'Cagri':
                        asayac1 += 1
                if a[i][0] == 'Omer Abi':
                        asayac1 += 1
        for i in range(0, len(a)):
                if b[i][0] == 'Cagri':
                        bsayac1 += 1
                if b[i][0] == 'Omer Abi':
                        bsayac1 += 1
        for i in range(0, len(a)):
                if b[i][0] == 'Musa':
                        asayac2 += 1
                if b[i][0] == 'Siriman':
                        asayac2 += 1
        for i in range(0, len(a)):
                if b[i][0] == 'Musa':
                        bsayac2 += 1
                if b[i][0] == 'Siriman':
                        bsayac2 += 1
        if abs(orta - ortb) < 0.1 and asayac!=2 and bsayac!=2 and asayac1!=2 and bsayac1!=2 and asayac2!=2 and bsayac2!=2 :
                print("A takimi ortalamasi={}".format(orta))
                print("B takimi ortalamasi={}".format(ortb))
                print("***********************************************************************************")
                # print("A takimi={}".format(a))
                # print("B takimi={}".format(b))
                for i in range(0,len(a)):
                        a_team.append(a[i][0])
                for i in range(0,len(b)):
                        b_team.append(b[i][0])
                print("A takimi:\n{}\n{}\n{}\n{}\n{}\n{}".format(a_team[0],a_team[1],a_team[2],a_team[3],a_team[4],a_team[5]))
                print('***********************************************************************************')
                print("B takimi:\n{}\n{}\n{}\n{}\n{}\n{}".format(b_team[0],b_team[1],b_team[2],b_team[3],b_team[4],b_team[5]))

                if(orta<ortb):
                        print('***********************************************************************************')
                        print('NOT!!!!!:\nIyi kaleciyi A takimi alacaktir')
                else:
                        print('***********************************************************************************')
                        print('NOT!!!!!:\nIyi kaleciyi B takimi alacaktir')

                break
