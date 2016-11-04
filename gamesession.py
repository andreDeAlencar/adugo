from Adugo import Adugo

C_WAIT_JAGUAR = "WAITING JAGUAR"
C_WAIT_DOG = "WAITING DOG"

a = Adugo()


while True:
    a.newBoard()
    while a.getStatus() not in ["JAGUAR_WIN", "DOGS_WIN"]:
        print(a.getBoard())
        if a.getStatus() == C_WAIT_JAGUAR:
            print("Jaguar turn")
            while True:
                if a.jaguarWalk(int(input())):
                    break
                print("not valid")
        elif a.getStatus() == C_WAIT_DOG:
            print("Dog turn")
            while True:
                if a.dogPlay(int(input()), int(input())):
                    break
                print("not valid")