import random
from typing import Optional
from heroe import heroe

class IronMan(heroe):
    def __init__(self, nombre_real: str = "Tony Stark", alias: str = "Iron Man"):
        super().__init__(nombre_real=nombre_real, alias=alias,
                         salud_max=120, salud_actual=120,
                         poderes=["repulsores", "misiles", "campo energético"],
                         equipo={"traje": "Mark L", "reactor": "Arc Reactor"},
                         equipo_estado={"energia_traje": 100})

    def usar_poder(self, nombre_poder: str, objetivo: Optional[heroe] = None) -> None:
        energia = self.equipo_estado.get("energia_traje", 0)
        coste = {"repulsores": 10, "misiles": 25, "campo energético": 40}.get(nombre_poder, 5)
        if nombre_poder not in self.poderes:
            print(f"{self.alias} no tiene el poder {nombre_poder}.")
            return
        if energia < coste:
            print(f"{self.alias} no tiene energía suficiente ({energia} < {coste}) para usar {nombre_poder}.")
            return
        # consumir energía y efectuar el ataque
        self.equipo_estado["energia_traje"] = energia - coste
        dano = random.randint(coste, coste + 20)  # potencia relacionada al coste
        if objetivo:
            print(f"{self.alias} dispara {nombre_poder} a {objetivo.alias} (-{coste} energía).")
            objetivo.recibir_dano(dano)
        else:
            print(f"{self.alias} activa {nombre_poder} (-{coste} energía).")
