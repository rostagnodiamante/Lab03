import csv
from operator import itemgetter


class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.nome=nome
        self.responsabile=responsabile
        self.deposito={}
        self.prestiti={}
        self.contatore_prestiti=0

    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        try:
            file=open(file_path, "r", encoding="utf-8")
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
        for codice in self.deposito:
            num=int(codice[1:])
            if num > max_id:
                max_id=num
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
        lista_ordinata=sorted(lista_strumenti, key=itemgetter("marca"))
        return lista_ordinata

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""

        if id_strumento not in self.deposito:
            return Exception("Lo strumento non è del deposito")

        if self.deposito[id_strumento]["prestito"]:
            return Exception("Strumento già in prestito")

        for p in self.prestiti.values():
            if p["data"] == data and p["strumento"] == id_strumento and p["cognome"] == cognome_allievo:
                return Exception("Lo strumento è già in prestito")

            self.contatore_prestiti =+1
            id_prestito= f"P{self.contatore_prestiti}"

            self.prestiti[id_prestito]={
                "codiceP": id_prestito,
                "data": data,
                "strumento": id_strumento,
                "cognome": cognome_allievo
            }
            self.deposito[id_strumento]["prestito"]=True
            return self.prestiti[id_prestito]



    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        if id_prestito not in self.prestiti:
            return Exception("ID non trovato")

        id_strumento=self.prestiti[id_prestito]["strumento"]
        if id_strumento in self.deposito:
            self.deposito[id_strumento]["prestito"]=False

        self.prestiti.pop(id_prestito)
