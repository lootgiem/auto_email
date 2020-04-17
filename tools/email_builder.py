import csv

import config_files.config as c


class email_builder:
    def __init__(self):
        self.emails_formats = self.load_emails_formats()

    @staticmethod
    def load_emails_formats():
        with open(c.path_csv_emails_format, "r") as f:
            reader = csv.DictReader(f, delimiter=";")
            return list(reader)

    def get_email(self, contact):
        for email in self.emails_formats:
            if email["societe"] == contact["societe"]:
                e = email["format"]
                e = e.replace("{prenom}", contact["prenom"])
                e = e.replace("{nom}", contact["nom"])
                return e

        print("Erreur : La société '" + contact['societe'] + "' de " + contact['prenom'] + " " + contact['nom'] + " ne correspond à aucune société dans emails_format.csv")
        raise Exception

    @staticmethod
    def get_content(contact):
        f = open("templates/" + contact["template_name"] + "_template.txt", "r", encoding="utf8")
        content = f.read()
        content = content.replace("{prenom}", contact["prenom"].capitalize())
        content = content.replace("{nom}", contact["nom"].capitalize())
        replacement = contact['template_replace'].split(";")
        for value in replacement:
            r = value.split("=")
            content = content.replace("{" + r[0] + "}", r[1])

        content_splitted = content.split("\n\n", 1)
        return content_splitted[0], content_splitted[1]

    @staticmethod
    def get_attachment_path(attachment):
        attachment_format = c.attachment_format
        replacement = attachment.split(";")
        for value in replacement:
            r = value.split("=")
            attachment_format = c.attachment_format.replace("{" + r[0] + "}", r[1])

        return "attachments/" + attachment_format

    def build(self, contact):
        email = self.get_email(contact)
        subject, message = self.get_content(contact)
        file = self.get_attachment_path(contact["attachment"])

        return email, subject, message, file
