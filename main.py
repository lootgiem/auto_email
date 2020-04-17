import csv

import config_files.config as c
from tools.email_builder import email_builder
from tools.gmail_api import gmail_api


def main():
    ga = gmail_api(email_from=c.email_from)
    eb = email_builder()
    contacts_list = get_contacts_list()
    emails_sent = []

    for contact in contacts_list:
        if not bool(int(contact['envoye'])):
            email, subject, message, file = eb.build(contact=contact)
            ga.send_message_with_attachment(to=email, subject=subject, message_text=message, file=file)
            emails_sent.append(email)
            contact['envoye'] = "1"

    save_csv(contacts_list)
    print("Emails sent to :")
    print(emails_sent)


def get_contacts_list():
    with open(c.path_csv_emails, "r") as f:
        reader = csv.DictReader(f, delimiter=";")
        return list(reader)


def save_csv(dict_data):
    csv_columns = [*dict_data[0]]
    try:
        with open(c.path_csv_emails, 'w', newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=csv_columns, delimiter=";")
            writer.writeheader()
            for data in dict_data:
                writer.writerow(data)
    except IOError:
        print("I/O error")


if __name__ == '__main__':
    main()
