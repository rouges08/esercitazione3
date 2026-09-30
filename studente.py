class Studente:
    def __init__(self, nome, cognome, eta, citta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.citta = citta

    def __str__(self):
        return f"{self.nome} {self.cognome}, {self.eta} anni, {self.citta}"