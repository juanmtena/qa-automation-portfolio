package com.qa.portfolio.pages;

import org.openqa.selenium.WebDriver;

public class LoginPage extends BasePage {

    public LoginPage(WebDriver driver) {
        super(driver);
    }

    public void open() {
        driver.get("https://www.saucedemo.com");
    }

    public void login(String user, String password) {
        type(testId("username"), user);
        type(testId("password"), password);
        click(testId("login-button"));
    }

    public String errorText() {
        return visible(testId("error")).getText();
    }
}
