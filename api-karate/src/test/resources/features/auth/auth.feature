@auth
Feature: Autenticación

  Background:
    * url baseUrl

  Scenario: Credenciales válidas devuelven token
    Given path 'auth'
    And request { username: '#(username)', password: '#(password)' }
    When method post
    Then status 200
    And match response == { token: '#string' }

  Scenario: Credenciales inválidas devuelven motivo
    Given path 'auth'
    And request { username: 'admin', password: 'incorrecta' }
    When method post
    Then status 200
    And match response == { reason: 'Bad credentials' }
