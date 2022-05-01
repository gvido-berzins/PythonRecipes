"""
Summary:
    Testing out capsys built-in pytest fixture
Description:
    An example of a command-line test, create after watching Anthony Explains
    [video](https://www.youtube.com/watch?v=sv46294LoP8)
"""
from argparse import ArgumentParser


def test_main(capsys):
    main(["Gvido"])
    out, err = capsys.readouterr()
    assert out == "Hello Gvido!\n"
    assert not err


def main(argv: list[str] = None) -> int:
    parser = ArgumentParser()
    parser.add_argument("name")
    args = parser.parse_args(argv)

    print(f"Hello {args.name}!")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
