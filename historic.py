import os
import csv
class LogWriter:
    def __init__(self, caminho: str = "historico.csv"):
        self.caminho = caminho

    def salvar(self, snapshot):
        existe = os.path.isfile(self.caminho)
        with open(self.caminho, mode="a", newline="") as arquivo:
            escritor = csv.writer(arquivo)
            if not existe:
                escritor.writerow(["timestamp", "cpu", "ram", "disco"])
            escritor.writerow([
                snapshot.timestamp,
                snapshot.cpu_percent,
                snapshot.ram_percent,
                snapshot.disk_percent,
            ])