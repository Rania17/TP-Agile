from superHeros import Heros, Avengers, Habitat
from behave import given, when, then, step

@given("le groupe d'avengers")
def step_impl(context):
    spiderman = Heros.Heros("SPIDERMAN", "2.20m", "Agile et adhère aux murs", "Toiles d'araignée")
    iron_man = Heros.Heros("IRON MAN", "5.20m", "Voler, tirer des missiles", "Armure")
    captain_america = Heros.Heros("CAPTAIN AMERICA", "4.20m", "Super soldat", "Sérum militaire")
    les_avengers = Avengers.Avengers("Les avengers!")
    les_avengers.ajouter_heros(spiderman)
    les_avengers.ajouter_heros(iron_man)
    les_avengers.ajouter_heros(captain_america)
    context.les_avengers = les_avengers
    assert context.les_avengers is not None

@when("je demande les informations du groupe")
def step_impl(context):
    Str = ""
    for heros in context.les_avengers.get_heros():
        Str = Str + heros.get_nom() + ", "
    Str = Str[:len(Str) - 2]
    context.result = Str

@then("j'ai en retour les informations")
def step_impl(context):
    assert context.result == "SPIDERMAN, IRON MAN, CAPTAIN AMERICA"

@given("un groupe {les_avengers}")
def step_impl(context, les_avengers):
    spiderman = Heros.Heros("SPIDERMAN", "2.20m", "Agile et adhère aux murs", "Toiles d'araignée")
    iron_man = Heros.Heros("IRON MAN", "5.20m", "Voler, tirer des missiles", "Armure")
    captain_america = Heros.Heros("CAPTAIN AMERICA", "4.20m", "Super soldat", "Sérum militaire")
    les_avengers = Avengers.Avengers("Les avengers!")
    les_avengers.ajouter_heros(spiderman)
    les_avengers.ajouter_heros(iron_man)
    les_avengers.ajouter_heros(captain_america)
    context.les_avengers = les_avengers
    assert context.les_avengers is not None

@then("j'ai en retour les informations {infos}")
def step_impl(context, infos):
    assert context.result == infos
