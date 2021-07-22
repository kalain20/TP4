from tkinter import Button, Entry, E, Label, Tk, Frame, messagebox, StringVar
from tkinter.ttk import Combobox
from utilisateur import AnnuaireUtilisateur
from erreurValidationException import ErreurValidationException
from espaceVideException import EspaceVideException
from abonnementValidationException import AbonnementValidationExecption
from datetime import date

class fenetreprincipal(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x250")
        self.title("BIENVENUE SUR ULFLIX")
        self.resizable(False, False)
        self.config(bg="black")
        label_Message_bienvenue = Label(self, text="Bienvenue sur ULFLix", font=("Arial", 15, "bold"), fg="red",
                                        padx=45, pady=50, bg="black")
        btn_inscription = Button(self, text='Creer un compte', padx=10, pady=10, font=("Arial", 10, "bold"), fg="red",
                                 bg="black", command=self.appeler_fenetre_inscription)
        btn_connexion = Button(self, text='Connectez-vous', padx=10, pady=10, font=("Arial", 10, "bold"), fg="red",
                               bg="black", command=self.appeler_fenetre_connexion)

        label_Message_bienvenue.grid(row=0, column=0, columnspan=2)
        btn_inscription.grid(row=1, column=0)
        btn_connexion.grid(row=1, column=1)
        self.grid()

    def appeler_fenetre_connexion(self):
        fenetre_connexion()

    def appeler_fenetre_inscription(self):
        fenetre_inscription()


class fenetre_connexion(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("580x300")
        self.cadre_fenetre_connexion_frame = Frame(self, bg="black")
        self.title("Connexion")
        self.resizable(False, False)
        self.config(bg="black")
        self.creer_composants_connexion()

    def creer_composants_connexion(self):
        self.label_titre_connexion = Label(self.cadre_fenetre_connexion_frame, text="Content de vous revoir !",
                                           font=("Arial", 10, "bold"), fg="red", padx=180, pady=50, bg="black")
        self.label_email = Label(self.cadre_fenetre_connexion_frame, text="Email: ", font=("Arial", 10, "bold"),
                                 fg="red", bg="black")
        self.entry_email = Entry(self.cadre_fenetre_connexion_frame)
        self.label_mot_de_passe = Label(self.cadre_fenetre_connexion_frame, text="Mot de passe: ",
                                        font=("Arial", 10, "bold"),
                                        fg="red", bg="black")
        self.entry_mot_de_passe = Entry(self.cadre_fenetre_connexion_frame, show="*")
        self.btn_connexion_fenetre_connexion = Button(self.cadre_fenetre_connexion_frame, text="Se connecter",
                                                      font=("Arial", 10, "bold"), fg="red", bg="black", pady=5,
                                                      command=self.gerer_connexion_utilisateur)
        self.label_lien_inscription = Label(self.cadre_fenetre_connexion_frame,
                                            text="Pas encore de compte? Cliquez ici pour créer un",
                                            font=("Arial", 10, "bold"), fg="blue", bg="black")

        self.label_titre_connexion.grid(row=0, column=0, columnspan=2)
        self.label_email.grid(row=1, column=0, sticky=E)
        self.entry_email.grid(row=1, column=1, columnspan=3)
        self.label_mot_de_passe.grid(row=2, column=0, sticky=E)
        self.entry_mot_de_passe.grid(row=2, column=1, columnspan=3)
        self.btn_connexion_fenetre_connexion.grid(row=3, column=0, columnspan=3, pady=20)
        self.label_lien_inscription.grid(row=4, column=0, columnspan=2)

        self.cadre_fenetre_connexion_frame.grid(row=0, column=0)

    def gerer_connexion_utilisateur(self):
        annuaireUtilisateur = AnnuaireUtilisateur("ulflix-utilisateurs.txt")
        try:
            utilsateur = annuaireUtilisateur.authentifier(self.entry_email.get(), self.entry_mot_de_passe.get())
        except ErreurValidationException as e:
            messagebox.showerror("Erreur de validation", e, parent=self)
        else:
            tableau_de_bord()


class fenetre_inscription(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x300")
        self.cadre_fenetre_inscription_frame = Frame(self, bg="black")
        self.title("Création de compte")
        self.resizable(False, False)
        self.config(bg="black")
        self.creer_composant_inscription()

    def creer_composant_inscription(self):
        self.label_titre_inscription = Label(self.cadre_fenetre_inscription_frame,
                                             text="Créer votre compte ULFlix en seulement quelques minutes.",
                                             font=("Arial", 15, "bold"), fg="red", bg="black")
        self.label_nom_inscription = Label(self.cadre_fenetre_inscription_frame, text="Nom:",
                                           font=("Arial", 10, "bold"), fg="red", bg="black")
        self.label_email_inscription = Label(self.cadre_fenetre_inscription_frame, text="Email:",
                                             font=("Arial", 10, "bold"), fg="red", bg="black")
        self.label_mot_de_passe_inscription = Label(self.cadre_fenetre_inscription_frame, text="Mot de passe:",
                                                    font=("Arial", 10, "bold"), fg="red", bg="black")

        self.label_annee_de_naissance = Label(self.cadre_fenetre_inscription_frame, text="Année de naissance:",
                                              font=("Arial", 10, "bold"), fg="red", bg="black")
        self.label_pays = Label(self.cadre_fenetre_inscription_frame, text="Pays :", font=("Arial", 10, "bold"),
                                fg="red", bg="black")
        self.label_abonnement = Label(self.cadre_fenetre_inscription_frame, text="Abonnement:",
                                      font=("Arial", 10, "bold"), fg="red", bg="black")

        self.btn_inscription_fenetre_inscription = Button(self.cadre_fenetre_inscription_frame, padx=10, pady=5,
                                                          text="Créer un compte",
                                                          font=("Arial", 10, "bold"), fg="red", bg="black",
                                                          command=self.gerer_inscription_utilisateur)

        self.label_lien_inscription = Label(self.cadre_fenetre_inscription_frame,
                                            text="Avez-vous déjà un compte? Cliquez ici pour vous connecter",
                                            font=("Arial", 10, "bold"), fg="blue", bg="black")

        self.entry_nom_inscription = Entry(self.cadre_fenetre_inscription_frame)
        self.entry_email_inscription = Entry(self.cadre_fenetre_inscription_frame)
        self.entry_mot_de_passe_inscription = Entry(self.cadre_fenetre_inscription_frame, show="*")

        value_annee = StringVar()
        self.combobox_annee_de_naissance = Combobox(self.cadre_fenetre_inscription_frame, width=17,
                                                    textvariable=value_annee,
                                                    font=("Arial", 8, "bold"), state="readonly")
        value_pays = StringVar()

        self.combobox_pays = Combobox(self.cadre_fenetre_inscription_frame, width=17, textvariable=value_pays,
                                      font=("Arial", 8, "bold"), state="readonly")

        value_abonnement = StringVar()
        self.combobox_abonnement = Combobox(self.cadre_fenetre_inscription_frame, width=17,
                                            textvariable=value_abonnement,
                                            font=("Arial", 8, "bold"), state="readonly")

        self.combobox_annee_de_naissance['values'] = self.definir_annee()
        self.combobox_pays['values'] = self.lire_fichier("pays.txt")
        self.combobox_abonnement['values'] = self.lire_fichier("abonnement.txt")

        self.label_titre_inscription.grid(row=0, column=0, columnspan=3, padx=20, pady=30)
        self.label_nom_inscription.grid(row=1, column=0, sticky=E)
        self.label_email_inscription.grid(row=2, column=0, sticky=E)
        self.label_mot_de_passe_inscription.grid(row=3, column=0, sticky=E)

        self.entry_nom_inscription.grid(row=1, column=1)
        self.entry_email_inscription.grid(row=2, column=1)
        self.entry_mot_de_passe_inscription.grid(row=3, column=1)

        self.label_annee_de_naissance.grid(row=4, column=0, sticky=E)
        self.label_pays.grid(row=5, column=0, sticky=E)
        self.label_abonnement.grid(row=6, column=0, sticky=E)

        self.combobox_annee_de_naissance.grid(row=4, column=1)
        self.combobox_pays.grid(row=5, column=1)
        self.combobox_abonnement.grid(row=6, column=1)

        self.btn_inscription_fenetre_inscription.grid(row=7, column=0, columnspan=3, pady=10)

        self.label_lien_inscription.grid(row=8, column=0, columnspan=3, padx=50)

        self.combobox_annee_de_naissance.current(0)
        self.combobox_pays.current(0)
        self.combobox_abonnement.current(0)
        self.cadre_fenetre_inscription_frame.grid(row=0, column=0)

    def definir_annee(self):
        liste_annee = []
        for annee in range(1900, 2022):
            liste_annee.append(annee)
        return liste_annee

    def lire_fichier(self, nom_fichier):
        liste_pays = []
        with open(nom_fichier, encoding="utf-8") as fichier:
            for pays in fichier:
                liste_pays.append(pays.strip())
        return liste_pays

    def gerer_inscription_utilisateur(self):
        annuaireUtilisateur = AnnuaireUtilisateur('ulflix-utilisateurs.txt')

        try:
            utilisateur = annuaireUtilisateur.inscrire(self.entry_nom_inscription.get(),
                                                       self.entry_email_inscription.get(),
                                                       date.today().year - int(self.combobox_annee_de_naissance.get()),
                                                       self.combobox_pays.get(),
                                                       self.combobox_abonnement.get(),
                                                       self.entry_mot_de_passe_inscription.get())
        except AbonnementValidationExecption as e:
            messagebox.showerror("Erreur de validation", e, parent=self)
        except EspaceVideException as e:
            messagebox.showerror("Erreur de validation", e, parent=self)

        else:
            messagebox.showinfo("Bienvenue " +utilisateur.nom, "Informative message")



class tableau_de_bord(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x300")
        self.cadre_fenetre_inscription_frame = Frame(self, bg="black")
        self.title("Création de compte")
        self.resizable(False, False)
        self.config(bg="black")


if __name__ == '__main__':
    f = fenetreprincipal()
    f.mainloop()
