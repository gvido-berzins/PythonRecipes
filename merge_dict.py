"""
Summary:
    Merge a dictionary in a different function to
    update the dictionary
"""
from uuid import uuid4


def merge_dict(d):
    other = {str(uuid4()): dict(some="dict", n=dict(nested=1))}
    d |= other


def unpack_merge_dict(d):
    d |= dict(
        **dict(some=str(uuid4())),
        **dict(som=str(uuid4())),
        **dict(so=str(uuid4())),
        **dict(s=str(uuid4())),
    )


if __name__ == "__main__":
    d = dict(been="here")
    # merge_dict(d)
    # merge_dict(d)
    unpack_merge_dict(d)
    print(d)
