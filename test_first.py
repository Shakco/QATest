import logging
import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s [%(levelname)s] %(message)s',
#     force=True,
#     datefmt='%Y-%m-%d %H:%M:%S',
#     handlers=[
#         logging.FileHandler('test.log', encoding='utf-8'),
#         logging.StreamHandler()
# ])
logger = logging.getLogger(__name__)

class TestStepik:
    def test_search(self):
        logger.info("Запуск браузера Chrome")
        driver = webdriver.Chrome()       # Открываем браузер Google Chrome
        driver.set_window_size(900, 1000) # Задаем разрешение экрана
        driver.implicitly_wait(10)        # "Задаем предельное время ожидания появления элементов на странице (10 сек)
        wait = WebDriverWait(driver, 15)

        try:
            logger.info("Открываем сайт twitch.tv")
            driver.get('https://twitch.tv/')

            logger.info("Находим поле ввода поискового запроса")
            search_input = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type="search"]'))
            )

            logger.info("Вводим слово MIRWANA")
            search_input.send_keys('MIRWANA')

            logger.info("Нажимаем Enter")
            search_input.send_keys(Keys.ENTER)

            logger.info("Получаем первый элемент из поисковой выдачи")
            first_result = wait.until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, 'strong[data-test-selector="search-result-live-channel__name"] a')
                )
            )

            logger.info(f"Найден результат: {first_result.text}")
            assert "mirwana" in first_result.text.lower()
            logger.info("Проверка пройдена!")

        except Exception as e:
            logger.exception(f"Тест упал с ошибкой: {e}")
            raise

        finally:
            logger.info("Закрываем браузер")
            driver.quit()