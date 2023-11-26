import time
from pages_.languageSettingsPage import LanguageSettings
from pages_.navigationBar import NavigationBar
from tests_.baseTest import BaseTestWithLogin


class LanguageSet(BaseTestWithLogin):

    def test_for_changing_language_to_spanish(self):
        navigationBarObj = NavigationBar(self.driver)
        navigationBarObj.click_on_language_changing_button()
        languageSettingsObj = LanguageSettings(self.driver)
        languageSettingsObj.select_spanish_language_button()
        languageSettingsObj.click_on_save_changes_button()
        time.sleep(3)

        self.assertEqual("ES", navigationBarObj.get_language_changing_flag_icon_text())

