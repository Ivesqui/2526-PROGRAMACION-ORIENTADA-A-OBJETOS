import random
from heroe import heroe


class SpiderMan(heroe):
    def __init__(self, nombre_real: str = "Peter Parker", alias: str = "Spider-Man"):
        super().__init__(nombre_real=nombre_real, alias=alias,
                         salud_max=90, salud_actual=90,
                         poderes=["sentido arácnido", "lanzaredes", "agilidad"],
                         equipo={"lanzaredes": "Mk II"},
                         equipo_estado={"telas": 30})

    def atacar(self, objetivo: heroe, base: int = 8) -> None:
        # Ataque con probabilidad de aturdir gracias a la agilidad o usar red
        if not self.esta_vivo():
            print(f"{self.alias} está fuera de combate y no puede atacar.")
            return
        dano_base = base + random.randint(0, 6)
        uso_red = False
        if self.equipo_estado.get("telas", 0) > 0 and random.random() < 0.4:
            uso_red = True
            self.equipo_estado["telas"] -= 1
            dano = dano_base + 6
            print(f"{self.alias} lanza una red a {objetivo.alias} y causa {dano} de daño (telas restantes: {self.equipo_estado['telas']}).")
        else:
            dano = dano_base
            print(f"{self.alias} golpea a {objetivo.alias} causando {dano}.")
        objetivo.recibir_dano(dano)
        # pequeño efecto del sentido arácnido: posibilidad de evitar contrataque (no modelado completamente aquí)