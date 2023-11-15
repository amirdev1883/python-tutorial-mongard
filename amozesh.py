# print ("heloo world !")
    #calss haiye (int , float  , string )

# name = 'amir abbas' #this is my name
# print (name)
#print (type (name))

    #amal haiye riyazi dar python (zarb  *  , jam  +  , tafrigh  -  , taghsim  /  , tavan  **  )
    #braye inke hasel taghsim be sorat yek adad gheir ashara bashad az // estefade mi konim

# print(15/2)
# print(15//2)
# a = 15/2
# a = round(a)
# print(a)


    #sting ha ro mishe ba   '   ,   "   zakhire kard
    #backe eslash dar string baes skip mishavad manand mesale payin ye jor bi mana kardaneshe

#print ('you can't read this')      XXXXXXXXXXXXXXXXXXXXXXXXXX

    #khorojiye bala estebah ast v dastgah an ra nmi tavanad kampyl konad pas az back eslash estefade mikonam

#print ('you can\'t read this')

    #dar code bala mitonim az  "  ham estefade konim
# \n   be manaye newline ast
#print ('amir \n abbas')

    #braye gheier faal kardane \n az yek eslash digar estefade mikonim

#print ("amir \\n abbas")


     #اینجا فهمیدم میشه فارسی هم تایپ کرد ولی چرا خوندنش سخته اهههههههه

#print (round (22.55))

    #tabe round adad ro rond mikone

#a= "amir"
#b= "abbas"
#print(a+b)

#a= "10"
#a=  10

    #in do fargh darand , avali a yek sting ast v dovomi yek intijer
    #dar python nmi shavad string ra ba intijer jam kard

# print("hello " 'world')

    #code bala dorost ast
    #braye neveshtane yek string boland mitavanid kare zir ra anjam dahid

# name = 'Hello my name is amir'\
#       'nice to meet you'\
#       'what is your name'
# print (name)

#name = ('Hello , my name is amiabbas'
#        'nice to meet you'
#        'what is your name ')
# name = '''
# Hello , my name is amiabbas
# nice to meet you
# what is your name
# '''

#print (name)

    #charactery darim be name   len   ke mokhaffafe length ast

# name = 'salam man amir abbas          ast'
# print (len(name))
    #ba bracet mitanim teke iy az string khod ra chap konim

# x = '0123456789'
# print ( x [0])
# print ( x [-1])
# print ( x [2:4])
# print(x[-5:-1])
# print ( x [-5: ])
# print ( x [ : 8 ])
# print ( x [0:9:2])
# print ( x [0:9:3])
# print ( x [0:9:1])

    #string ha gheyr ghabele taghiyir hastan be estelah immutable ast
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------

                                    #list

    #braye zakhire kardane chand meghdar mitonim on ha ro toye list zakhire konim

# names = []
# print (names)
# print (type (names))   #khoroghi in   <class list>   ast

# x = ['amir' , 'abbas' , 'ali' , 'iman'  , 12 , 12.22 ]
# print ( x [ : ])
# y = ['alo' , 'amiro' , 13.2]
# print (x + y)    #khoroghi in code list x sepas y ast
    #list ha bar khalaf string ha mutable ya hamon ghabel taghiyr hastand

# names = ['ali' , 'amir abbas' , 'iman' , 'ghaghaly' , 'mohammad']
# names [0] = 'sibiloiyan'
# names [2] = 'lalalal'
# names [3 : ] = ['baba' , 'maman']
# print (names)

    #mitavanim ba append yek meghdar ra be listeman ezafe konim

# names = ['ali' , 'amir abbas' , 'iman' , 'ghaghaly' , 'mohammad' ]
# names.append('ali lala')
# print (names)
# print (len(names))

    #baraye hazf kardane bakhshi az list an ra mosavi ba khali gharar midahim

# names = ['ali' , 'amir abbas' , 'iman' , 'ghaghaly' , 'mohammad']
# names[0:2] = []
# print (names)

# len braye list ham estefade mishavad

