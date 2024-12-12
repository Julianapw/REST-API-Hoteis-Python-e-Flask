from sql_alchemy import banco

class UserModel(banco.model):
    __tablename__ = 'usuarios'
    
    user_id = banco.Column(banco.Integer, primary_key = True)
    login = banco.Column(banco.String(40))
    senha = banco.Column(banco.String(40))
    
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha
    
    def json(self):
        return{
            "user_id":self.user_id,
            "login":self.login
        }
    
    @classmethod
    def find_by_login(cls,login):
        user = cls.query.filter_by(login).first()
        if user:
            return user
        return None
    
    def save_hotel(self):
        banco.session.add(self)
        banco.session.commit()
        
    