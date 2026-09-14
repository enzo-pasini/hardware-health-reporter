def imprimir_relatorio(snapshot, avaliacao: dict):
    print(f"\n=== Relatório — {snapshot.timestamp} ===")
    print(f"CPU:   {snapshot.cpu_percent}%  -> {avaliacao['cpu']}")
    print(f"RAM:   {snapshot.ram_percent}%  -> {avaliacao['ram']}")
    print(f"Disco: {snapshot.disk_percent}%  -> {avaliacao['disco']}")