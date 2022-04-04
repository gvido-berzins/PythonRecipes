class M:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a < 20:
            self.a += 1
            return self.a
        else:
            raise StopIteration


if __name__ == "__main__":
    for x in M():
        print(x)
