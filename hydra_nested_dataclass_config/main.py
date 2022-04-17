import textwrap

import hydra
from hydra.core.config_store import ConfigStore
from models import DefaultConfig
from omegaconf import OmegaConf

cs = ConfigStore.instance()
cs.store(name="base_config", node=DefaultConfig)


@hydra.main(config_path=".", config_name="config")
def main(cfg: DefaultConfig):
    print("SERVER".center(50, "-"))
    print(textwrap.fill(str(cfg.server), 50))

    print("CLIENT".center(50, "-"))
    print(textwrap.fill(str(cfg.client), 50))

    print("YAML".center(50, "-"))
    print(OmegaConf.to_yaml(cfg))

    print("END".center(50, "-"))


if __name__ == "__main__":
    main()
