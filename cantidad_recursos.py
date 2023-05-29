import psutil

# Obtener la información del sistema
disk_usage = psutil.disk_usage('/')
memory_usage = psutil.virtual_memory()
cpu_usage = psutil.cpu_percent()
network_stats = psutil.net_if_stats()

# Obtener la cantidad de recursos disponibles
disk_available = disk_usage.free
memory_available = memory_usage.available
cpu_available = 100 - cpu_usage

# Obtener el nombre de las interfaces de red
network_interfaces = list(network_stats.keys())

# Imprimir el resultado
print(f"Recursos de hardware disponibles:")
print(f"Disco disponible: {disk_available} bytes")
print(f"Memoria disponible: {memory_available} bytes")
print(f"CPU disponible: {cpu_available}%")
print("Interfaces de red:")
for interface in network_interfaces:
    print(f"- {interface}")