@ui @login
Feature: Login en SauceDemo

  Background:
    Given Estoy en la página de inicio de sesión

  @smoke
  Scenario: Usuario válido accede al catálogo
    When Inicio sesión con "standard_user" y "secret_sauce"
    Then Debería ver la página de productos

  Scenario Outline: Credenciales inválidas muestran error
    When Inicio sesión con "<user>" y "<password>"
    Then Debería ver el mensaje de error que contiene "<error>"

    Examples:
      | user            | password     | error                |
      | locked_out_user | secret_sauce | locked out           |
      | standard_user   | wrong        | do not match         |
      |                 | secret_sauce | Username is required |
      | standard_user   |              | Password is required |
