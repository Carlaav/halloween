# datos

nombres = ['Sand Crawler', 'T-16 skyhopper', 'X-34 landspeeder',
        'TIE/LN starfighter', 'Snowspeeder', 'TIE bomber',
        'AT-AT', 'AT-ST', 'Storm IV Twin-Pod cloud car',
        'Sail barge', 'Bantha-II cargo skiff', 'TIE/IN interceptor',
        'Imperial Speeder Bike', 'Vulture Droid', 'Multi-Troop Transport',
        'Armored Assault Tank', 'Single Trooper Aerial Platform', 'C-9979 landing craft',
        'Tribubble bongo', 'Sith speeder', 'Zephyr-G swoop bike', 'Koro-2 Exodrive airspeeder',
        'XJ-6 airspeeder', 'LAAT/i', 'LAAT/c', 'Tsmeu-6 personal wheel bike',
        'Droid tri-fighter', 'Oevvaor jet catamaran',
        'Raddaugh Gnasp fluttercraft', 'Clone turbo tank', 'Corporate Alliance tank droid',
        'Droid gunship', 'AT-RT', 'AT-TE', 'SPHA', 'Flitknot speeder',
        'Neimoidian shuttle', 'Geonosian starfighter','Executor', 'Sentinel-class landing craft',
        'Death Star', 'Millennium Falcon', 'Y-wing', 'X-wing', 'TIE Advanced x1', 'Slave 1',
        'Imperial shuttle', 'EF76 Nebulon-B escort frigate', 'Calamari Cruiser', 'A-wing',
        'B-wing', 'Republic Cruiser', 'Naboo fighter', 'Scimitar',
        'J-type diplomatic barge', 'Jedi starfighter', 'Star Destroyer', 'Trade Federation cruiser',
        'Theta-class T-2c shuttle', 'Rebel transport', 'Droid control ship', 'Republic Assault ship',
        'Solar Sailer', 'Republic attack cruiser', 'Naboo star skiff', 'Jedi Interceptor',
        'arc-170', 'Belbullab-22 starfighter', 'V-wing', 'CR90 corvette']

largo = [36.8, 10.4, 3.4, 6.4, 4.5, 7.8, 20.0, 2.0, 7.0, 30.0, 9.5, 9.6,
        3.0, 3.5, 31.0, 9.75, 2.0, 210.0, 15.0, 1.5, 3.68, 6.6, 6.23, 17.4, 28.82, 3.5,
        5.4, 15.1, 7.0, 49.4, 10.96, 12.3, 3.2, 13.2, 140.0, 2.0, 20.0, 9.8,19000,
        38, 120000, 34.37, 14, 12.5, 9.2, 21.5, 20, 300, 1200, 9.6, 16.9,
        115, 11, 26.5, 39, 8,47.9, 1600, 1088, 18.5, 90,
        3170, 752, 15.2, 1137, 29.2, 5.47, 14.5, 6.71, 7.9]
tripulacion = [46, 1, 1, 1, 2, 1, 5, 2, 2, 26, 5, 1, 1, 0, 4, 4, 1, 140, 1,
                1, 1, 1, 1, 6, 1, 1, 1, 2, 2, 20, 0, 0, 1, 6, 25, 1, 2, 1,279144.0, 5.0,
                342953.0, 4.0, 2.0, 1.0, 1.0, 1.0, 6.0, 854.0, 5400.0, 1.0, 1.0, 9.0, 1.0,
                1.0, 5.0, 1.0, 47060.0, 600.0, 5.0, 6.0, 175.0, 700.0,
                3.0, 7400.0, 3.0, 1.0, 3.0, 1.0, 1.0, 165.0]
pasajeros = [30.0, 1.0, 1.0, 0.0, 0.0, 0.0, 40.0, 0.0, 0.0, 500.0, 16.0, 0.0, 1.0,
            0.0, 112.0, 6.0, 0.0, 284.0, 2.0, 0.0, 1.0, 1.0, 1.0, 30.0, 0.0, 1.0,
            0.0, 2.0, 0.0, 300.0, 4.0, 0.0, 0.0, 36.0, 30.0, 0.0, 6.0, 0.0,38000.0, 75.0,
            843342.0, 6.0, 0.0, 0.0, 0.0, 6.0, 20.0, 75.0, 1200.0, 0.0, 0.0, 16.0, 0.0,
            6.0, 10.0, 0.0,  0.0, 48247.0, 16.0, 90.0, 139000.0, 16000.0,
            11.0, 2000.0, 3.0, 0.0, 0.0, 0.0, 0.0, 600.0]


