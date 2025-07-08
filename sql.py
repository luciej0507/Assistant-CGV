from dotenv import load_dotenv
import os
import openai
import mysql.connector as mysql
from datetime import datetime


load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

def phrase_accueil():
    return f"LexiBot : Bonjour, comment puis-je vous aider ?"

def demander_au_modele_finetune(question):
    response = openai.completions.create(
        model="ft:gpt-4.1-nano-2025-04-14:jn-formation::BqylGQAA",
        messages=[
            {"role": "system", "content": "Tu es un assistant amical et spécialisé."},
            {"role": "user", "content": question}  #ce qu'on veut envoyer au modèle
        ]
    )
    return (response.choices[0].message.content)  # récupère le texte généré par le modèle et le renvoie en sortie de la fonction

def sauvegarder_echange(prompt, reponse, date, statut):
        # Connexion à la base de données
        connexion = mysql.connect(
            host='localhost',
            user='root',       
            password='example',  
            database='logs',
            port=3306          
        )

        curseur = connexion.cursor()
        requete = """
                INSERT INTO echanges (conversation, prompt, reponse, date, statut)
                VALUES (1, %s, %s, %s, %s)
            """
        valeurs = (prompt, reponse, date, statut)
        curseur.execute(requete, valeurs)
        connexion.commit()
    
        curseur.close()
        connexion.close()

sauvegarder_echange(
    prompt="Quels sont les CGV applicables aux prestations ?",
    reponse="Les CGV applicables sont celles en vigueur à la date de signature.",
    date=datetime.now(),
    statut=1
)

print(phrase_accueil())
question = input("Vous : ")
reponse = demander_au_modele_finetune(question)
print("LexiBot :", reponse)


