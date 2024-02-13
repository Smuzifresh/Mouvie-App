class Config():
    def __init__(self):
        self.SECRET_KEY = "6ec67f2caf30692c2d33699cc9a6c06593e534eff3e8372ebfb6423b2a7c3f5358efc3c496275eb4aefd29c1996e8a5d467cd9b9f03ea131da614c1a85bd9c46"
        # self.SQLALCHEMY_DATABASE_URI = "sqlite:///project.db"
        self.SQLALCHEMY_DATABASE_URI = "postgresql://client:vz7SCXfGRo6Cu6LNMphXmGqbD6Dq0N0e@dpg-cn3iv3ljm4es73bla90g-a/mouviesflask"
        self.UPLOAD_FOLDER = "app/static/media"

        self.DEBUG = True
        self.SQLALCHEMY_ECHO = True
