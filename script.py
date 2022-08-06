import pytest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
from time import sleep

def test_add_todo_list():
    # Access website and access pop-up
    driver = webdriver.Chrome()
    driver.get('https://todo-list-login.firebaseapp.com/')
    driver.maximize_window()
    btn_github = driver.find_element(By.CLASS_NAME, "btn-github")
    btn_github.click()

    # Wait until new window appears and do a hardcoded sleep to load content
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    newWindow = driver.window_handles
    newNewWindow = newWindow[1]
    driver.switch_to.window(newNewWindow)
    element_present = EC.presence_of_element_located((By.CLASS_NAME, "js-login-field"))
    WebDriverWait(driver, 10).until(element_present)
    textbox_login = driver.find_element(By.CLASS_NAME, "js-login-field")
    textbox_login.send_keys("username")
    textbox_login.send_keys(Keys.ENTER)
    textbox_password = driver.find_element(By.CLASS_NAME, "js-password-field")
    textbox_password.send_keys("password")
    textbox_password.send_keys(Keys.ENTER)
    sleep(5)

    # Wait GitHub login resolves and login to main page.
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(1))
    newWindow = driver.window_handles
    newNewWindow = newWindow[0]
    driver.switch_to.window(newNewWindow)
    element_present = EC.presence_of_element_located((By.XPATH, "/html/body/ng-view/div/div[2]/div[1]/input"))
    WebDriverWait(driver, 10).until(element_present)

    # Get elements and create 10 objects
    textbox_todo = driver.find_element(By.XPATH, "/html/body/ng-view/div/div[2]/div[1]/input")
    submit_todo = driver.find_element(By.CLASS_NAME, "task-btn")
    logout_todo = driver.find_element(By.CLASS_NAME, "btn-default")
    for i in range(10):
        textbox_todo.send_keys("abcd")
        textbox_todo.send_keys(Keys.ENTER)
        submit_todo.send_keys(Keys.ENTER)
    logout_todo.send_keys(Keys.ENTER)
    sleep(1)
    driver.quit()

def test_delete_todo_list():
    # Access website and access pop-up
    driver = webdriver.Chrome()
    driver.get('https://todo-list-login.firebaseapp.com/')
    driver.maximize_window()
    btn_github = driver.find_element(By.CLASS_NAME, "btn-github")
    btn_github.click()

    # Wait until new window appears and do a hardcoded sleep to load content
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    newWindow = driver.window_handles
    newNewWindow = newWindow[1]
    driver.switch_to.window(newNewWindow)
    element_present = EC.presence_of_element_located((By.CLASS_NAME, "js-login-field"))
    WebDriverWait(driver, 10).until(element_present)
    textbox_login = driver.find_element(By.CLASS_NAME, "js-login-field")
    textbox_login.send_keys("username")
    textbox_login.send_keys(Keys.ENTER)
    textbox_password = driver.find_element(By.CLASS_NAME, "js-password-field")
    textbox_password.send_keys("password")
    textbox_password.send_keys(Keys.ENTER)
    sleep(5)

    # Delete selected tasks
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(1))
    newWindow = driver.window_handles
    newNewWindow = newWindow[0]
    driver.switch_to.window(newNewWindow)
    btn_delete = driver.find_elements(By.CLASS_NAME, "btn-danger")
    for i in range(len(btn_delete)):
        if i > 3:
            btn_delete[i].send_keys(Keys.ENTER)


    logout_todo = driver.find_element(By.CLASS_NAME, "btn-default")
    logout_todo.send_keys(Keys.ENTER)
    sleep(1)
    driver.quit()