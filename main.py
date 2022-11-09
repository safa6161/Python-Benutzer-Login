print("""
************************
Benutzer Login
************************
""")
sys_benutzer_name = "maxmeier"
sys_passwort = "12345"
versuche = 3

while True:
    benutzer_name = input("Benutzername:")
    passwort = input("Passwort eingeben:")
    if (benutzer_name == sys_benutzer_name and passwort != sys_passwort):
        print("Passwort falsch")
        versuche -= 1
    elif (benutzer_name != sys_benutzer_name and passwort == sys_passwort):
        print("Benutzername falsch")
        versuche -= 1
    elif (benutzer_name != sys_benutzer_name and passwort != sys_passwort):
        print("Benutzername und Passwort falsch")
        versuche -= 1
    else:
        print("Sie sind erfolgreich eingeloggt")
        break
    if (versuche == 0):
        print("Keine versuche mehr")
        break
