# locators used in tests

main_page_adress = "https://magento.softwaretestingboard.com/"
register_firstname_id = '//input[@id="firstname"]'
register_lastname_id = '//input[@id="lastname"]'
register_mail_id = '//input[@id="email_address"]'
register_password_id = '//input[@id="password"]'
register_password_confirmation_id = '//input[@id="password-confirmation"]'
main_page_welcome_message_id = "/html/body/div[1]/header/div[1]/div/ul/li[1]/span"
main_page_sign_in_button_id = '//a[contains(text(), "Sign In")]'
main_page_create_account_button_id = "/html/body/div[1]/header/div[1]/div/ul/li[3]/a"
sign_in_page_mail_id = '//*[@id="email"]'
sign_in_page_password_id = '//*[@id="pass"]'
create_account_firstname_error_id = '//*[@id="firstname-error"]'
create_account_lastname_error_id = '//*[@id="lastname-error"]'
create_account_mail_error_id = '//*[@id="email_address-error"]'
create_account_password_error_id = '//*[@id="password-error"]'
create_account_repeat_password_error_id = '//*[@id="password-confirmation-error"]'
create_account_password_strength_meter_label_id = (
    '//*[@id="password-strength-meter-label"]'
)
account_page_submit_button_id = '//button[@type="submit"][@title="Create an Account"]'
create_account_mail__already_existing_id = (
    '//*[@id="maincontent"]/div[2]/div[2]/div/div/div'
)
sign_in_page_sign_in_button_id = '//*[@id="send2"]/span'
main_page_account_options_expand_id = (
    "/html/body/div[1]/header/div[1]/div/ul/li[2]/span/button"
)
main_page_account_options_expanded_open_account_data_id = (
    "/html/body/div[1]/header/div[1]/div/ul/li[2]/div/ul/li[1]/a"
)
create_account_page_title = "Create New Customer Account"
sign_in_page_title = "Customer Login"
account_page_shipping_adress_id = '//*[@data-ui-id="default-shipping-edit-link"]'
main_page_mini_cart_expand_id = '//*[@id="mini-cart"]/li[1]/div/div/div[3]/div[2]/a'
main_page_mini_cart_clean_cart_button_id = (
    "/html/body/div[3]/aside[2]/div[2]/footer/button[2]"
)
delivery_page_firstname_id = '//*[@id="firstname"]'
delivery_page_lastname_id = '//*[@id="lastname"]'
delivery_page_telephone_id = '//*[@id="telephone"]'
delivery_page_street_id = '//*[@id="street_1"]'
delivery_page_city_id = '//*[@id="city"]'
delivery_page_region_id = '//*[@id="region_id"]'
delivery_page_zip_code_id = '//*[@id="zip"]'
delivery_page_country_id = '//*[@id="country"]'
delivery_page_save_adress_button_id = '//*[@title="Save Address"]'
delivery_page_firstname_error_id = '//*[@id="firstname-error"]'
delivery_page_lastname_error_id = '//*[@id="lastname-error"]'
delivery_page_telephone_error_id = '//*[@id="telephone-error"]'
delivery_page_street_error_id = '//*[@id="street_1-error"]'
delivery_page_city_error_id = '//*[@id="city-error"]'
open_cart_button_id = '//*[@class="action showcart"]'
cart_content_no_content = '//*[@id="minicart-content-wrapper"]/div[2]/strong'
cart_content_content_number = "/html/body/div[1]/header/div[2]/div[1]/a/span[2]/span[1]"
account_page_go_to_acc_page_id = '//*[@id="block-collapsible-nav"]/ul/li[7]/a'
account_information_page_title = "Account Information"
account_information_page_change_email_id = '//*[@id="change-email"]'
account_information_page_change_mail_password_id = (
    '//span[@data-title="change-email-password"]'
)
account_information_page_change_password_id = '//*[@id="change-password"]'
main_page_gear_menu_expand_id = '//*[@id="ui-id-6"]'
main_page_gear_menu_expanded_bags_id = '//*[@id="ui-id-25"]'
gear_bags_page_title = "Bags - Gear"
gear_bags_page_item_counter_id = '//*[@id="toolbar-amount"]/span[3]'
gear_bags_page_any_item_id = '//a[@class="product-item-link"]'
gear_bags_page_next_page_button_id = (
    '//*[@id="maincontent"]/div[3]/div[1]/div[4]/div[2]/ul/li[2]/a'
)
