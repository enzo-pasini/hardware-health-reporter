class Snapshot:
    def __init__(self, cpu_percent: float, ram_percent: float, disk_percent: float, timestamp: str):
        self.cpu_percent = cpu_percent
        self.ram_percent = ram_percent
        self.disk_percent = disk_percent
        self.timestamp = timestamp

    def to_dict(self) -> dict:
        return {
            "cpu_percent": self.cpu_percent,
            "ram_percent": self.ram_percent,
            "disk_percent": self.disk_percent,
            "timestamp": self.timestamp
        }