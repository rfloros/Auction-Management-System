from dataclasses import dataclass, field

@dataclass
class Bidder:
    bidderId: int
    name: str
    itemsWon: list[int] = field(default_factory=list)
    totalOwed: float = 0.0

    def to_dict(self) -> dict:
        return {
            "bidderId": self.bidderId,
            "name": self.name,
            "itemsWon": self.itemsWon,
            "totalOwed": self.totalOwed
        }