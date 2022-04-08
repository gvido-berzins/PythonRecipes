"""
Summary:
    Choosing authentication methods based on a pattern
"""


class BasicAuth:
    ...


class PasswordAuth:
    ...


def auth_factory(auth_options: dict):
    option_keys = sorted(list(auth_options.keys()))
    match option_keys:
        case ["basic", *_]:
            return BasicAuth()
        case ["password", "username", *_]:
            return PasswordAuth()
        case _:
            raise ValueError("Authentication not supported")


def main():
    auth_dict = dict(username="big", password="Sh00")
    auth_dict = dict(password="Sh00", username="big")
    auth_dict = dict(password="Sh00", username="big", wut="hello?")
    auth = auth_factory(auth_dict)
    print()
    print(f"Given: {auth_dict}")
    print(auth)

    auth_dict = dict(basic="YWRtaW46YWRtaW4K")
    auth = auth_factory(auth_dict)
    print()
    print(f"Given: {auth_dict}")
    print(auth)


if __name__ == "__main__":
    main()
