import sympy as sp
def taylor_series(f, x, a, N):
    """
    Calcula la aproximación de Taylor de la función f(x) alrededor del punto a hasta el orden N.

    :param f: Función a aproximar
    :param x: Variable independiente
    :param a: Punto de expansión
    :param N: Orden de la aproximación de Taylor
    :return: Expresión de la serie de Taylor
    """
    taylor_approx = 0
    for n in range(N + 1):
        term = (f.diff(x, n).subs(x, a) / sp.factorial(n)) * (x - a)**n
        taylor_approx += term

    return taylor_approx
x = sp.symbols('x')
func_str = input("Ingrese la función en términos de x (por ejemplo, sin(x), exp(x), etc.): ")
f = sp.sympify(func_str)  
a = float(input("Ingrese el punto de expansión (a): "))
N = int(input("Ingrese el orden de la aproximación de Taylor (N): "))
taylor_approx = taylor_series(f, x, a, N)
print(f"\nSerie de Taylor de {f} alrededor de {a} hasta el orden {N}:")
print(taylor_approx)