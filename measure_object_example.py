from pymongo import MongoClient

class Measure:

    def __init__(self, name, end_use, sector, description, life_exp, primary_fuel):
        self.name = name
        self.end_use = end_use
        self.sector = self.validate_sector(sector)
        self.description = description
        self.life_exp = life_exp
        self.primary_fuel = primary_fuel

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data['name'],
            end_use=data['end_use'],
            sector=data['sector'],
            description=data['description'],
            life_exp=data['life_exp'],
            primary_fuel=data['primary_fuel']
        )

    def validate_sector(self, sector):
        if sector not in ['R', 'C', 'I']:
            raise ValueError("Invalid sector value. Acceptable values are 'R', 'C', or 'I'.")
        return sector

    def to_dict(self):
        return {
            'name': self.name,
            'end_use': self.end_use,
            'sector': self.sector,
            'description': self.description,
            'life_exp': self.life_exp,
            'primary_fuel': self.primary_fuel
        }
    
    def __str__(self):
        return f"Measure(name={self.name}, end_use={self.end_use}, sector={self.sector}, description={self.description}, life_exp={self.life_exp}, primary_fuel={self.primary_fuel})"

    