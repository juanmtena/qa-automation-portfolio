@booking @negative
Feature: Casos negativos de reservas

  Background:
    * url baseUrl
    * configure headers = { Accept: 'application/json' }

  Scenario: Consultar una reserva inexistente devuelve 404
    Given path 'booking', 999999999
    When method get
    Then status 404

  Scenario: Borrar sin token devuelve 403
    Given path 'booking', 1
    When method delete
    Then status 403

  Scenario: Actualizar sin token devuelve 403
    Given path 'booking', 1
    And request read('classpath:data/booking.json')
    When method put
    Then status 403
