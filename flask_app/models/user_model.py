from flask_app.config.mysqlconnection import connectToMySQL

# from flask_app import app


class User:
    DB = 'users_schema'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod 
    def get_all(cls):
        query = '''
        SELECT *
        FROM users;
        '''

        #results refers to the function connectToMySQL 
        # in mysqlconnection.py file that pulls whichever class that
        # has been specified and the database that exists within it

        #then within the database pulls any queries which are represented through 
        # the classmethod to instruct the data base using CRUD methods(Create,Read,Update, and Delete)
        results = connectToMySQL(cls.DB).query_db(query)

        all_users=[]

        #for (each row in DB == user)
        #Always pass objects to the front end when getting data from the database
        for user in results:  
            all_users.append( cls(user) )

        return all_users



    @classmethod
    def add_user(cls,data):
        query= """
        INSERT INTO users (first_name,last_name,email)
        VALUES( %(first_name)s, %(last_name)s, %(email)s )
        """

        results = connectToMySQL(cls.DB).query_db(query,data)

        return results



    @classmethod
    def get_one(cls,data):
        query= """
        SELECT * FROM users
        WHERE id = %(user_id)s;
        """

        results = connectToMySQL(cls.DB).query_db(query,data)

        return cls(results[0]) #this creates an object out of the first dictionary 
                                #in the list of results



    @classmethod
    def update_user(cls,data):
        query= """
        UPDATE users 
        SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s
        WHERE id = %(user_id)s ;
        """

        results = connectToMySQL(cls.DB).query_db(query,data)

        return results



    @classmethod
    def delete_one(cls,data):
        query="""
        DELETE FROM users
        WHERE id = %(user_id)s ;
        """

        results = connectToMySQL(cls.DB).query_db(query,data)

        return results



    @classmethod
    def display_one(cls,data):
        query= """
        SELECT * FROM users
        WHERE id = %(user_id)s;
        """

        results = connectToMySQL(cls.DB).query_db(query,data)
        print(cls(results[0]))

        return cls(results[0]) #this creates an object out of the first dictionary 
                                #in the list of results