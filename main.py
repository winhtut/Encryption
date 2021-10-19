
import random
import platform

class User:
    def __init__(self):
        self.players_name=[]
        self.players_money=[]
        self.jugdeMoney = 10000
        print("Welcome to our game:")

    def start(self):

        players=int(input("How many player wanna play:"))

        for i in range(players):
            self.players_name.append(input("Enter {0} player name:>".format(i)))
            print("Welcome :",self.players_name[i])
            self.players_money.append(int(input("Enter {0}'s Money:>".format(self.players_name[i]))))

    def randNumber(self):
        randNumber = random.randint(10,20)
        return randNumber

    def update(self):

        edit = int(input("Press 1 to continue or press 2 to edit information"))
        if edit == 1:
            pass
        elif edit ==2:
            self.players_name.clear()
            self.players_money.clear()
            self.start()
        else:
            print("Invalid option:")
            self.update()

class MyEncrypt:
    def __init__(self):
        self.uname=[] #list

        self.unameValueList = [] # for game user name value list
        self.unameAdd=0 #for computer username adding value

        self.addTwoUname=[]
        self.finalEncryptValue=0
    def encrypt(self,gusername):
        node = list(platform.uname())
        edata =list(gusername)
        # for game user name data
        for i in edata:
            print(ord(i))
            self.unameValueList.append(ord(i))


        #for computer user name
        for z in node[1]:
            print(ord(z)) #y = mx + b
            self.uname.append(ord(z))

        for a in self.uname:
            self.unameAdd = self.unameAdd+a


        #Final Encryption
        for x in self.unameValueList:
            y= x + self.unameAdd
            self.addTwoUname.append(y)

        for add in self.addTwoUname:
            self.finalEncryptValue = self.finalEncryptValue+add

        print("all data from self.uname",self.uname)
        print("Added value:",self.unameAdd)

        print("Final Encryptin list adding value:",self.addTwoUname)

        print("The final value is:>",self.finalEncryptValue)


class MyDecrypt:
    def __init__(self):
        self.toDecrypt=1225
        self.finalOraginalChar=[]

        self.first_decryptedValue = 0 # firstly game uname removed value
        self.decrypt2Value=[]

    def decrypt1(self): #Fristy remove game user name value :
        for i in encrypt.addTwoUname:
            # print("from addTwoUname:",i)
            oraginalAsciivalue=i - encrypt.unameAdd
            oraginalChar = chr(oraginalAsciivalue)
            print("OraginalAsciiValue ",oraginalAsciivalue , oraginalChar)

            self.finalOraginalChar.append(oraginalChar)

        print(''.join(self.finalOraginalChar))


if __name__ == '__main__':
    game = User()
    # game.start()

    # print(game.randNumber())
    # game.update()
    # print(game.players_name, game.players_money)
    gusername=input(("Please enter your user name"))

    encrypt = MyEncrypt()
    encrypt.encrypt(gusername)
    # encrypt.encrypt()

    decrypt = MyDecrypt()
    decrypt.decrypt1()





