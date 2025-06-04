from datetime import datetime, date

def hora_valida(hora_str):
    try:
        hora = datetime.strptime(hora_str, "%H:%M").time()
        if 0 <= hora.hour < 24 and 0 <= hora.minute < 60:
            return True
        else:
            return False
    except ValueError:
        return False
