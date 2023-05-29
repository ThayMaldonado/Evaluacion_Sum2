import subprocess
import datetime

# Obtener la hora actual
current_hour = datetime.datetime.now().hour

# Calcular el rango de tiempo objetivo
start_hour = (current_hour - 1) % 24
end_hour = current_hour % 24

# Ejecutar el comando para obtener los intentos fallidos de inicio de sesión
command = f'grep "Failed password" /var/log/auth.log | grep "sshd" | awk \'$0 >= "May 29 {start_hour}:00:00" && $0 <= "May 29 {end_hour}:59:59"\''
process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, error = process.communicate()

# Contar los intentos fallidos de inicio de sesión
failed_attempts = output.decode().count('\n')

# Imprimir el resultado
print(f"La cantidad total de intentos fallidos de inicio de sesión en la última hora cerrada es: {failed_attempts}")

