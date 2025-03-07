from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

# Fungsi untuk menguji login
def test_login(username, password, expected_message):
    # Konfigurasi Firefox Options
    options = Options()
    options.add_argument('--headless')  # Menjalankan browser di mode headless
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # Inisialisasi driver Firefox menggunakan Remote WebDriver
    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        options=options
    )
    driver.get("http://localhost:3000/login.php")
    
    # Tunggu elemen tersedia
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
        driver.find_element(By.NAME, "username").send_keys(username)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.NAME, "submit").click()
        
        # Tunggu sampai URL berubah atau pesan error muncul
        WebDriverWait(driver, 10).until(
            lambda d: d.current_url != "http://localhost:3000/login.php" or expected_message in d.page_source
        )

        # Verifikasi hasil
        if expected_message in driver.page_source:
            print(f"Test login dengan username '{username}' dan password '{password}' berhasil. Pesan yang diharapkan muncul: '{expected_message}'.")
        else:
            print(f"Test login dengan username '{username}' dan password '{password}' gagal: pesan yang diharapkan tidak ditemukan.")

    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    finally:
        # Tutup driver setelah setiap pengujian
        driver.quit()

# Test cases untuk login
test_login("", "", "Data tidak boleh kosong !!")
test_login("mahak", "maha", "Register User Gagal !!")
test_login("mahak", "mahak", "index.php")
