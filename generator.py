import sys

def capitalizeFirst(s):
  leftSide = s[0:1].upper()
  rightSide = s[1:]
  return leftSide + rightSide

sys.stdout.write('#tab spaces: ')
sys.stdout.flush()
tabk = input()
tab = " " * tabk

sys.stdout.write('class name: ')
sys.stdout.flush()
className = raw_input()

sys.stdout.write('#variables: ')
sys.stdout.flush()
n = input()

print "variable name, type:"
names = []
types = []
for i in xrange(n):
  a, b = map(str, raw_input().split())
  names.append(a)
  types.append(b)

sys.stdout.write('key variable name: ')
sys.stdout.flush()
keyVarName = raw_input()

print "import YapDatabase"
print "import Foundation"
print ""

print "class %s: NSObject, NSCoding {" % className

for i in xrange(n):
  print tab + "var %s: %s" % (names[i], types[i])
print ""

print tab + "static let collection = String(%s)" % (className)
print ""

print tab + "func key() -> String {"
print tab + tab + "return String(%s)" % (keyVarName)
print tab + "}"
print ""

initFunc = tab + "func init("
for i in xrange(n):
  if i == 0:
    initFunc += "%s: %s" % (names[i], types[i])
  else:
    initFunc += "and%s %s: %s" % (capitalizeFirst(names[i]), names[i], types[i])
  if i + 1 < n:
    initFunc += ", "
initFunc += ") {"

print initFunc  
for i in xrange(n):
  print tab + tab + "self.%s = %s" % (names[i], names[i])
print tab + "}"
print ""

print tab + "required init(coder aDecoder: NSCoder) {"
for i in xrange(n):
  print tab + tab + 'self.%s = aDecoder.decodeObjectForKey("%s") as! %s' % (names[i], names[i], types[i])
print tab + "}"
print ""

print tab + "func encodeWithCoder(aCoder: NSCoder) {"
for i in xrange(n):
  print tab + tab + 'aCoder.encodeObject(self.%s, forKey: "%s")' % (names[i], names[i])
print tab + "}"
print ""

print tab + "func saveWithTransaction(transaction: YapDatabaseReadWriteTransaction) {"
print tab + tab + "transaction.setObject(self, forKey: key(), inCollection: %s.collection)" % (className)
print tab + "}"
print ""

print tab + "static func fetch(key: String, withTransaction transaction: YapDatabaseReadTransaction) -> %s? {" % (className)
print tab + tab + "return transaction.objectForKey(key, inCollection: collection) as? %s" % (className)
print tab + "}"
print ""

print tab + "static func fetchAll(transaction: YapDatabaseReadTransaction) -> [%s] {" % (className)
print tab + tab + "let keys = transaction.allKeysInCollection(collection) as! [String]"
print tab + tab + "var res:[%s] = []" % (className)
print tab + tab + "for key in keys {"
print tab + tab + tab + "if let object = transaction.objectForKey(key, inCollection: collection) as? %s {" % (className)
print tab + tab + tab + tab + "res.append(object)"
print tab + tab + tab + "}"
print tab + tab + "}"
print tab + tab + "return res"
print tab + "}"

print "}"
