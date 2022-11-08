print("""
************************
Benutzer Login
************************
""")
sys_benutzer_name = "maxmeier"
sys_passwort = "12345"

benutzer_name = input ("Benutzer Name:")
passwort = input ("Passwort eingeben:")

if   (benutzer_name == sys_benutzer_name and sys_passwort != passwort):
    print("Passwort falsch")
elif (benutzer_name != sys_benutzer_name and passwort == sys_passwort):
    print("Benutzername falsch")
elif (benutzer_name != sys_benutzer_name and passwort != sys_passwort):
    print("Benutzername und Passwort falsch")
else:
    print("Sie sind erfolgreich eingeloggt")
