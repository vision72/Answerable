class Tag:
    def __init__(self, name, reputation=0, count=1):
        self.name = name
        self.reputation = reputation
        self.count = count

    def ratio(self):
        return max(self.reputation / self.count, 0.01)

    def __str__(self):
        return "{:15}{}/{}".format("[{}]".format(self.name), reputation, count)
