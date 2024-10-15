from datetime import datetime
fecha1 = datetime.strptime(input("Primera fecha (dd-mm): ") + '-2024', '%d-%m-%Y')
fecha2 = datetime.strptime(input("Segunda fecha (dd-mm): ") + '-2024', '%d-%m-%Y')

print(f"diferencia de dias: {(fecha2 - fecha1).days}")
