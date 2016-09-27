# YapdatabaseSwiftObjGen
This is a python script that generates a swift class for the given instance variables user requests. 
Generated swift class includes NSCoding delgete and few utility functions for Yapdatabase such as
key, collection, saveWithTransaction, fetch, fetchAll.  

# Example
tab spaces: 4
class name: User
variables: 3
variable name, type:
name String
surname String
id Int
key variable name: id

# Generated Code
import YapDatabase
import Foundation

class User: NSObject, NSCoding {
    var name: String
    var surname: String
    var id: Int

    static let collection = String(User)

    func key() -> String {
        return String(id)
    }

    func init(name: String, andSurname surname: String, andId id: Int) {
        self.name = name
        self.surname = surname
        self.id = id
    }

    required init(coder aDecoder: NSCoder) {
        self.name = aDecoder.decodeObjectForKey("name") as! String
        self.surname = aDecoder.decodeObjectForKey("surname") as! String
        self.id = aDecoder.decodeObjectForKey("id") as! Int
    }

    func encodeWithCoder(aCoder: NSCoder) {
        aCoder.encodeObject(self.name, forKey: "name")
        aCoder.encodeObject(self.surname, forKey: "surname")
        aCoder.encodeObject(self.id, forKey: "id")
    }

    func saveWithTransaction(transaction: YapDatabaseReadWriteTransaction) {
        transaction.setObject(self, forKey: key(), inCollection: User.collection)
    }

    static func fetch(key: String, withTransaction transaction: YapDatabaseReadTransaction) -> User? {
        return transaction.objectForKey(key, inCollection: collection) as? User
    }

    static func fetchAll(transaction: YapDatabaseReadTransaction) -> [User] {
        let keys = transaction.allKeysInCollection(collection) as! [String]
        var res:[User] = []
        for key in keys {
            if let object = transaction.objectForKey(key, inCollection: collection) as? User {
                res.append(object)
            }
        }
        return res
    }
}