# x = ['ali' , 'amir abbas', 'mohammad', 'abolfazl']
# print (len(x)) #khorojy adad 4 ast
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------

                                      #while

    #ta vaghti ke shart halghe dorost ast amaliyat an ejra mi shavad

# a , b = 2 , 20
# while a < 100:
#     a = a + 1         #mitanim jaye in   a += 1
#     print (a)
# v yeki az digar ghabeliat haye print
# a , b = 2 , 20
# while a < 100:
#     a = a + 2
#     print (a , end = ' / ' )
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------

                                # if v else v elif

# x = int(input('please enter your age :'))
# if x < 18 :
#     print ('no')
# elif x == 18 :
#     print ('yes ma braye shoma hediye iy darim')
# else :
#     print ('yes')

    #bolean bool  --> True , False

# if True :
#     print ('greater than 30')
# if False :
#     print('greater than 10')

    #dar ghesmate bala bayad avale horofe true v false bayad capytal bashad
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------

                                        #for

# words = ['amirabbas' , 'ali' , 'iman']
# for w in words :
#     print ( w , len(w) , end = '|')

    #deghat dashte bashid ke dar string ha ghabeliyat charkhesh (itrabele) ast ama aadad kheyr

# words = '123'
# for w in words :
#     print ( w , end = '|')
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------

                                        #range

    #yek donbale iy az adad ra be ma midahad

# print (range (5))       #be ma yek object ra midahad

# for x in range(5):
#     print ( x )           #khorogy cahp mi shavad az adad 0 ta 4

# for y in range(5 , 15):
#     print ( y )           #khorogy cahp mi shavad az adad 5 ta 14

# for y in range(5 , 15 , 2):
#     print ( y )             #khorogy bala ba step 2 yani do ta do ta az 5 ta 14 chap mi shavad

# for y in range(-5 , -20 , -2):
#     print ( y )

    #kare list in ast ke yek object ra be list tabdil konad

# print ( list (range(10)))
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------

                                #break v continue v else baraye loop ha v pass

# names = ['amirabbas' , 'ali' , 'admin' , 'iman' , 'hasan' ]
# for x in names :
#     if x == 'admin':
#         continue
#     print (x)               #agar x barabar shod ba admin rad kon an ra v halghe ra edame bede


# names = ['amirabbas' , 'ali' , 'admin' , 'iman' , 'hasan' ]
# for x in names :
#     if x == 'admin':
#         break
#     print (x)                 #agar x barabar shod ba admin halghe ra motevaghef kon

# names = ['amirabbas' , 'ali' , 'admin' , 'iman' , 'hasan' ]
# for x in names :
#     print (x)
# else :
#     print ('End....')           #halghe zamani ke be akharin draye miresad else ejra mi shavad

    #agar dar codeman breack dashte bashim else ejra nemi shavad

# names = ['amirabbas' , 'ali' , 'admin' , 'iman' , 'hasan' ]
# for x in names :
#     if x =='ali' :
#         break
#     print (x)
# else :      #in else birone halghe ma ast
#     print ('end...')
    

    #pass baraye in ast ke yek halghe ra dar majmoe code hayeman dashte bashim ke movaghta kari nemi konad
    #be jaye pass mitavan az object elleipsis ham estefade kard ke haman  ...  ast

# names = ['amirabbas' , 'ali' , 'admin' , 'iman' , 'hasan' ]
# for x in names :
#     pass

# names = ['amirabbas' , 'ali' , 'admin' , 'iman' , 'hasan' ]
# for x in names :
#     ...
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------

                                                   #Function

    #braye kamtar neveshtane code az Function estefade mikonim
    #kafi ast yek tabe ra seda bezanim ta an kari ra ke mikhahim ra baraye ma anjam dahad
    #def be manaye define ast

# def show ():
#     print ('Hello world !')
#
# show()          #inja tabe ra seda zadim

