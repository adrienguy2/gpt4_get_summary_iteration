text = """
    """

def build_prompt(text):
    prompt = f"""
        Voici un texte que je veux que tu résume :

        {text}

        ********************

        Consignes pour remplir cette tâche:
        - Tu dois relever toutes les informations importantes de chaque text en revenant à la ligne a chaque information
        - La sortie que tu me donnes doit être une liste à tirets, bien formattée
        - Utilise des termes simple et des abréviations qui permettent de lire rapidement sans déformer le sens du texte original

        Maintenant, procède :
    """
    return prompt