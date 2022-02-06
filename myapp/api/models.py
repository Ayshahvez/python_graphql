from unicodedata import name
from app import db

class Tokens(db.Model):
      __tablename__ = 'Tokens'
      id =db.Column(db.Integer,primary_key=True)
      address = db.Column(db.String)
      symbol = db.Column(db.String)
      name= db.Column(db.String)
      decimals= db.Column(db.String)
      total_supply = db.Column(db.String)
 
        def to_dict(self):
            return{   
            "address": self.address,
            "id":self.id,
            "symbol":self.symbol,
            "name":self.name,
            "decimals": self.decimals,
            "total_supply":self.decimals
            }



class Token_Transfers(db.Model):  
        __tablename__ = 'Token_Transfers'     
        token_address = db.Column(db.String)
        from_address = db.Column(db.String)
        to_address = db.Column(db.String)
        transaction_hash = db.Column(db.String)
        block_hash = db.Column(db.String)
        value = db.Column(db.String) 
        log_index = db.Column(db.String)
        block_number = db.Column(db.String)
        block_timestamp = db.Column(db.String)
        id =db.Column(db.Integer,primary_key=True)
        
        def to_dict(self):
            return{   
                "id":self.id,        
                "token_address" : self.token_address,
                "from_address" : self.from_address,
                "to_address": self.to_address,
                "transaction_hash": self.transaction_hash,
                "block_hash" : self.block_hash,
                "value" : self.value,
                "log_index" : self.log_index,
                "block_number" : self.block_number,
                "block_timestamp": self.block_timestamp              
            }