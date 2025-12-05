from dataclasses import dataclass, field
from datetime import datetime
from typing import List

@dataclass
class MeterReading:
    timestamp: datetime
    kwh: float

@dataclass
class Building:
    name: str
    meter_readings: List[MeterReading] = field(default_factory=list)

    def add_reading(self, reading: MeterReading):
        self.meter_readings.append(reading)

    def calculate_total_consumption(self):
        return sum(r.kwh for r in self.meter_readings)

    def generate_report(self):
        values = [r.kwh for r in self.meter_readings]

        if not values:
            return {"building": self.name, "total": 0, "mean": 0, "min": 0, "max": 0}

        return {
            "building": self.name,
            "total": sum(values),
            "mean": sum(values)/len(values),
            "min": min(values),
            "max": max(values)
        }

class BuildingManager:
    def __init__(self):
        self.buildings = {}

    def add_from_dataframe(self, df):
        for _, row in df.iterrows():
            b = row["building"]
            if b not in self.buildings:
                self.buildings[b] = Building(b)

            self.buildings[b].add_reading(
                MeterReading(row["timestamp"], float(row["kwh"]))
            )

    def summary(self):
        return [b.generate_report() for b in self.buildings.values()]