# METODO DE LA BURBUJA GUARSANDO LISTA

def burbuja_carla(listado):
    tamano = len(listado)
    indice_provisional = list(range(tamano))
    for i in range(tamano-1):       
        for j in range(tamano-1-i): 
            if listado[j] > listado[j+1]:
                listado[j], listado[j+1] = listado[j+1], listado[j]
                indice_provisional[j], indice_provisional[j+1] = indice_provisional[j+1], indice_provisional[j]

    return(indice_provisional)


if __name__ == "__main__":

    n = len(pasajeros)

    # ordar por nombre
    print("\n")
    indice_ordenado = burbuja_carla(nombres[:])
    print("ordar por nombres")
    for i in indice_ordenado:
        print("Nombre de nave: {} | Largo de nave: {} | Tripulacion de nave: {} |  Pasajeros de nave: {}".format(
            nombres[i],largo[i],tripulacion[i],pasajeros[i]))


    # ordar por largo descendiente
    print("\n")
    indice_ordenado = burbuja_carla(largo[:])[::-1]
    print("ordar por largo")
    for i in indice_ordenado:
        print("Nombre de nave: {} | Largo de nave: {} | Tripulacion de nave: {} |  Pasajeros de nave: {}".format(
            nombres[i],largo[i],tripulacion[i],pasajeros[i]))


    # mostrar toda la información del “Halcón Milenario” y la “Estrella de la Muerte”;
    print("\n")
    print("mostrar toda la información del “Halcón Milenario” y la “Estrella de la Muerte”;")
    for i in range(n):
        if nombres[i] in ['Millennium Falcon','Death Star']:
            print("Nombre de nave: {} | Largo de nave: {} | Tripulacion de nave: {} |  Pasajeros de nave: {}".format(
                nombres[i],largo[i],tripulacion[i],pasajeros[i]))

    # top 5 naves con mas pasajeros
    print("\n")
    indice_ordenado = burbuja_carla(pasajeros[:])[::-1]
    print("ordar por pasajeros top 5")
    for i in indice_ordenado[0:4]:
        print("Nombre de nave: {} | Largo de nave: {} | Tripulacion de nave: {} |  Pasajeros de nave: {}".format(
            nombres[i],largo[i],tripulacion[i],pasajeros[i]))

    # # # indicar cuál es la nave que requiere mayor cantidad de tripulación;
    print("\n")
    indice_ordenado = burbuja_carla(tripulacion[:])[::-1]
    print("indicar cuál es la nave que requiere mayor cantidad de tripulación;")
    print("Nombre de nave: {} | Largo de nave: {} | Tripulacion de nave: {} |  Pasajeros de nave: {}".format(
        nombres[indice_ordenado[0]],largo[indice_ordenado[0]],tripulacion[indice_ordenado[0]],pasajeros[indice_ordenado[0]]))

    # mostrar todas las naves que comienzan con AT;
    print("\n")
    print("mostrar todas las naves que comienzan con AT")
    for i in range(n):
        if nombres[i][0:2] == 'AT':
            print("Nombre de nave: {} | Largo de nave: {} | Tripulacion de nave: {} |  Pasajeros de nave: {}".format(
                nombres[i],largo[i],tripulacion[i],pasajeros[i]))

    # listar todas las naves que pueden llevar seis o más pasajeros;
    print("\n")
    print("listar todas las naves que pueden llevar seis o más pasajeros")
    for i in range(n):
        if pasajeros[i] >= 6:
            print("Nombre de nave: {} | Largo de nave: {} | Tripulacion de nave: {} |  Pasajeros de nave: {}".format(
                nombres[i],largo[i],tripulacion[i],pasajeros[i]))

    # ordar por largo ascendiente
    print("\n")
    indice_ordenado = burbuja_carla(largo[:])
    print("ordar por largo")
    for i in indice_ordenado:
        print("Nombre de nave: {} | Largo de nave: {} | Tripulacion de nave: {} |  Pasajeros de nave: {}".format(
            nombres[i],largo[i],tripulacion[i],pasajeros[i]))
