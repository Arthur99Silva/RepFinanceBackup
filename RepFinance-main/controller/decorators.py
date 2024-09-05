# decorators.py
def handle_exceptions_and_logging(func):
    def wrapper(*args, **kwargs):
        try:
            print(f"Executando {func.__name__} com args={args}, kwargs={kwargs}")
            result = func(*args, **kwargs)
            print(f"{func.__name__} executado com sucesso")
            return result
        except Exception as e:
            print(f"Erro ao executar {func.__name__}: {e}")
            return None
    return wrapper
