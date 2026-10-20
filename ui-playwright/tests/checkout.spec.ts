import { test } from './fixtures';

test.describe('Compra', () => {
  test.beforeEach(async ({ loginPage, inventoryPage }) => {
    await loginPage.goto();
    await loginPage.login('standard_user', 'secret_sauce');
    await inventoryPage.expectLoaded();
  });

  test('flujo completo de compra de un producto', async ({ inventoryPage, checkoutPage }) => {
    await inventoryPage.addToCart('sauce-labs-backpack');
    await inventoryPage.expectCartCount(1);
    await inventoryPage.openCart();
    await checkoutPage.start();
    await checkoutPage.fillInfo('Ana', 'García', '41001');
    await checkoutPage.finish();
    await checkoutPage.expectOrderComplete();
  });

  test('el contador del carrito refleja varios productos', async ({ inventoryPage }) => {
    await inventoryPage.addToCart('sauce-labs-backpack');
    await inventoryPage.addToCart('sauce-labs-bike-light');
    await inventoryPage.expectCartCount(2);
  });
});
