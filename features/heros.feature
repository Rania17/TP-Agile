Feature: Manage heros
  En tant qu'un super heros
  Je veux savoir à quels sont les héros de mon groupe
  Afin que je puisse savoir si y a des créatures que j'aime pas

  Scenario: Checker les informations de mon groupe d'avengers
    Given le groupe d'avengers
    When je demande les informations du groupe
    Then j'ai en retour les informations

  Scenario Outline:Checker les informations d'un groupe
    Given un groupe <les_avengers>
    When je demande les informations du groupe
    Then j'ai en retour les informations <infos>
    Examples:
      | les_avengers     | infos  |
      | les_avengers     | SPIDERMAN, IRON MAN, CAPTAIN AMERICA  |