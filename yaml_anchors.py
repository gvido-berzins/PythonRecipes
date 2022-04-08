"""
Summary:
    Read a YAML file which includes anchors
"""
import yaml

if __name__ == "__main__":
    y = """
    x-this: &this
        yaml: configuration
        is: shared

    that:
        <<: *this
        some: unique1
        keys: values1

    and that:
        <<: *this
        some: unique2
        keys: values2
    """

    dict_ = yaml.safe_load(y)

    print(yaml.dump(dict_))
