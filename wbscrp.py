import tkinter as tk
from tkinter import messagebox, filedialog
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Function to show the signature in a message box
def show_signature():
    signature = (
        "------------------------------------------------\n"
        "Job Application Automation by Erdem Yildiz\n"
        "All Rights Reserved © 2024\n"
        "LinkedIn    : https://www.linkedin.com/in/erdem-yildiz\n"
        "GitHub      : https://github.com/erdemyildiz35?tab=repositories\n"
        "------------------------------------------------"
    )
    messagebox.showinfo("Signature", signature)

# Function for LinkedIn login
def linkedin_login(driver, username, password):
    driver.get('https://www.linkedin.com/login')
    email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username')))
    email_input.send_keys(username)
    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys(password)
    sign_in_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    sign_in_button.click()

# Function for Xing login
def xing_login(driver, username, password):
    driver.get('https://login.xing.com/')
    email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username')))
    email_input.send_keys(username)
    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys(password)
    sign_in_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    sign_in_button.click()

# Function to search and apply on LinkedIn
def search_and_apply_linkedin(driver, job_title, location, cv_path):
    driver.get('https://www.linkedin.com/jobs/')
    job_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@aria-label="Search by title, skill, or company"]'))
    )
    job_input.send_keys(job_title)
    location_input = driver.find_element(By.XPATH, '//input[@aria-label="City, state, or zip code"]')
    location_input.clear()
    location_input.send_keys(location)
    location_input.send_keys(Keys.RETURN)

    # Code to upload CV can be added here
    # Example: driver.find_element(By.XPATH, '<CV upload button XPATH>').send_keys(cv_path)

# Function to search and apply on Xing
def search_and_apply_xing(driver, job_title, location, cv_path):
    driver.get('https://www.xing.com/jobs')
    job_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@id="search-bar-keyword"]'))
    )
    job_input.send_keys(job_title)
    location_input = driver.find_element(By.XPATH, '//input[@id="search-bar-location"]')
    location_input.clear()
    location_input.send_keys(location)
    location_input.send_keys(Keys.RETURN)

    # Code to upload CV for Xing applications can be added here
    # Example: driver.find_element(By.XPATH, '<CV upload button XPATH>').send_keys(cv_path)

# Function to select CV file
def select_cv_file():
    file_path = filedialog.askopenfilename(title="Select Your CV File", filetypes=[("PDF files", "*.pdf"), ("Word files", "*.docx")])
    if file_path:
        cv_path_entry.delete(0, tk.END)
        cv_path_entry.insert(0, file_path)

# Function to start the bot
def start_bot():
    linkedin_username = linkedin_username_entry.get()
    linkedin_password = linkedin_password_entry.get()
    xing_username = xing_username_entry.get()
    xing_password = xing_password_entry.get()
    job_title = job_title_entry.get()
    location = location_entry.get()
    cv_path = cv_path_entry.get()

    if not (linkedin_username and linkedin_password and xing_username and xing_password and job_title and location and cv_path):
        messagebox.showerror("Incomplete Information", "Please fill in all fields!")
        return

    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # LinkedIn login and application
        linkedin_login(driver, linkedin_username, linkedin_password)
        search_and_apply_linkedin(driver, job_title, location, cv_path)

        # Xing login and application
        xing_login(driver, xing_username, xing_password)
        search_and_apply_xing(driver, job_title, location, cv_path)

        messagebox.showinfo("Completed", "Application process completed successfully.")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
    finally:
        driver.quit()

# Create Tkinter GUI
root = tk.Tk()
root.title("Job Application Bot for LinkedIn and Xing")

# Show the signature when the program starts
show_signature()

# LinkedIn Login Information
tk.Label(root, text="LinkedIn Username (Email):").grid(row=0, column=0, padx=10, pady=5)
linkedin_username_entry = tk.Entry(root, width=30)
linkedin_username_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="LinkedIn Password:").grid(row=1, column=0, padx=10, pady=5)
linkedin_password_entry = tk.Entry(root, show="*", width=30)
linkedin_password_entry.grid(row=1, column=1, padx=10, pady=5)

# Xing Login Information
tk.Label(root, text="Xing Username (Email):").grid(row=2, column=0, padx=10, pady=5)
xing_username_entry = tk.Entry(root, width=30)
xing_username_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Xing Password:").grid(row=3, column=0, padx=10, pady=5)
xing_password_entry = tk.Entry(root, show="*", width=30)
xing_password_entry.grid(row=3, column=1, padx=10, pady=5)

# Job Information and CV File
tk.Label(root, text="Job Title:").grid(row=4, column=0, padx=10, pady=5)
job_title_entry = tk.Entry(root, width=30)
job_title_entry.grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="Location:").grid(row=5, column=0, padx=10, pady=5)
location_entry = tk.Entry(root, width=30)
location_entry.grid(row=5, column=1, padx=10, pady=5)

tk.Label(root, text="CV File:").grid(row=6, column=0, padx=10, pady=5)
cv_path_entry = tk.Entry(root, width=30)
cv_path_entry.grid(row=6, column=1, padx=10, pady=5)
cv_browse_button = tk.Button(root, text="Browse", command=select_cv_file)
cv_browse_button.grid(row=6, column=2, padx=10, pady=5)

# Start Button
start_button = tk.Button(root, text="Start", command=start_bot)
start_button.grid(row=7, column=0, columnspan=3, pady=10)

# Run the Tkinter event loop
root.mainloop()
