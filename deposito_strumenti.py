import csv
from operator import attrgetter
class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.nome=nome
        self.responsabile=responsabile
        self.deposito={}

    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        try:
            file=open(file_path, "r", encoding="uft-8")
        except FileNotFoundError:
            return None

        lettore = csv.DictReader(file, fieldnames=["tipo", "marca", "anno", "valore"])

        for riga in lettore:
            codice=riga["codice"]
            tipo=riga["tipo"]
            marca=riga["marca"]
            anno=int(riga["anno"])
            valore=float(riga["valore"])

            ogg_strumento={
                "codice":codice,
                "tipo":tipo,
                "marca":marca,
                "anno":anno,
                "valore":valore,
                #aggiungo la voce prestito perchè la funzione nuovo_prestito mi chiede di verificar che lo strumento non sia già in prestito
                "prestito": False
            }

            self.deposito[codice]=ogg_strumento
        file.close()


    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        max_id = 0
        for codice in self.strumenti:
            num=int(codice[1:])
            if num > max_id:
                max=num
        nuovo_id=f"S{max_id + 1}"
        nuovo_oggetto={
            "codice": nuovo_id,
            "tipo": tipo,
            "marca": marca,
            "anno": anno_acquisto,
            "valore": valore,
            "prestito": False
        }
        self.deposito[nuovo_id]=nuovo_oggetto
        return nuovo_oggetto

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        lista_strumenti=list(self.deposito.values())
        lista_ordinata=sorted(lista_strumenti, key=attrgetter("marca"))
        return lista_ordinata

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""


    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        # TODO
