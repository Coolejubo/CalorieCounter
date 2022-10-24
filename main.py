# Main.Py for a simple calorie counter.
# Developed by Huub Al.
# 23-10-2022.

# -------------------------------------------------------------------------------

# Opzet van de App.

# Voor de kolommen hoef ik er maar 1, want ik wil een overzichtelijke app,
# met de volgende rijelementen:

# 1: De Hoeveelheid calorieen van de dag. 
#       - Dit is een Label met de hoeveelheid calorieen, eiwitten, suikers en vetten.

# 2: Eten/Drinken Menu.
#       -   Je kunt dan eerder ingevoerde etenswaren van vandaag bekijken en eventueel verwijderen.
#       -   Je kunt nieuwe maaltijden invoeren, door de voedingswaarden en 
#           hoeveelheid aan te geven en deze op te slaan in de lokale database,
#       -   er is ook een mogelijkheid om extra info toe te voegen, zoals de gebruikelijke 
#           grootte van een portie of dergelijken.
#       -   Je kunt gemakkelijk een eerder gegeten maaltijd invoeren door
#           deze te selecteren in de database en de hoeveelheid aan te passen.
#       -   Je kunt elementen uit de database aanpassen en verwijderen.

# 3: CalorieHistorie.
#       - Afgelopen dagen terugkijken.


# Functies:

# - Om 12 uur snachts wordt de counter gereset.

# -------------------------------------------------------------------------------

import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager

# Hier worden de verschillende menus gedefinieerd voor de app.

# De main UI met het keuze menu.

class MainUI(Screen):
    pass

# Het MealMenuUI die het keuze menu bevat om (1) de maaltijden van vandaag te bekijken 
# en te bewerken, (2) nieuwe maaltijdgegevens invoeren in de database, 
# (3) maaltijd invoeren voor vandaag, (4) maaltijdgegevens bekijken en bewerken in de database.

class MealMenuUI(Screen):
    pass

class TodaysMeals(Screen):
    pass

class NewMeal(Screen):
    pass

class SelectMeal(Screen):
    pass

class MealDatabase(Screen):
    pass

# Scroll pagina met de maaltijden van de afgelopen 7 dagen.

class CaloricHistory(Screen):
    pass



class CalorieCounter(App):
    def build(self):
        return MainUI()

if __name__ == "__main__":
    CalorieCounter().run()
