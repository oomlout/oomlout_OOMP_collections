import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()

oType = "COLLECTION"
oSize = "PARTL"
oColor = "JLCC"
oDesc = "BASIC"
oIndex = "01"
hexId = "COLJLCB"

newPart.addTag('oompType',oType)
newPart.addTag('oompSize',oSize)
newPart.addTag('oompColor',oColor)
newPart.addTag('oompDesc',oDesc)
newPart.addTag('oompIndex',oIndex)
oompId = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 

newPart.addTag('name','JLC Parts Library')
newPart.addTag('description','A collection of all OOMP parts with JLC parts library details')
newPart.addTag('code','jlcb')
newPart.addTag('collection',[])


######  Common
newPart.addTag('hexID',hexId)

######  Housekeeping
newPart = OOMPtags.addTags(newPart,oompId)
OOMP.parts.append(newPart)