# def show (name , age ):                  #meghdary ke function entezar darad ke barayash biyayad ra arguement migoyand
#     print ('Hello ' + name)
#     print ('you are '+ name + ' years old')
# show('amir' , '18')                             #be an maghadiry ke ma ersal mikonim be functoin ra parameter migoyand

    #nokte python adad ra nemitavanad be string bechasbanad
    #ye vaghtaiyy be parameter ha arguement migoyand ya bar aks ke moredi nadarad v dorost ast
    #az kalamat rezer shode kelidiye python braye name function estefade nakonid
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------

                                                #List methods

#bararye kar ba list ha yek sery tabe az ghabl tarif shode dar python darim ke ba seda zadan an ha mitavanim
#ba on ha bishtar kar konim

# names = ['ali' , 'amir abbas' , 'iman' , 'iman']
# names.append('baba')                  #baraye ezafe kardane ye done item
# names.append(['salami' , 'mamady'])   #fargh tabe bala v payin inja malmos tar mishavad
# names.extend (['salami' , 'mamady'])  #baraye ezafe kardane ye list be listeman
# names.insert ( 2 , 'bob')             #bakhsh aval tabe jaygahe itemy ke mikhahid ezafe konid ast
                                      #v bakhsh dovom haman item
# names.insert ( 5 , 'amir abbas')
# names.remove ('mamady')               #ba in method item mored nazar ra nam borde v hazf konid
# names.pop()                           #dar halate difalt in tabe agar khaly begzarid akharin item ra hazf mi konad
# names.pop(2)                       #ba dadn adad item ke dar on jaygah gharar darad hazf mi shavadprint (names.pop(2))
# print (names)                         #v mitavanid on ra return konid
# print (names.pop(2))                  #inja amalkard pop behtar malom mishavad
# print(names.index('amir abbas'))      #in tabe naeshan midahad ke itemy ke neveshte in iteme chandome list ast
# print(names.index('amir abbas' ,  2)) #bakhsh dovom ekhtiyary ast v migoyad ke dar kodam item baad az on shomare
                                      #in meghdar vojod darad
# print(names.index('amir abbas' ,2,5)) #adad aval v adad dovom baze iy ast ke az tabe jaiye item ro miporsim
                                     #agar dar tabe index dara on baze nabod eror baraye ma ersal mi shavad
# print (names.count('amir abbas'))
# names.clear()                         #in tabe tamam item haye dakhele list ra pak mikonad
# print (names)                      #ba print kardan list pas az tabe mibinim ke kol list bar asar clear pak shode ast

# names = ['amir' , 'abbas' , 'ali' , 'iman']
# names.sort()                                    #tabe sort tartib bandi mikonad bar asas horof alefba
# print(names)
# print (names.sort())                             #in be ma khorojy khali mi dahad

# names = ['amir' , 'abbas' , 'ali' , 'iman']
# names.reverse()                                     #tabe reverse tartibe item ha ra bar aks mi konad
# print(names)


#tabe copy niz vjod darad ke pishrafte ast v mitavan on ra bad ha braye mbahes movred niyaz amokht

# names = ['amir' , 'abbas' , 'ali' , 'iman']
# del names                                    #dar halat difalt agar an ra khaki begozarim kole list ra hazf mi konad
# print(names)                                 #clear item haye list ra khali mi kard ama in be tanhayy kamel mi pakad

# names = ['amir' , 'abbas' , 'ali' , 'iman']
# del names [ 1:2 ]                                   #dar in halat item mored nazar r amitavanid pak konid
# print(names)
#ye jam bandiye mashti

# append  ,  extand  ,  insert  ,  remove  ,  pop  ,  *index*  ,  count  ,  clear  ,  sort  ,  reverse  ,  del

#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------

                                     # tuple and sequences

#tuple ha immutable hastand
#mi tavan tuple ha ra dar beyn do prantez ham zakhire kard

# names = 'amirabbas' , 'ali' , 'iman' , 'hasan' , 12 , (54321 , 12345)
# x = (12345 , 'amirabbas' , 'ali' , 'alireza')
# y = (1234 , 'amirabbas' , ['ali' , 'hassan' , 3])
# print (names)
# print (type(names))
# print (type (x))
# print (type (y))
# print (y)
# print (names[0])

