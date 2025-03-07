from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Inisialisasi driver Firefox
driver = webdriver.Firefox()  # Pastikan path ke GeckoDriver sudah diatur di PATH
driver.get("http://localhost:3000")

# Fungsi untuk menguji pendaftaran
def test_register(username, name, email, password, repassword, expected_message):
    driver.get("http://localhost:3000/register.php")
    
    # Tunggu elemen tersedia
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
    
    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "name").send_keys(name)
    driver.find_element(By.NAME, "email").send_keys(email)
    driver.find_element(By.NAME, "password").send_keys(password)
    
    # Gunakan nama elemen yang benar untuk konfirmasi password
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "repassword")))
    
    driver.find_element(By.NAME, "repassword").send_keys(repassword)
    driver.find_element(By.NAME, "submit").click()
    time.sleep(2)  # Tunggu sebentar untuk hasil

    # Verifikasi hasil
    if expected_message in driver.page_source:
        print(f"Test register with {username} passed.")
    else:
        print(f"Test register with {username} failed.")

# Test cases untuk pendaftaran
test_register("testuser", "Test User", "test@example.com", "test123", "test123", "index.php")
test_register("irul", "Irul", "irul@irul.com", "test123", "test123", "Username sudah terdaftar !!")
test_register("newuser", "New User", "new@example.com", "test123", "test321", "Password tidak sama !!")
test_register("", "", "", "", "", "Data tidak boleh kosong !!")



# Tutup driver
driver.quit()