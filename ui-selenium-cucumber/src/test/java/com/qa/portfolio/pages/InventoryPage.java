package com.qa.portfolio.pages;

import org.openqa.selenium.WebDriver;

public class InventoryPage extends BasePage {

    public InventoryPage(WebDriver driver) {
        super(driver);
    }

    public boolean isLoaded() {
        return visible(testId("title")).getText().equals("Products") && driver.getCurrentUrl().contains("inventory");
    }

    public void addToCart(String slug) {
        click(testId("add-to-cart-" + slug));
    }

    public int cartCount() {
        return Integer.parseInt(visible(testId("shopping-cart-badge")).getText());
    }
}