#---------------------------------------------------------------------------------------------------------------------

# n = []
# t = ()
# print (type(n))
# print (type (t))

#dar ghesmat bala korojy print (type(t)) tuple  ama dar payyin khorojy str ast

# n = ['amirabbas']
# t = ('amir')
# print (type(n))            #khorojy class list  ast
# print (type(t))            #khorojy class str ast

#braye shenasandane t be onvane tuple kar paiyn ra anjam midahim

# t = ('amir' ,)
# print (type(t))

#--------------------------------------------------------------------------------------------------------------------
#tfavot haye tuple v list ra dar internet serch konid
#braye zakhire kardane etelaaty ke ziad shabihe ham nidtand az tuple estefade mi konim v agar etelaat shabih be ham ra
#khastim zakhire konim az list estefade mi konim
#list ha mutable hastand ama tuple ha immutable pas agar ghasd taghiyre dade hayeman ra dashtim az list estefade komim

#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------

                                              #sets

#set ha ham daghighan kareshon mesle list ha v tuple ha ast be shoma ejaze midahad chand meghdar dakhek yek
#moteghayer ezafe bokonid   ama   do fargh darad
#1.nmi tavanid meghdare tekrary dashte bashid
#2.na monazam ast v tartibe vorode etelaat ra hefz nmi konad

# names ={'amir' , 'abbas' , 'ali' , 'iman' ,'amir' , "amir" , 'amir' , 'amir' , 'Amir'}
# print (names)                   #agar chand bar khorojy begirim mibinim ke khorojy ha fargh darn v sabet nistand

# x = { 1 , 2 , 3 , 4 , 5}
# if 1 in x:
#     print ('yes')
# if 21 not in x:
#     print ('yes')

# letters = set()
# print (letters)

# letters = set('amirabbas')
# print (letters)

#set amaliyate riyazy ra ham poshtibany mikonad

# a = set('abcdefghi')
# b = set('cdefghijk')
# print ( a - b )                 #letters in a but not in b
# print ( a | b )                 #letters in a or b or both
# print ( a & b )                 #letters in both a and b
# print ( a ^ b )                 #letters in a or b but not both

#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------
                                                #Dictonary
                                            #key : value pair

#dictonary ha daghigh medle bagheye donbale ha hastand
#be shoma ejaze midahad chand meghdar ra dar an zakhire konid
#maghdir be sorat kilid meghdar save mi shavad
#dictonary ha mutable hastand v tartib vorode ra hefz mi konad

# tel = { 'jack' : 9133633480 , 'mohammad' : 9123605425 , 20 : 'aliviya'}
# tel ['iman'] = 9367107429
# tel ['jack'] = 9137107429
# del tel ['mohammad']
# print (tel)
# print ( 'amir' in tel)
# print ('mohammad' in tel)
# print ('jack' in tel )
# # print (20 in tel)                 #neshan midahad ke hamchin key vjod darad dar dictonary ma 
# print (tel.items())
# print ('-----------------------------------\n')
# for i in tel.items():
#     print (i)
# print ("\n")
# print ('-----------------------------------\n')
# for k , v in tel.items():
#     print ( k , v)

#digar emkanati braye dictonary vojod darad ke mitavanid az tutarial python dar sait pyton estefade konid

# ages = dict  ([     ('amir' , 20) , ('abbas' , 18) , ('mohammad' , 30)    ])
# print (ages)

# nomre = dict (( ('ali' , 20 ) , ('mohammad' , 2 ) , ('alirza' , 18 ) ))
# print (nomre)
# print (type (nomre))

#az in halat dar code haye pichide estefade mishavad ama dar halat ady behtare ke az dic estefade nakonim

#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------

                                                #Module

#zmani ke dar python code mizanim momkene barnammon barnammon bozorg beshe v natonim tamam code ha ro dakhele yek file
#bezanim az Mudule estefade mikonim
#vaghty code haye ma ziyad mishavad code hayeman ra dakhele chand file zakhire mikonim
#be har file python ba pasvand   .py    ra module mi goyim
#agar file pythone ma dar poshe iy gheyr az hamna poshe bod
#braye dastresy be an aval esm poshe sepas bedone fasele noghte mi gozarim
#mesle        projects.app.amozesh

