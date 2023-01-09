Feature: Manage houses
  En tant que locataire
  Je veux voir le montant de mon loyer à payer
  Afin que je puisse m'organiser dans mes dépenses

  Scenario: Checker les informations de ma maison
    Given la maison
    When je demande les informations
    Then j'ai en retour le loyer

  Scenario Outline:Checker les informations d'une maison
    Given une maison <maison>
    When je demande les informations
    Then j'ai en retour <reponse>
    Examples:
      | maison   | reponse |
      | maison1  | 800     |