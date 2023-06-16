import unittest
from tests_account_information import TestAccountInformation
from tests_create_new_account_page import TestAccountCreatingForm
from tests_delivery_form import TestDeliveryForm
from tests_gear_page import TestGearPage
from tests_shop_functionality import TestShopFunctionality
from tests_mainpage import TestMainpage
from tests_sign_in_page import TestSignIn


tc1 = unittest.TestLoader().loadTestsFromTestCase(TestAccountInformation)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestAccountCreatingForm)
tc3 = unittest.TestLoader().loadTestsFromTestCase(TestDeliveryForm)
tc4 = unittest.TestLoader().loadTestsFromTestCase(TestGearPage)
tc5 = unittest.TestLoader().loadTestsFromTestCase(TestShopFunctionality)
tc6 = unittest.TestLoader().loadTestsFromTestCase(TestMainpage)
tc7 = unittest.TestLoader().loadTestsFromTestCase(TestSignIn)


test_suite_new = unittest.TestSuite([tc1, tc2, tc3, tc4, tc5, tc6, tc7])
unittest.TextTestRunner().run(test_suite_new)
