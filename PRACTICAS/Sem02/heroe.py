from __future__ import annotations
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Optional
import random

@dataclass
class heroe:
    nombre_real: str
    alias: str
    salud_max: int = 100
    salud_actual: int = 100
    poderes: List[str] = field(default_factory=list)
    equipo: Dict[str, str] = field(default_factory=dict)  # ej. {"traje": "Mark L", "dispositivo": "lanzaredes"}
    equipo_estado: Dict[str, int] = field(default_factory=dict)  # p. ej. carga/uso

    def __post_init__(self):
        # asegurar que la salud actual no exceda la máxima
        self.salud_actual = min(self.salud_actual, self.salud_max)

    def esta_vivo(self) -> bool:
        return self.salud_actual > 0

    def recibir_dano(self, cantidad: int) -> None:
        """Aplica daño al héroe (no cae por debajo de 0)."""
        if cantidad < 0:
            raise ValueError("El daño debe ser positivo.")
        self.salud_actual = max(0, self.salud_actual - cantidad)
        print(f"{self.alias} recibe {cantidad} de daño. Salud: {self.salud_actual}/{self.salud_max}")

    def curar(self, cantidad: int) -> None:
        """Cura al héroe (no excede salud_max)."""
        if cantidad < 0:
            raise ValueError("La curación debe ser positiva.")
        self.salud_actual = min(self.salud_max, self.salud_actual + cantidad)
        print(f"{self.alias} se cura {cantidad}. Salud: {self.salud_actual}/{self.salud_max}")

    def atacar(self, objetivo: 'Heroe', base: int = 10) -> None:
        """Ataque simple: daño con variación aleatoria pequeña."""
        if not self.esta_vivo():
            print(f"{self.alias} está fuera de combate y no puede atacar.")
            return
        if not objetivo.esta_vivo():
            print(f"{objetivo.alias} ya está fuera de combate.")
            return
        variacion = random.randint(-2, 5)
        dano = max(0, base + variacion)
        print(f"{self.alias} ataca a {objetivo.alias} causando {dano}.")
        objetivo.recibir_dano(dano)

    def usar_poder(self, nombre_poder: str, objetivo: Optional['Heroe'] = None) -> None:
        """Usa un poder si lo tiene: comportamiento por defecto simple."""
        if nombre_poder not in self.poderes:
            print(f"{self.alias} no conoce el poder '{nombre_poder}'.")
            return
        # comportamiento por defecto: poder causa daño moderado al objetivo si hay uno
        if objetivo is None:
            print(f"{self.alias} usa {nombre_poder} (efecto pasivo).")
        else:
            dano = random.randint(8, 20)
            print(f"{self.alias} usa {nombre_poder} sobre {objetivo.alias} causando {dano}.")
            objetivo.recibir_dano(dano)

    def agregar_poder(self, poder: str) -> None:
        if poder not in self.poderes:
            self.poderes.append(poder)

    def __str__(self) -> str:
        return f"{self.alias} ({self.nombre_real}) - Salud: {self.salud_actual}/{self.salud_max}"

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> 'heroe':
        return cls(**data)