# import amozesh_one
# amozesh_one.say_something_to_user()

# from amozesh_one import say_something_to_user
# say_something_to_user()

# from amozesh_one import say_something_to_user , names         #inja names ro ham ezafe kardim
# say_something_to_user()

#parantez ra zamani jeloye tabe man migozarim ke bekhahim an ra ejra konim

# from amozesh_one import say_something_to_user as great        #inja esme tabe man ra avaz kardim
# great()

# from amozesh_one import *                   #dar estefade az in deghat konim chon koll file ra import mi konad

#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------

                                                #-fsting
                                            #input v output


#baraye zamani estefade mi shavad ke shoma bekhahid chand motaghayer ra ba string ghati bokonid

# name = "amir"
# age = 18
# print ( name + " is" + age + "years old")

#khoroji code be ma eror dade mishvad ama yek rah braye hal an ast

# name = "amir"
# age = str(18)
# print ( name + " is " + age + " years old")

#ya in rah

# name = "amir"
# age = 18
# print ( name + " is " + str(age) + " years old")

# name = "amir"
# age = 18
# print ( f'{name} is {age} years old')           # mi tavanim ham f v F  estefade konim farghy nadarad

# name = "amir"
# age = 18
# print ( f'{name:10} is {age} years old')    #in chizi ke ezafe kardim baraye fasele gozary ast
                                            #khorajy haman ghabli ast ama 6 fasele ezafe shode
                                            #chon amir 4 ta charecter ast v ma ba in code be computer gofte im 10 fasele
#karbord in fasele gozary bra tamiz neveshtane code v khroji ra betvanim moratab konim

#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------

                                                    #format

#format braye in ast ke chand moteghayer ra dakhele yek string ja bedahim

# name = 'amir abbas'
# age = 18
# print ('{} is {} years old .'.format (name , age))
# print ('{} is {} years old'.format('ali' , 13))
# print ('{0} is {1} years old .'.format (name , age))
# print ('{1} is {0} years old .'.format (name , age))
# print ('{n} is {a} years old .'.format (n = name , a = age))
# print ('{a} is {n} years old .'.format (n = name , a = age))

# info = {'name':'amir abbas' , 'age':12}
# info2= {'name':'ali' , 'age' : 18}
# print ('{0[name]} is {0[age]} years old and {1[name]} is {1[age]} years old.'.format(info , info2) )

#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------

                                                 #file

# 'w'  braye neveshtani bodane file ast ,  'r'   braye khandani bodan file ast
# agar bekhahid be file tan chizy ezafe konid minevesid az 'a' ke append ast estefade konid
#  'r+'  v  'rw'  braye neveshtni v khandani bodane file ast
# agar bakhsh dovom ra vared nakonid dar halate diffalt   'r'  ast

# f = open('text.txt' , 'r')              #ya mitavanim open ('text.txt') chon dar halat difalt 'r' ast
# print (f)                               #khorojiye in code etelaate marbote be file ash ast
# print (f.read())
# f.close()                               #inja baad az baz shodane file dar khat 523 mitavanim an ra bebandim
#print (f.closed)                         #khorojy in code kalame true ast chon dar khate bala file baste shode

# with open ('text.txt') as f :             #in yek contex manager ast ke python ham an ra pishnehad karde ast
#     pass                                  #tarz karash in ast ke yek kary ra braye shoma anjam midahad
                                            # v vaghty an kar tamam shod an ra braye shoma mibandad
# print (f.closed)                          #khojy in tabe be ma migoyad file ma baste shode ya na

# with open ('text.txt') as f :
#     print (f.readlines())

# with open ('text.txt') as f :
#     print(f.readline())
#     print(f.readline())
#     print(f.readline())

# with open ('text.txt') as f :
#     print(f.readline())

