from dataclasses import dataclass, field

@dataclass
class Item:
    itemNumber: int
    name: str
    type: str
    salePrice: float | None = None
    winnerId: int | None = None

    def to_dict(self) -> dict:
        return {
            "itemNumber": self.itemNumber,
            "name": self.name,
            "type": self.type,
            "salePrice": self.salePrice,
            "winnerId": self.winnerId
        }