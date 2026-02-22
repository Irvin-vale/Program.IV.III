#!/usr/bin/env python3
import sys

def compute(a: float, op: str, b: float) -> float:
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op in ("*", "x", "X"):
        return a * b
    if op in ("/", ":"):
        if b == 0:
            raise ZeroDivisionError("División por cero")
        return a / b
    if op in ("^", "**"):
        return a ** b
    if op == "%":
        if b == 0:
            raise ZeroDivisionError("Módulo por cero")
        return a % b
    raise ValueError(f"Operador no soportado: {op}")


def run_tests() -> bool:
    cases = [
        (3, "+", 4, 7),
        (5.5, "*", 2, 11.0),
        (2, "^", 8, 256),
        (5, "%", 3, 2),
        (4, "/", 2, 2),
    ]
    passed = 0
    for a, op, b, expected in cases:
        try:
            got = compute(a, op, b)
            if abs(got - expected) < 1e-9:
                passed += 1
            else:
                print(f"Fallo: {a} {op} {b} => {got} (esperado {expected})")
        except Exception as e:
            print(f"Error en {a} {op} {b}: {e}")
    print(f"Tests pasados: {passed}/{len(cases)}")
    return passed == len(cases)


def is_valid_number(s: str) -> bool:
    """Valida que el string sea un número (entero o decimal)."""
    try:
        float(s)
        return True
    except ValueError:
        return False


def repl():
    print("Calculadora Python (escribe 'salir' para terminar). Ejemplos: 3 + 4, 5.2 * 3, 2 ^ 8")
    print("SOLO se aceptan números enteros y decimales.")
    try:
        while True:
            line = input("> ").strip()
            if not line:
                continue
            if line.lower() in ("salir", "exit"):
                break

            tokens = line.split()
            if len(tokens) != 3:
                print("Entrada no válida. Formato: <número> <operador> <número>")
                continue

            a_s, op, b_s = tokens
            
            # Validación estricta: operandos deben ser números válidos
            if not is_valid_number(a_s):
                print(f"Error: '{a_s}' no es un número válido.")
                continue
            if not is_valid_number(b_s):
                print(f"Error: '{b_s}' no es un número válido.")
                continue

            try:
                a = float(a_s)
                b = float(b_s)
            except ValueError:
                print("Error: operandos no son números válidos.")
                continue 

            try:
                res = compute(a, op, b)
                if isinstance(res, float) and abs(res - round(res)) < 1e-12:
                    print(int(round(res)))
                else:
                    print(res)
            except ZeroDivisionError as zde:
                print("Error:", zde)
            except Exception as e:
                print("Error:", e)
    except (EOFError, KeyboardInterrupt):
        print("\nAdiós.")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        ok = run_tests()
        sys.exit(0 if ok else 1)
    repl()


