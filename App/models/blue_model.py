from App.ext import db


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    def save(self):
        try:
            db.session.add(self)

            db.session.commit()

            return True
        except Exception as e:
            print(e)
            return False

    def delete(self):
        try:
            db.session.delete(self)

            db.session.commit()

            return True
        except Exception as e:
            print(e)
            return False


class Bing(BaseModel):
    __tablename__ = "bingImg"
    copyright = db.Column(db.String(200))  # 版权
    copyrightlink = db.Column(db.String(200))  # 版权链接
    startdate = db.Column(db.String(50))
    fullstartdate = db.Column(db.String(50))
    enddate = db.Column(db.String(50))
    hsh = db.Column(db.String(50))
    url = db.Column(db.String(200))
    imgUrl = db.Column(db.String(255))
    http = db.Column(db.String(200))
    bot = db.Column(db.Integer())
    drk = db.Column(db.Integer())
    title = db.Column(db.String(50))
    top = db.Column(db.Integer())
    wp = db.Column(db.String(10))
    hs = db.Column(db.String(255))
    addTime = db.Column(db.DateTime())

