class SupplierModel():
    
    def __init__(self, company_name, description, email, phone, street_address, city, postal_code, province, country):
        self._id = None
        self._company_name = company_name
        self._description = description
        self._email = email
        self._phone = phone
        self._street_address = street_address
        self._city = city
        self._postal_code = postal_code
        self._province = province
        self._country = country
        self._created_at = None
        
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id
        
    @property
    def company_name(self):
        return self._company_name
    
    @company_name.setter
    def company_name(self, company_name):
        self._company_name = company_name
        
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, description):
        self._description = description
        
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        self._email = email
        
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        self._phone = phone
        
    @property
    def street_address(self):
        return self._street_address
    
    @street_address.setter
    def street_address(self, street_address):
        self._street_address = street_address
        
    @property
    def city(self):
        return self._city
    
    @city.setter
    def city(self, city):
        self._city = city
        
    @property
    def postal_code(self):
        return self._postal_code
    
    @postal_code.setter
    def postal_code(self, postal_code):
        self._postal_code = postal_code
        
    @property
    def province(self):
        return self._province
    
    @province.setter
    def province(self, province):
        self._province = province
        
    @property
    def country(self):
        return self._country
    
    @country.setter
    def country(self, country):
        self._country = country
        
    @property
    def created_at(self):
        return self._created_at
    
    @created_at.setter
    def created_at(self, created_at):
        self_created_at = created_at
        
    def to_dict(self):
        supplier_dict = {
            'id': self._id,
            'company_name': self._company_name,
            'description': self._description,
            'email': self._email,
            'phone': self._phone,
            'street_address': self._street_address,
            'city': self._city,
            'postal_code': self._postal_code,
            'province': self._province,
            'country': self._country,
            'created_at': self._created_at
        }
        return supplier_dict