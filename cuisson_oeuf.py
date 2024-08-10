import time


def choisir_option():
    print("Cuisson des oeufs")
    print("-----------------")
    print("""a) Oeufs à la coque : 3 minutes
b) Oeufs mollets : 6 minutes
c) Oeufs dur : 9 minutes""")
    choix = 0
    while not choix == "a" or choix == "b" or choix == "c":
        choix_str = input("Votre choix : ")
        choix = choix_str
    if choix == "a":
        minuteur_cuisson(3)
    elif choix == "b":
        minuteur_cuisson(6)
    elif choix == "c":
        minuteur_cuisson(9)


def minuteur_cuisson(temps: int):
    d = temps * 60
    print(f"Cuisson en cours ", end="", flush=True)
    while d > 0:
        for i in range(10):
            time.sleep(1)
            d -= 1
            print(".", end="", flush=True)
            if d <= 0:
                break
        min = d//60
        sec = d-min*60
        if d <= 0:
            break
        print(f"\nTemps restants : {min:02d}:{sec:02d}", end="", flush=True)

    print("\nvotre Cuisson est prêt")


# choisir_option()



def minuteur():
    duree = 3*60
    for d in range(duree, 0, -1):
        min = d//60
        sec = d-min*60
        print(f'{min:02d}:{sec:02d}', end='\r')
        time.sleep(1)
        d -= 1

