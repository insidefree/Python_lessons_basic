import random


class Ticket:
    def __init__(self, ticket):
        self.ticket = ticket

    @staticmethod
    def generate_ticket():
        numbers = random.sample(range(1, 90), 15)
        it = iter(numbers)
        ticket = dict.fromkeys(range(1, 90), "-")
        i = 0
        while i < 3:
            keys = random.sample(range(1, 9), 5)
            for key in keys:
                ticket[key + i * 10] = next(it)
            i += 1
        return ticket

    def __iter__(self):
        for each in self.__dict__.keys():
            yield self.__getattribute__(each)

    def __str__(self):
        return "{}".format(self.ticket)

ticket = Ticket(Ticket.generate_ticket())
print(ticket)