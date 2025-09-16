# hello_catia.py
# PURPOSE: Open CATIA, show the window, and create a blank Part document.

# 1) Import the Windows COM bridge for Python (pywin32).
import win32com.client as win32

try:
    # 2) Connect to CATIA application via COM.
    catia = win32.Dispatch("Catia.Application")

    # 3) Make sure the CATIA window is visible on screen.
    catia.Visible = True

    # 4) Create a new Part document inside CATIA.
    doc = catia.Documents.Add("Part")

    # 5) Feedback in PowerShell so you know it worked.
    print("Hello CAD Automation! Part created.")

except Exception as e:
    # If something goes wrong, show the error message.
    print("ERROR connecting to CATIA:", e)

