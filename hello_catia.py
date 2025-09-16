# hello_catia.py
import win32com.client as win32

try:
    catia = win32.Dispatch("Catia.Application")
    catia.Visible = True
    doc = catia.Documents.Add("Part")
    print("Hello CAD Automation! Part created.")
except Exception as e:
    print("ERROR connecting to CATIA:", e)
