class CookieJar(object):

    def __init__(self):
        self._is_open = False

    def take(self):
        if not self._is_open:
            raise ValueError("Cookie jar is closed")
        return "Cookie"

    def open_jar(self):
        self._is_open = True

    def close_jar(self):
        self._is_open = False

    def is_open(self):
        return self._is_open


class SelfClosing:
    def __init__(self, jar):
        self._jar = jar

    def __enter__(self):
        self._jar.open_jar()
        return self._jar

    def __exit__(self, exc_type, exc_value, traceback):

        if self._jar.is_open():
            print("Closing the jar...")
            self._jar.close_jar()
        else:
            print("Jar is already closed.")

        if exc_type is not None:

            print(f"An exception occurred: {exc_value}")
            print(f"Exception type: {exc_type}")
            print(f"Traceback: {traceback}")

            return True


def main():
    jar = CookieJar()
    with SelfClosing(jar) as j:
        print(j.take())
        j.close_jar()
        print(j.take())
        print("Jar is closed now.")
