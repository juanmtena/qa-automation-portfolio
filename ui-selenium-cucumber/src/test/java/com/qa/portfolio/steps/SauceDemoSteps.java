package com.qa.portfolio.steps;

import static org.assertj.core.api.Assertions.assertThat;

import com.qa.portfolio.pages.InventoryPage;
import com.qa.portfolio.pages.LoginPage;
import com.qa.portfolio.support.DriverFactory;

import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;

public class SauceDemoSteps {

    private LoginPage login() {
        return new LoginPage(DriverFactory.get());
    }

    private InventoryPage inventory() {
        return new InventoryPage(DriverFactory.get());
    }

    @Given("Estoy en la página de inicio de sesión")
    public void iAmOnTheLoginPage() {
        login().open();
    }

    @When("Inicio sesión con {string} y {string}")
    public void iLogInWith(String user, String password) {
        login().login(user, password);
    }

    @Then("Debería ver la página de productos")
    public void iShouldSeeTheProductsPage() {
        assertThat(inventory().isLoaded()).isTrue();
    }

    @Then("Debería ver el mensaje de error que contiene {string}")
    public void iShouldSeeTheErrorMessage(String text) {
        assertThat(login().errorText()).contains(text);
    }

    @When("Añado {string} al carrito")
    public void iAddToTheCart(String slug) {
        inventory().addToCart(slug);
    }

    @Then("El indicador del carrito debería mostrar {int}")
    public void theCartBadgeShouldShow(int count) {
        assertThat(inventory().cartCount()).isEqualTo(count);
    }
}