# with open ('text.txt') as f :
#     print(f.read(20))
#     print(f.read(20))
#     print(f.tell())                                 #be ma neshan mi dahad ke computer ta kojaye file ra khande

# with open ('text.txt') as f :
#     f.seek (34)                                    # f.seek migoyad az an jaiye ke taiyen kardam be baad ra bash kar daram
#     print (f.read(24))

# with open ('text2.txt' , 'w') as f :
#     f.write('mamad gholi')                        #deghat dashte bashid ke agar ghabl az neveshtan neveshte iy dar an
                                                    #file bashad be kol pak mishavad

# with open ('text2.txt' , 'a') as f :                    # 'a'  braye append ast ke akhare file chizi ra ezafe konad
#     f.writelines(' \n salam bar shoma dost aziz')       #ba har bar ejraye in code yek khat be file ma ezafe mishavad
                  #deghat konid ke agar mikhahid baad az append kardan jomle ya an chizy ke vared karde id bekhate baad
                  #montaghel shavad  \n   ra faramosh nakonid

#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------

                                                #scope

                                     #global scope v local scope

# a = 20        #global scope

# def a_ra_neshan():
#     print(a)

# a_ra_neshan()



# a = 20      #global scope

# def a_ra_neshan():
#     a = 10                  #local scope 
#     print(a)

# a_ra_neshan()

#khorojy code bala 10 ast 

# a = 20 
# def a_ra_neshan():
#     print(a)
#     a = 10


# a_ra_neshan()

#UnboundLocalError: local variable 'a' referenced before assignment
#eror code bala

# a = 10 
# def a_ra_neshan():
#     global a 
#     print(a)
#     a = 20

# a_ra_neshan()
# print(a)

#khorojy code bala
# 10
# 20


#mafhome scope ha ra be khobi yad begirid

#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------

                                        #OOP (Object_oriented_programing)

#raveshi ke be shoma komak mi konad tamiz tar code bezanid
#braye modiryat kardane code haye shoma
#besyar mohem

# class car :     #blueprint    halate koly
#     pass
# a = car()   #be in migoiym object ya instance #nemone kochek tar
# b = car()
#
# a.name ='pride'    #be migan attribute ya property
# b.name ='benz'

# a.price = 100       #be in migan dot notation   ke ba noghte be vizegi hash ezafe kardim ya dastresy peyda kardim
# b.price = 900
#
# print(a.price)
# print(b.name)
#
# print(f'{a.name} cpsts {a.price}')
# print(f'{b.name} cpsts {b.price}')

#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------

                                             # method haye oop

#method haman function hast faght dar class gharar gerefte ast
#hich farghy ba function nadarad v baraye tamiz neveshtane code haman estefade mi shavad

# class car :
#     def show (self):                #harchiz mi tavanim braye argoman entekhb konim vli self braye fahme an behtar ast
#         print ('this is method....')
#         print (self)
#
#
# a = car()
#
# a.show()             #inja darim  a  ra be tabe ersal mikonim v agar dakhele tabe argomany nabashd eror braye ma mi ayad
# print(a)

#dar class haye python yek sery method khosash darad ke kare ma ra rahat tar mi konad

# class car:
#     def __init__(self):         #in form esm braye tabe neshan midahad ke braye python ast ya built-in ast
#         print('this is initializor')
#
#     def show(self):
#             print ('This is method...')
#
# c1 = car()
# c2 = car()
#
# c1.name = 'prid'
# c2.name ='benz'
#
# c1.price = 100
# c2.price = 900


# class car:
#     def __init__(self , n , p ):
#         self.name = n
#         self.price = p
#     def show(self):
#         print('imane koni')
#
# c1 = car('prid' , 100)
# c2 = car('benz' , 900)
#
# print (f'{c1.name} costs {c1.price}')
# print (f'{c2.name} costs {c2.price}')



# class car:
#     def __init__(self , n , p):         #ba karbord intializor ashna mi savim
#         self.name  = n
#         self.price = p
#         print(f'{self.name} costs {self.price}')
#
# c1 = car('pride' , 100)
# c2 = car('benz'  , 900)


