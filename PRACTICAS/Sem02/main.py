from PRACTICAS.Sem02.ironman import IronMan
from PRACTICAS.Sem02.spiderman import SpiderMan

if __name__ == "__main__":
    tony = IronMan()
    peter = SpiderMan()
    print(tony)
    print(peter)

    # Ronda 1
    tony.usar_poder("repulsores", objetivo=peter)
    peter.atacar(tony)

    # Ronda 2
    peter.usar_poder("sentido arácnido")  # poder pasivo
    tony.usar_poder("misiles", objetivo=peter)

    # Curación y estado final
    peter.curar(15)
    print(tony)
    print(peter)
