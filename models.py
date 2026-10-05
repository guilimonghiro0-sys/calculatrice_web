class Calculatrice:
    """Calculatrice avec 4 opérations et historique."""

    def __init__(self):
        self._historique = []

    def calculer(self, nombre1, operateur, nombre2):
        if operateur == "+":
            resultat = nombre1 + nombre2
        elif operateur == "-":
            resultat = nombre1 - nombre2
        elif operateur == "*":
            resultat = nombre1 * nombre2
        elif operateur == "/":
            if nombre2 == 0:
                raise ValueError("Division by zero is not allowed.")
            resultat = nombre1 / nombre2
        else:
            raise ValueError("Unknown operator.")

        self._historique.append((nombre1, operateur, nombre2, resultat))
        return resultat

    def get_historique(self):
        return list(self._historique)

    def effacer_historique(self):
        self._historique.clear()
