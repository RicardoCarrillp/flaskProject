class User():
    count = 1

    def __init__(self, first_name, last_name, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.id = User.count
        User.count += 1
