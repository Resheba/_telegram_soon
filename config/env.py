import os
from dotenv import load_dotenv


load_dotenv(override=True)


class Settings:
    # NEW VARS PUT BELOW
    TG_TOKEN: str = os.getenv('TG_TOKEN')
    DB_DSN: str = os.getenv('DB_DSN')

    @classmethod
    def __get_vars__(cls) -> dict[str, str | None]:
        return {k:v for k,v in cls.__dict__.items() if not k.startswith('__')}
    

if not all(Settings.__get_vars__().values()):
    raise Exception(f'Some env variable missed!\n\t' + "\n\t".join(k for k, v in Settings.__get_vars__().items() if not v))
