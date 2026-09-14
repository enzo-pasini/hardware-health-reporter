from collector import HardwareCollector
from evaluator import HealthEvaluator
from reporter import imprimir_relatorio
from historic import LogWriter

def main():
    coletor = HardwareCollector()
    avaliador = HealthEvaluator()
    log = LogWriter()

    snapshot = coletor.collect() # Chama a função collect() do arquivo para coletar os dados de hardware
    avaliacao = avaliador.avaliar(snapshot)

    imprimir_relatorio(snapshot, avaliacao)
    log.salvar(snapshot)

if __name__ == "__main__":
    main()