package runner;

import static org.junit.jupiter.api.Assertions.assertEquals;

import com.intuit.karate.Results;
import com.intuit.karate.Runner;
import org.junit.jupiter.api.Test;

class KarateRunnerTest {

    @Test
    void runAll() {
        Results results = Runner.path("classpath:features").tags("~@ignore").parallel(2);
        assertEquals(0, results.getFailCount(), results.getErrorMessages());
    }
}
