from dicepy.lib.database import Database


class AddressesController():

    def __init__(self):
        self.db = Database()
        self.table = 'addresses'
        self.columns = [
            'street_address',
            'city',
            'postal_code',
            'province',
            'country'
        ]
