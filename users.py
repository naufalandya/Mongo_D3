from server import db

users = db['users']

class Users:
    def __init__(self, id, name, username, email, password, bio, createdAt):
        self.id = id
        self.name = name
        self.username = username
        self.email = email
        self.password = password
        self.bio = bio
        self.createdAt = createdAt

    def add_single_user(name, username, email, password, bio, createdAt, country, age):

        try:

            isEmail =  users.find_one({'email' : email})

            if isEmail:
                return False
            
            data = users.insert_one({
                'name': name,
                'username': username,
                'email': email,
                'password': password,
                'bio': bio,
                'createdAt': createdAt,
                'country' : country,
                'age' : age
            })
            
            return data
    
        except Exception as e:
            print(e)
            return None

    def find_user_by_email(email):

        try:
            user =  users.find_one({'email' : email})

            if not user:
                return False

            return user

        except Exception as e:
            print(e)
            return None


    def find_user_by_username(username):

        try:
            user =  users.find_one({'username' : username})

            if not user:
                return False

            return user

        except Exception as e:
            print(e)
            return None


    def update_user_by_username(name=False, username=False, email=False, bio=False):

        try:
                        
            if username is False:
                return False

            isUser =  users.find_one({'username': username})

            if not isUser:
                return False

            update_data = {}
            if name is not False:
                update_data['name'] = name
            if email is not False:
                update_data['email'] = email
            if bio is not False:
                update_data['bio'] = bio

            user =  users.update_one({'username': username}, {'$set': update_data})

            return user

        except Exception as e:
            print(e)
            return None


    def delete_user_by_username(username):

        try:

            isUser =  users.find_one({'username': username})

            if not isUser:
                return False
        
            user =  users.delete_one({'username' : username})

            return user

        except Exception as e:
            print(e)
            return None
        
        
    def aggregated_users_by_country():
        pipeline = [
            {"$group": {"_id": "$country", "total_users": {"$sum": 1}}}
        ]

        result = list(users.aggregate(pipeline))

        aggregated_data = []
        for data in result:
            aggregated_data.append({"country": data['_id'], "total_users": data['total_users']})

        return aggregated_data
    
    def aggregated_users_by_age():
        pipeline = [
            {
                "$group": {
                    "_id": {
                        "$switch": {
                            "branches": [
                                {"case": {"$and": [{"$gte": ["$age", 10]}, {"$lt": ["$age", 20]}]}, "then": "10-19"},
                                {"case": {"$and": [{"$gte": ["$age", 20]}, {"$lt": ["$age", 30]}]}, "then": "20-29"},
                                {"case": {"$and": [{"$gte": ["$age", 30]}, {"$lt": ["$age", 40]}]}, "then": "30-39"},
                                {"case": {"$and": [{"$gte": ["$age", 40]}, {"$lt": ["$age", 50]}]}, "then": "40-49"},
                                {"case": {"$and": [{"$gte": ["$age", 50]}, {"$lt": ["$age", 60]}]}, "then": "50-59"},
                                {"case": {"$and": [{"$gte": ["$age", 60]}, {"$lt": ["$age", 70]}]}, "then": "60-69"},
                                {"case": {"$and": [{"$gte": ["$age", 70]}, {"$lt": ["$age", 80]}]}, "then": "70-79"}
                            ],
                            "default": "80+"
                        }
                    },
                    "total_users": {"$sum": 1}
                }
            },
            {"$sort": {"_id": 1}}  
        ]

        result = list(users.aggregate(pipeline))

        aggregated_data = []
        for data in result:
            aggregated_data.append({"age_group": data['_id'], "total_users": data['total_users']})

        return aggregated_data





