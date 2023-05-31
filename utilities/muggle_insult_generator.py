import requests
import re

def get_insult():
    response = requests.get(f"https://evilinsult.com/generate_insult.php?lang=en&type=json")
    if response.status_code == 200:
        print("Success!")
        return response.json()["insult"]
    else:
        print(f"Error: {response.status_code}")


def make_muggle_insult():
    insult = get_insult()
    upper_case_name_matches = ["Satan"]
    upper_case_singular_matches = ["You're", "Your", "You"]
    lower_case_singular_matches = ["you're", "you"]
    lower_case_possessive_matches = ["your"]
    lower_case_plural_matches = ["yourself"]

    for keyword in upper_case_name_matches:
        insult = re.sub(rf"\b{re.escape(keyword)}\b", "Dumbledore", insult)

    for keyword in upper_case_singular_matches:
        insult = re.sub(rf"\b{re.escape(keyword)}\b", "Muggles", insult)

    for keyword in lower_case_singular_matches:
        insult = re.sub(rf"\b{re.escape(keyword)}\b", "muggles", insult)
        
    for keyword in lower_case_possessive_matches:
        insult = re.sub(rf"\b{re.escape(keyword)}\b", "their", insult)

    for keyword in lower_case_plural_matches:
        insult = re.sub(rf"\b{re.escape(keyword)}\b", "themselves", insult)

    if ("muggles" not in insult) | ("Muggles" not in insult):
        print("Error: Insult does not contain the word 'muggles' or 'Muggles', trying again...")
        return make_muggle_insult()
    
    return insult
