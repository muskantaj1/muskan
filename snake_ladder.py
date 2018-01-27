import random
count=0
r=0
while count<=100:
        roll=input("press q to roll")
        if roll=="q":
            r=random.randint(1,6)
            count=count+r
            if count>=100:
                print("you won")
                else:
                     print("you got",r)
                     print("your current location")
                    if count==8:
                        count=34
                        print("oh! climbed the ladder to", count)
                        elif count==13:
                            count=34
                            print("oh! climbed the ladder to", count)
                            elif count==40:
                                count=68
                                print("oh! climbed the ladder to", count)
                                elif count==52:
                                    count=81
                                    print("oh! climbed the ladder to", count)
                                    elif count==76:
                                        count=97
                                        print("oh! climbed the ladder to", count)
                                        elif count==38:
                                            count=9
                                            print("snake bite and your down at", count)
                                            elif count==25:
                                                count=4
                                                print("snake bite and your down at", count)
                                                elif count==11:
                                                    count=2
                                                    print("snake bite and your down at", count)
                                                    elif count==65:
                                                        count=46
                                                        print("snake bite and your down at", count)
                                                        elif count==93:
                                                            count=64
                                                            print("snake bite and your down at", count)
                                                            elif count==89:
                                                                count=70
                                                                print("snake bite and your down at", count)
                                                                else:
                                                                    print(count)
                                                                                                                                                                                           
