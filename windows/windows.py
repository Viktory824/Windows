from time import sleep

from pytest import fixture
from selenium import webdriver


@fixture
def driver():
    driver = webdriver.Chrome(executable_path='../drivers/chromedriver')
    driver.maximize_window()
    yield driver
    driver.quit()


def test_windows(driver):
    driver.get('http://beru.ru')
    main_window = driver.current_window_handle
    sleep(1)

    driver.execute_script('window.open();')
    sleep(3)

    # получить список дексрипторов всех окон
    all = driver.window_handles
    new = list(set(all).difference({driver.current_window_handle}))[0]

    sleep(3)
    driver.switch_to_window(new)
    driver.get('http://google.com')
    sleep(5)
    driver.close()


def test_tab_in_new_window(driver):
    """Открытие вкладки в новом окне

    тут больше примеров: https://www.w3schools.com/jsref/met_win_open.asp

    """
    driver.get('http://beru.ru')
    main_window = driver.current_window_handle

    js_str = '''window.open("http://google.com", "myWindow", "width=2000,height=1000");  '''

    driver.execute_script(js_str)
    all = driver.window_handles
    print(all)
    # sleep(10)
