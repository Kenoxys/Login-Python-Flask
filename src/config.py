class Config:
    SECRET_KEY= 'B!1w8NAt1T^%kvhUI*S^'

class DevelopmentConfig(Config):
    DEBUG=True
    MYSQL_HOST= 'localhost'
    MYSQL_USER= 'MYSQL-USER'
    MYSQL_PASSWORD= 'MYSQL-PASSWORD'
    MYSQL_DB= 'flask-login'

config={
    'development':DevelopmentConfig
}
