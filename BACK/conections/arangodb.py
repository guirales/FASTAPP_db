from pyArango.connection import Connection
from pyArango.query import AQLQuery
conn=Connection(username="root", password="guirales123")
def ID_userdb(idx,db_name="mydb",col_name="Prueba"):
    db=conn[db_name]
    aql=f"""RETURN DOCUMENT("{col_name}","{idx}")"""
    #print(aql)
    return db.AQLQuery(aql,rawResults=True,batchSize=100)[0]

def Read_usersdb(db_name="mydb",col_name="Prueba"):
    db=conn[db_name]
    aql=f"""
    for c in {col_name}
        return c
    """
    all_users={}
    for user in db.AQLQuery(aql,rawResults=True,batchSize=100):
        all_users[user["_key"]]=user
    #print(aql)
    return all_users

def Create_userdb(new_user,db_name="mydb",col_name="Prueba"):
    db=conn[db_name]
    aql=f"""
    INSERT {new_user} INTO {col_name} 
    LET newDoc = NEW 
    RETURN newDoc"""#RETURN [newDoc._key,newDoc.name,newDoc.surname]
    try:
        new_us=eval(str(db.AQLQuery(aql)))[0]
        return {"status":"done",**new_us}
    except:
        return {"status":"fail","name":"null","surname":"null","alive":False}
#
def Update_userdb(idx,user_update,db_name="mydb",col_name="Prueba"):
    db=conn[db_name]
    aql=f"""
    UPDATE "{idx}" WITH {user_update} IN {col_name} 
    LET updated = NEW 
    RETURN updated""" #[updated._key,updated.name,updated.surname,updated.age]"""
    try:
        updated_us=eval(str(db.AQLQuery(aql)))[0]
        return {"status":"done",**updated_us}
    except:
        return {"status":"fail","name":None,"surname":None}

def Delete_userdb(idx:int,db_name="mydb",col_name="Prueba"):
    db=conn[db_name]
    print("ARANGODB: ",idx)
    aql=f"""
    REMOVE "{idx}" IN {col_name} 
    LET deleted = OLD 
    RETURN [deleted._key,deleted.name,deleted.surname]"""
    try:
        del_us=eval(str(db.AQLQuery(aql,rawResults=False)))[0]
        return {"status":"deleted","id":del_us[0],"name":del_us[1],"surname":del_us[2]}
    except:
        return {"status":"fail","name":None,"surname":None}

if __name__=="__main__":
    #aql="""
    #for c in Prueba
    #    filter c.age >10 and c.age<30
    #    return [c.name,c.surname,c.age]
    #"""
    #aql2="FOR c IN Prueba RETURN c._key"
    #aql3="""
    #for c in Prueba
    #    filter c._key<6450
    #    return [c.name,c.surname,c.age]
    #"""
    #aql4="""RETURN DOCUMENT("Prueba","6434")"""
    #aql5="""RETURN "6434" IN "Prueba" """
    #db=conn["mydb"] 
    #result=db.AQLQuery(aql4,rawResults=True,batchSize=100) 
    
    #print(ID_userdb(26126))
    new={"name":"Pepota","surname":"Pig","2":1,"alive":"True","age":3}
    #nup={"age":13}
    print(Create_userdb(new))
    #print(Update_userdb(71602,nup))
    #print(Delete_userdb(79263))
    #print(Read_usersdb())