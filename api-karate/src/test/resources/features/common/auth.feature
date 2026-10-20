@ignore
Feature: Helper de autenticación (se invoca con call)

  Scenario: Obtener token
    Given url baseUrl
    And path 'auth'
    And request { username: '#(username)', password: '#(password)' }
    When method post
    Then status 200
    * def token = response.token
