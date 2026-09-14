import psutil
from datetime import datetime
from snapshot import Snapshot

class HardwareCollector:
    def collect(self) -> Snapshot:
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return Snapshot(cpu, ram, disk, timestamp)