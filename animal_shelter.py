from pymongo import MongoClient
from pprint import pprint
from bson.objectid import ObjectId

# This class handles mongo CRUD operations
# for the animals collection in the AAC database
# AAC is a csv file
#
#each method for this class handles a single CRUD
#operation by taking in a single data parameter of
#type dictionary which will correspond to a data
#item from/to the database
class AnimalShelter(object) :
    
    #initialize mongo client
    def __init__(self, username, password) :
        self.client = MongoClient('mongodb://%s:%s@localhost:28434' % (username, password))
        self.database = self.client['AAC']
    
    # C(create) method =========================================================
    # adds one new document to the database returns boolean completion result
    def create(self, data) :
        
        #try catch to clean up output
        #and also since error handling is an aboslute good in the world
        try :
            #determine non empty
            if data is not None :

                #determine dictionary type
                if(isinstance(data, dict)) : 
                    result = self.database.animals.insert_one(data)
                    pprint("Document added. INFO: " + str(result))
                    return True

                else :
                    raise Exception("Data must be of type: dictionary")
                    return False

            else :
                raise Exception("Nothing to save, because data parameter is empty")
                return False
        
        except Exception as e :
            print("Exception occured: ", e)
            
    # R(read) method =========================================================
    # queries for the passed in data. prints result and returns boolean completion result
    def read(self, data) :
        
        #clean up output 
        try :
            #determine non empty
            if data is not None :

                #determine dictionary type
                if(isinstance(data, dict)) :
                    result = list(self.database.animals.find(data, {"_id": False}))
                    #pprint(result)
                    return result

                else :
                    raise Exception("Data must be of type: dictionary")
                    return False
            else :
                raise Exception("Nothing to read, data parameter is empty")
                return False
                
        except Exception as e :
            print("Exception occured: ", e)
            
            
    # U(update) method =========================================================
    # queries for the passed in data, updates to the new data (once)
    def update(self, toUpdate, data) :
        
        #clean up output
        try :
            #determine query not empty
            if toUpdate is not None and data is not None:
                
                #determine dictionary type
                if(isinstance(toUpdate, dict) and isinstance(data, dict)) :
                    
                    #determine if the query returns actual document/s
                    if(list(self.database.animals.find(toUpdate)) is not None) :
                        result = self.database.animals.update_one(toUpdate, data)
                        pprint(result)
                        return True
                    
                    else :
                        raise Exception("Data parameter was not located in the database")
                
                else :
                    raise Exception("Data parameters must be of type: dictionary")
                    return False
                
            else :
                raise Exception("One or both data parameters are empty")
                return False
                
        except Exception as e :
            print("Exception occured: ", e)
            
            
    # D(delete) method =========================================================
    # deletes one document from the database
    def delete(self, data) :
        
        #clean up output
        try :
            #determine not empty
            if data is not None :
                
                #determine dictionary type
                if(isinstance(data, dict)) :
                    result = self.database.animals.delete_one(data)
                    pprint(result)
                    return True
                
                else :
                    raise Exception("Data must be of type: dictionary")
                    return False
                
            else :
                raise Exception("Nothing to read, data parameter is empty")
                
        except Exception as e :
            print("Exception occured: ", e)
                  