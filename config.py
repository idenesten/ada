from dynaconf import Dynaconf

settings = Dynaconf(
    environments=True,
    load_dotenv=True,
    envvar_prefix=False,
    auto_cast=True,
)
