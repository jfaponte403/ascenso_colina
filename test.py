class NodoNario:
    def __init__(self, valor):
        self.valor = valor
        self.conexiones = []  # Lista de tuplas (nodo_hijo, peso)

    def agregar_conexion(self, hijo, peso):
        self.conexiones.append((hijo, peso))

    def __repr__(self, nivel=0):
        resultado = "  " * nivel + str(self.valor) + "\n"
        for hijo, peso in self.conexiones:
            resultado += "  " * (nivel + 1) + f"({peso}) " + hijo.__repr__(nivel + 1)
        return resultado

# Ejemplo de uso
if __name__ == "__main__":
    # Crear nodos
    raiz = NodoNario("A")
    b = NodoNario("B")
    c = NodoNario("C")
    d = NodoNario("D")
    e = NodoNario("E")
    f = NodoNario("F")

    # Construir árbol
    raiz.agregar_conexion(b, 10)
    raiz.agregar_conexion(c, 20)
    b.agregar_conexion(d, 15)
    b.agregar_conexion(e, 25)
    c.agregar_conexion(f, 30)

    # Imprimir árbol
    print("Árbol n-ario con pesos en las conexiones:")
    print(raiz)
