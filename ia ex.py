def EvaluerRegle(regle):
    NouveauxFaits = []
    if all(antecedent in Faits for antecedent in regle[0]):  
       for consequent in regle[1]:
         valeur_consequent = "Calcul de la valeur du conséquent"
         NouveauxFaits.append(consequent)
    return NouveauxFaits

    
def ChaineMixte(Faits, Regles, But):
    if But in Faits:
        return True  

    for regle in Regles:
        if all(antecedent in Faits for antecedent in regle[0]):
            NouveauxFaits = EvaluerRegle(regle)
            Faits.extend(NouveauxFaits)  
    if But in Faits:
                return True  

    else :
      return False  