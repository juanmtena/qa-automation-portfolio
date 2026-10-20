@ui @cart
Feature: Carrito de la compra

  Background:
    Given Estoy en la página de inicio de sesión
    And Inicio sesión con "standard_user" y "secret_sauce"

  Scenario: Añadir productos actualiza el contador
    When Añado "sauce-labs-backpack" al carrito
    And Añado "sauce-labs-bike-light" al carrito
    Then El indicador del carrito debería mostrar 2
