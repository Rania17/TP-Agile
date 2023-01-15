from superHeros import Heros, Avengers
from gestionLocation import Maison
from designPatterns import LogementAdaptateur
from behave import given, when, then


@given("un logementAdaptateur {logement}")
def step_impl(context, logement):
    logement = LogementAdaptateur.LogementAdaptateur("Mars")
    context.logement = logement
    assert context.logement is not None

@when("je décide de loger les Avengers {les_avengers}")
def step_impl(context, les_avengers):
    spiderman = Heros.Heros("SPIDERMAN", "2.20m", "Agile et adhère aux murs", "Toiles d'araignée")
    iron_man = Heros.Heros("IRON MAN", "5.20m", "Voler, tirer des missiles", "Armure")
    captain_america = Heros.Heros("CAPTAIN AMERICA", "4.20m", "Super soldat", "Sérum militaire")
    les_avengers = Avengers.Avengers("Les avengers!")
    les_avengers.ajouter_heros(spiderman)
    les_avengers.ajouter_heros(iron_man)
    les_avengers.ajouter_heros(captain_america)
    context.les_avengers = les_avengers

    maison = Maison.Maison(4, 200, 5000)

    context.logement.loger_avengers(les_avengers,maison)
    context.result = context.logement.get_nb_heros()

@then("le système met à jour le nombre d'héros dans le logementAdaptateur {nb_heros}")
def step_impl(context, nb_heros):
    assert context.result == int(nb_heros)