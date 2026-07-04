from keyword_library import KeywordLibrary

def test_login_and_add_product():
    test = KeywordLibrary()

    try:
        test.OpenBrowser("https://www.saucedemo.com")
        test.InputText("user-name", "standard_user")
        test.InputText("password", "secret_sauce")
        test.ClickElement("login-button")
        test.VerifyTextPresent("Products")
        test.AddToCartByIndex(0)
        test.VerifyTextPresent("1")
    finally:
        test.CloseBrowser()