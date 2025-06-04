from datetime import datetime, date

def data_valida_futura_ou_hoje(data_str):
    try:
        data = datetime.strptime(data_str, "%d/%m/%Y").date()
        hoje = date.today()
        if data >= hoje:
            return True
        else:
            return False
    except ValueError:
        return False
