import os
from arboretum import Arboretum
from biome import River


def annex_biome(arboretum):
    os.system("cls" if os.name == "nt" else "clear")
    print("1. Mountain")
    print("2. Swamp")
    print("3. Grassland")
    print("4. Forest")
    print("5. River")
    print("6. Coastline")

    choice = input("Choose biome to annex > ")

    if choice == "1":
        # mountain = Mountain()
        # arboretum.mountains.append(mountain)
        pass
    if choice == "2":
        # swamp = Swamp()
        # arboretum.swamps.append(swamp)
        pass
    if choice == "3":
        # grassland = Grassland()
        # arboretum.grasslands.append(grassland)
        pass
    if choice == "4":
        # forest = Forest()
        # arboretum.forests.append(forest)
        pass
    if choice == "5":
        river = River("Test")
        arboretum.rivers.append(river)
        pass
    if choice == "6":
        # coastline = Coastline()
        # arboretum.coastlines.append(coastline)
        pass