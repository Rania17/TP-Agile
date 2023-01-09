from gestionLocation import Maison, Locataire
from behave import given, when, then, step

@given("la maison")
def step_impl(context):
    context.maison = Maison.Maison(3,25,800)
    assert context.maison is not None

@when("je demande les informations")
def step_impl(context):
    context.result = context.maison.get_loyer()

@then("j'ai en retour le loyer")
def step_impl(context):
    assert context.result == 800

@given("une maison {maison}")
def step_impl(context, maison):
    context.maison = Maison.Maison(3,25,800)
    assert context.maison is not None

@then("j'ai en retour {reponse}")
def step_impl(context, reponse):
    assert context.result == int(reponse)
