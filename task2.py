class User:
    level = 0
    exp = 0
    status = 'free'
    remaining_days = None


    def validate_exp(self, exp):
        if exp < 0:
            raise Exception('exp cannot be negative')
        return exp

    def validate_username(self, username):
        if not username:
            raise Exception('Username cant be empty')
        return username

    def validate_status(self, status):
        if status not in ['free', 'paid']:
            raise Exception('Status must be one of: "free", "paid"')
        return status

    def __init__(self, username, exp=None, status=None):
        username = self.validate_username(username)
        self.username = username

        if exp is not None:
            exp = self.validate_exp(exp)
            self.exp = exp

        if status is not None:
            status = self.validate_status(status)
            self.status = status

    def __increase_level(self):
        self.level += 1

    def update(self):
        levels = self.exp // 500
        for i in range(levels):
            self.__increase_level
        if self.actions < 3 and self.status == 'free':
            self.actions = 3
        if self.status == 'paid':
            self.remaining_days -= 1

    def make_action(self):
        pass

    def __setattr__(self, attr, value):
        if attr == 'level':
            raise Exception('You cannot increase level directly')


user1 = User(
    username='andrew',
    exp=10,
    'paid',
)
user1.make_action()
user1.update()
user1.increase_level()