#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------

                              #        instance variable , class variable
#variable--> 1.class  2.instance

# class car:
#     wheel = 4
#     def __init__(self , n , p):
#         self.name = n
#         self.price = p
#         print (f'{self.name} has {self.wheel} wheel  ')     #mitavind be jaye self , car  benevisid
#
#
# c1 = car ('pride' , 100)
# c2 = car ('benz' , 900)
#
# print(car.__dict__)
# print(c1.__dict__)



# class car:
#     wheel = 4
#     def __init__(self , n , p):
#         self.name = n
#         self.price = p
#     def show(self):
#         print(f'{self.name} has {self.wheel} wheels')
#
# c1 = car ('pride' , 100)
# c2 = car ('benz' , 900)
#
# c1.wheel = 5
#
# c1.show()
#
# print(c1.__dict__)
# print(c2.__dict__)
# print(car.__dict__)



# class car:
#
#     obj_nums = 0
#
#     def __init__(self , n , p):
#         self.name = n
#         self.price = p
#
#         car.obj_nums += 1
#
#     def show(self):
#         print(f'{self.name} has {self.wheel} wheels')
#
# c1 = car ('pride' , 100)
# c2 = car ('benz' , 900)
# c3 = car ('pride' , 100)
# c4 = car ('benz' , 900)
#
# print(car.obj_nums)


#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------

# import datetime                                    #built in   ast
#
# result = datetime.datetime.now()
# result1 = datetime.datetime.now().year   -  18       #data ha ra mitavan kam v ziyad ham kard
# result2 = datetime.datetime.now().month
# result3 = datetime.datetime.now().day
# result4 = datetime.datetime.now().hour
# result5 = datetime.datetime.now().minute
# result6 = datetime.datetime.now().second
#
# print(result)
# print(result1)
# print(result2)
# print(result3)
# print(result4)
# print(result5)
# print(result6)

#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------

                                    #static method , class method

# method --> 1.instanc 2.class 3.static


# import datetime
#
# class person:
#     def __init__(self, name , height , age):
#         self.name = name
#         self.height = height
#         self.age = age
#     def show(self):
#         print(f'{self.name} is {self.height} and {self.age} years old.')
#
#     @classmethod
#     def from_birth(cls , name , height , age):
#         return cls(name , height , datetime.datetime.now().year - age)
#
#
# print('name khod ra vared konid :')
# b = input()
# print('ghade shoma chand santy metr ast ?')
# c = int (input())
# print('sale tavalade khod ra vared konid :')
# d = int (input())
#
# p1 = person.from_birth( b , c , d)
# p1.show()




# import datetime
#
# class person:
#     def __init__(self, name , height , age):
#         self.name = name
#         self.height = height
#         self.age = age
#     def show(self):
#         print(f'{self.name} is {self.height} and {self.age} years old.')
#
#     @classmethod
#     def from_birth(cls , name , height , age):
#         return cls(name , height , datetime.datetime.now().year - age)
#
#     @staticmethod
#     def is_adult(age):
#         if age >= 18:
#             print('yes')
#         else:
#             print('no')
#
# a = int(input())
# person.is_adult(a)

#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------

                                              #lnhetirance

# class car:
#     wheel = 4
#     def __init__(self , name):
#         self.name = name
#     def show(self):
#         print(f'i have a {self.name}')
#
# class motor(car):
#     wheel = 2
#     def show(self):
#         print(f'i have a {self.name}')
#         print(f'i ride {self.name}')
#
# m = motor('honda')
# # help(m)                                 #mro  method resusion order
#
# m.show()



# class car:
#     wheel = 4
#     def __init__(self , name):
#         self.name = name
#     def show(self):
#         print(f'i have a {self.name}')
#
# class motor(car):
#     wheel = 2
#     def show(self):
#         super().show()          #ghablaa be shekle  super(motor , self ).show   bode    ghable python 3
#         print(f'i ride {self.name}')
#
# m = motor('honda')
# # help(m)                                 #mro  method resusion order
#
# m.show()








