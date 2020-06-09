f""" pytest se usa para pruebas sencillas"""

from algoritmos import fibonacci, palindromo, factorial

def test_fibonacci():
    assert fibonacci(5) == 5

def test_palinfromo():
    assert palindromo("Anita lava la tina")

def test_factorial():
    assert factorial(5) ==120