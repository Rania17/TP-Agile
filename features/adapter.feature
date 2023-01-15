Feature: US_01
  En tant que gestionnaire de l'agence de location
  Je veux loger les Avengers provenant d'une autre planete dans un LogementAdaptateur de mon agence

  Scenario Outline: Affecter les Avengers dans un logement
    Given un logementAdaptateur <logement>
    When je décide de loger les Avengers <les_avengers>
    Then le système met à jour le nombre d'héros dans le logementAdaptateur <nb_heros>
    Examples:
      | logement     | les_avengers     | nb_heros  |
      | logement     | les_avengers     | 3  |