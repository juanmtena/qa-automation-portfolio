package com.qa.portfolio.support;

import io.cucumber.java.After;
import io.cucumber.java.Before;
import io.cucumber.java.Scenario;
import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;

public class Hooks {

    @Before
    public void setUp() {
        DriverFactory.start();
    }

    @After
    public void tearDown(Scenario scenario) {
        if (scenario.isFailed() && DriverFactory.get() instanceof TakesScreenshot shooter) {
            scenario.attach(shooter.getScreenshotAs(OutputType.BYTES), "image/png", "failure");
        }
        DriverFactory.quit();
    }
}
