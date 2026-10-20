import { test } from './fixtures';

test.describe('Login', () => {
  test.beforeEach(async ({ loginPage }) => loginPage.goto());

  test('usuario válido accede al catálogo', async ({ loginPage, inventoryPage }) => {
    await loginPage.login('standard_user', 'secret_sauce');
    await inventoryPage.expectLoaded();
  });

  test('usuario bloqueado ve mensaje de error', async ({ loginPage }) => {
    await loginPage.login('locked_out_user', 'secret_sauce');
    await loginPage.expectError('locked out');
  });

  const invalid = [
    { name: 'contraseña incorrecta', user: 'standard_user', pass: 'wrong', error: 'do not match' },
    { name: 'usuario vacío', user: '', pass: 'secret_sauce', error: 'Username is required' },
    { name: 'contraseña vacía', user: 'standard_user', pass: '', error: 'Password is required' },
  ];

  for (const c of invalid) {
    test(`credenciales inválidas: ${c.name}`, async ({ loginPage }) => {
      await loginPage.login(c.user, c.pass);
      await loginPage.expectError(c.error);
    });
  }
});
