from django import template
from notification.models import Notification
register = template.Library()

@register.filter
def get_faculty(i, faculty):
    department = None
    if faculty == "dentistry":
        department = "Faculty of Dentistry"
    elif faculty == "pharmacy":
        department = "Faculty of Pharmacy"
    elif faculty == "literature":
        department = "Faculty of Literature"
    elif faculty == "educational":
        department = "Faculty of Educational Sciences"
    elif faculty == "science":
        department = "Faculty of Sciences"
    elif faculty == "arts":
        department = "Faculty of Arts"
    elif faculty == "health":
        department = "Faculty of Health Sciences"
    elif faculty == "seas":
        department = "School of Economics and Administrative Sciences"
    elif faculty == "engineering":
        department = "Faculty of Engineering"
    elif faculty == "medical":
        department = "Medial Faculty"
    elif faculty == "law":
        department = "Faculty of Law"
    else:
        department = "Faculty doesn't defined!"

    return department

@register.filter
def get_contact(i, contact):
    contactType = None
    if contact == "wPhone":
        contactType = "User wants to be conact with phone number."
    elif contact == "wMail":
        contactType = "User wants to be conact with e-mail adress."

    return contactType