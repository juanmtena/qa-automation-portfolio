@booking
Feature: Ciclo de vida de una reserva

  Background:
    * url baseUrl
    * def auth = call read('classpath:features/common/auth.feature')
    * def token = auth.token
    * def payload = read('classpath:data/booking.json')
    * configure headers = { Accept: 'application/json' }

  Scenario: Crear, consultar, actualizar y borrar una reserva
    # CREATE
    Given path 'booking'
    And request payload
    When method post
    Then status 200
    And match response.bookingid == '#number'
    And match response.booking == payload
    * def id = response.bookingid

    # READ
    Given path 'booking', id
    When method get
    Then status 200
    And match response.firstname == payload.firstname

    # UPDATE
    * def updated = karate.merge(payload, { firstname: 'Actualizado', totalprice: 200 })
    Given path 'booking', id
    And header Cookie = 'token=' + token
    And request updated
    When method put
    Then status 200
    And match response.firstname == 'Actualizado'
    And match response.totalprice == 200

    # DELETE
    Given path 'booking', id
    And header Cookie = 'token=' + token
    When method delete
    Then status 201

    # VERIFY
    Given path 'booking', id
    When method get
    Then status 404

  Scenario: El listado devuelve identificadores numéricos
    Given path 'booking'
    When method get
    Then status 200
    And match each response == { bookingid: '#number' }
