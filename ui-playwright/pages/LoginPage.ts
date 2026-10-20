import { Page, expect } from '@playwright/test';

export class LoginPage {
  constructor(private readonly page: Page) {}

  async goto() {
    await this.page.goto('/');
  }

  async login(user: string, pass: string) {
    await this.page.getByTestId('username').fill(user);
    await this.page.getByTestId('password').fill(pass);
    await this.page.getByTestId('login-button').click();
  }

  async expectError(text: string | RegExp) {
    await expect(this.page.getByTestId('error')).toContainText(text);
  }
}
