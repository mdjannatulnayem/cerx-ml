
class crex_utility:
    def __init__(self):
        self.ed = 0
        self.nd = 0
        self.l = 0
        self.mat_S = 0
        self.fuel = 0
        self.ewt = 0
        self.lwt = 0
        self.fuel = 0
        self.max_t = 0

    def take_input(self):
        try:
            self.ed = float(input("Enter ed: "))
            self.nd = float(input("Enter nd: "))
            self.l = float(input("Enter l: "))
            self.mat_S = float(input("Enter mat_S: "))
            self.fuel = int(input("Enter fuel: "))
            self.ewt = float(input("Enter ewt: "))
            self.lwt = float(input("Enter lwt: "))
            
            if any(value < 0 for value in [self.ed, self.nd, self.l, self.mat_S, self.fuel, self.ewt, self.lwt]):
                raise ValueError("Negative values are not accepted!")

        except ValueError as e:
            print(f"Invalid input: {e}")

