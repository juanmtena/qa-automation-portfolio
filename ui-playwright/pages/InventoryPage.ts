import { Page, expect } from '@playwright/test';

export class InventoryPage {
  constructor(private readonly page: Page) {}

  async expectLoaded() {
    await expect(this.page).toHaveURL(/inventory\.html/);
    await expect(this.page.getByTestId('title')).toHaveText('Products');
  }

  async addToCart(slug: string) {
    await this.page.getByTestId(`add-to-cart-${slug}`).click();
  }

  async expectCartCount(count: number) {
    await expect(this.page.getByTestId('shopping-cart-badge')).toHaveText(String(count));
  }

  async openCart() {
    await this.page.getByTestId('shopping-cart-link').click();
  }
}
