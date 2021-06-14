class Controls:

    def __init__(self):
        self._observers = []

    def notify_s(self, modifier=None):

        for observer in self._observers:
            if modifier != observer:
                observer.start()

    def notify_i(self, modifier=None):

        for observer in self._observers:
            if modifier != observer:
                observer.info()

    def notify_k(self, modifier=None):

        for observer in self._observers:
            if modifier != observer:
                observer.exit()

    def notify_test(self, modifier=None):

        for observer in self._observers:
            if modifier != observer:
                observer.test()

    def attach(self, observer):

        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):

        try:
            self._observers.remove(observer)
        except ValueError:
            pass
