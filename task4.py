class ContactList(list):
    
    def __init__(self, *args):
        self.contacts = []

    def search_by_name(self, *args):
        for i in args:
            self.contacts.append(i)
        contact_list = [i for i in self.contacts if self.contacts.count(i) > 1]
        print('Repetitive contacts in your contacts list:')
        for i in contact_list:
            print(i)


all_contacts = ContactList()
all_contacts.search_by_name('Amangeldi', 'Atai', 'Arstan', 'Aleksandr', 'Alisher',
                            'Azatbek', 'Akhmed', 'Aibek', 'Askar', 'Aleksandr', 'Beken',
                            'Damir', 'Erkin', 'Kanaiym', 'Marsel', 'Nooruz',
                            'Nurgazy', 'Saida', 'Salamat', 'Seitek', 'Shaislam',
                            'Tynchtykbek', 'Uulzhan', 'Uzar', 'Vlad')
