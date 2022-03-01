from functools import wraps
import json
def json_io(func):
    @wraps(func)
    def dec(self, url, payload=None):
        if payload is not None and isinstance(payload, str):
            payload = json.loads(payload)
        return json.dumps(func(self, url, payload), indent=2)
    return dec
class User(object):
    def __init__(self, name, owed_by=None, owes=None, **kwargs):
        self.name = name
        self.records = {}
        for borrower, amount in (owed_by or {}).items():
            self.loan(borrower, amount)
        for lender, amount in (owes or {}).items():
            self.borrow(lender, amount)
    def borrow(self, borrower, amount):
        self.records[borrower] = self.records.get(borrower, 0) - amount
    def loan(self, lender, amount):
        self.records[lender] = self.records.get(lender, 0) + amount
    @property
    def owes(self):
        return {k: -v for k, v in self.records.items() if v < 0}
    @property
    def owed_by(self):
        return {k: v for k, v in self.records.items() if v > 0}
    @property
    def balance(self):
        return sum(self.records.values())
    @property
    def __dict__(self):
        return {
            'name': self.name,
            'owes': self.owes,
            'owed_by': self.owed_by,
            'balance': self.balance
        }
class RestAPI(object):
    def __init__(self, database=None):
        self.users = {
            user['name']: User(**user)
            for user in (database or {}).get('users', [])
        }
    @json_io
    def get(self, url, payload=None):
        if url == '/users':
            return {'users': [
                user.__dict__
                for name, user in sorted(self.users.items())
                if payload is None or name in payload['users']
            ]}
    @json_io
    def post(self, url, payload):
        if url == '/add':
            user = User(payload['user'])
            self.users[user.name] = user
            return user.__dict__
        elif url == '/iou':
            lender = self.users[payload['lender']]
            borrower = self.users[payload['borrower']]
            amount = payload['amount']
            lender.loan(borrower.name, amount)
            borrower.borrow(lender.name, amount)
            return {'users': sorted(
                [lender.__dict__, borrower.__dict__],
                key=lambda u: u['name']
            )}
