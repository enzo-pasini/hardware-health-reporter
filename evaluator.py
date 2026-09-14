class HealthEvaluator:
    def __init__(self, limite_atencao: int = 70, limite_critico: int = 90):
        self.limite_atencao = limite_atencao
        self.limite_critico = limite_critico

    def classificar(self, valor: float) -> str:
        if valor >= self.limite_critico:
            return "CRÍTICO"
        elif valor >= self.limite_atencao:
            return "ATENÇÃO"
        return "NORMAL"

    def avaliar(self, snapshot) -> dict:
        return {
            "cpu": self.classificar(snapshot.cpu_percent),
            "ram": self.classificar(snapshot.ram_percent),
            "disco": self.classificar(snapshot.disk_percent),
        }