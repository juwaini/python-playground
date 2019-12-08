from dataclasses import dataclass, field, asdict, replace, astuple
from typing import List


@dataclass
class Pizza:
    crust: str
    has_cheese: bool = True
    toppings: List[str] = field(default_factory=list)

    def crust_type(self) -> str:
        return self.crust


thick_cheesy = Pizza(crust='thick')

print(thick_cheesy)
print(thick_cheesy.crust_type())
d = asdict(thick_cheesy)
print(d)

with_olives = replace(thick_cheesy, toppings=['olives'])

t = astuple(with_olives)
print(t)
