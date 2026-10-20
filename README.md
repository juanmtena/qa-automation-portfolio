# QA Automation Portfolio

[![CI](https://github.com/juanmtena/qa-automation-portfolio/actions/workflows/ci.yml/badge.svg)](https://github.com/juanmtena/qa-automation-portfolio/actions/workflows/ci.yml)

Proyectos de automatización de pruebas sobre aplicaciones públicas, ejecutados en CI en cada push.

| Módulo | Stack | Qué demuestra | Sistema bajo prueba |
|---|---|---|---|
| `ui-playwright` | TypeScript, Playwright | Page Object Model, fixtures, tests parametrizados, trazas y capturas | [SauceDemo](https://www.saucedemo.com) |
| `ui-selenium-cucumber` | Java 17, Selenium 4, Cucumber, JUnit 5 | BDD con Gherkin, POM, esperas explícitas, captura en fallos | [SauceDemo](https://www.saucedemo.com) |
| `api-karate` | Karate | CRUD completo, auth, validación de esquema, casos negativos | [Restful-Booker](https://restful-booker.herokuapp.com) |
| `ml-healthcare-qa` | Python, pytest, scikit-learn | Calidad de datos y tests de un modelo de ocupación hospitalaria (datos **sintéticos**) | Modelo propio |

## Ejecución local

```bash
# Playwright
cd ui-playwright && npm ci && npx playwright install chromium && npx playwright test
npx playwright show-report

# Selenium + Cucumber (requiere Chrome)
cd ui-selenium-cucumber && mvn test            # -Dheadless=false para ver el navegador
# informe: target/cucumber-report.html

# Karate
cd api-karate && mvn test                      # informe: target/karate-reports/karate-summary.html

# ML sanitario
cd ml-healthcare-qa && pip install -r requirements.txt && pytest
```

## Estructura

```
.github/workflows/ci.yml   # 4 jobs en paralelo + informes como artefactos
ui-playwright/             # pages/, tests/, fixtures.ts
ui-selenium-cucumber/      # features/, pages/, steps/, support/
api-karate/                # features/{auth,booking,common}, data/
ml-healthcare-qa/          # src/ (datos y modelo), tests/
```

> Nota: no se usan datos reales de pacientes. Todo dato sanitario es sintético.
