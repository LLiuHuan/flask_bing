import redis


def get_db_uri(dbinfo):
    enqine = dbinfo.get("ENGINE") or "mysql"
    driver = dbinfo.get("DRIVER") or "pymysql"
    user = dbinfo.get("USER") or "root"
    password = dbinfo.get("PASSWORD") or "1234567"
    host = dbinfo.get("HOST") or "localhost"
    port = dbinfo.get("PORT") or 3306
    name = dbinfo.get("NAME") or "Flask"

    return "{}+{}://{}:{}@{}:{}/{}".format(
        enqine, driver, user, password, host, port, name
    )


class Config:
    TESTING = False
    DEBUG = False

    # SQLAlchemy 默认配置
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 加密密钥 越复杂越好
    SECRET_KEY = "elephantnote.com"

    # session缓存 设置为redis
    SESSION_TYPE = 'redis'
    # 是否强制加盐，混淆session
    SESSION_USE_SIGNER = True
    # session的key 越复杂越好
    SESSION_KEY = "LLiuHuan980724."
    # 设置redis的ip,port,库,有效时间
    # REDIS_HOST = "127.0.0.1"
    # REDIS_PORT = "6379"
    # REDIS_DB = 0
    # ERMANENT_SESSION_LIFETIME = 24 * 60 * 60

    # sessons是否长期有效，false，则关闭浏览器，session失效
    # SESSION_PERMANENT = False
    # 保存到redis的session数的名称前缀
    SESSION_KEY_PREFIX = "session:"
    # session保存数据到redis时启用的链接对象
    SESSION_REDIS = redis.Redis(host='127.0.0.1', port='6379', password='LLiuHuan980724.')  # 用于连接redis的配置


class DevelopConfig(Config):
    """
    开发环境
    """
    DEBUG = True

    dbinfo = {
        "ENGINE": "mysql",  # 使用数据库
        "DRIVER": "pymysql",  # 数据库驱动器
        "USER": "root",  # 用户
        "PASSWORD": "LLiuHuan980724.",  # 密码
        "HOST": "49.233.178.154",  # 连接地址
        "PORT": 3306,  # 端口
        "NAME": "bing"  # 数据库名称
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


class TestingConfig(Config):
    """
    测试环境
    """
    TESTING = True

    dbinfo = {
        "ENGINE": "mysql",  # 使用数据库
        "DRIVER": "pymysql",  # 数据库驱动器
        "USER": "root",  # 用户
        "PASSWORD": "LLiuHuan980724.",  # 密码
        "HOST": "49.233.178.154",  # 连接地址
        "PORT": 3306,  # 端口
        "NAME": "bing"  # 数据库名称
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


class StagingConfig(Config):
    """
    演示环境
    """
    dbinfo = {
        "ENGINE": "mysql",  # 使用数据库
        "DRIVER": "pymysql",  # 数据库驱动器
        "USER": "root",  # 用户
        "PASSWORD": "LLiuHuan980724.",  # 密码
        "HOST": "49.233.178.154",  # 连接地址
        "PORT": 3306,  # 端口
        "NAME": "bing"  # 数据库名称
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


class ProductConfig(Config):
    """
    生产环境
    """
    dbinfo = {
        "ENGINE": "mysql",  # 使用数据库
        "DRIVER": "pymysql",  # 数据库驱动器
        "USER": "root",  # 用户
        "PASSWORD": "LLiuHuan980724.",  # 密码
        "HOST": "49.233.178.154",  # 连接地址
        "PORT": 3306,  # 端口
        "NAME": "bing"  # 数据库名称
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


# 组合所有环境
envs = {
    "develop": DevelopConfig,
    "testing": TestingConfig,
    "staging": StagingConfig,
    "product": ProductConfig,
    "default": DevelopConfig
}
