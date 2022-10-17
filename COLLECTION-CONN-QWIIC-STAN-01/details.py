import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()

oType = "COLLECTION"
oSize = "CONN"
oColor = "QWIIC"
oDesc = "STAN"
oIndex = "01"
hexId = "COLQWIIC"

newPart.addTag('oompType',oType)
newPart.addTag('oompSize',oSize)
newPart.addTag('oompColor',oColor)
newPart.addTag('oompDesc',oDesc)
newPart.addTag('oompIndex',oIndex)
oompId = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 

newPart.addTag('name','QWIIC Breakouts')
newPart.addTag('description','A collection of all OOMP projects that have a qwiic connector')
newPart.addTag('code','qwiic')
newPart.addTag('collection',[])


######  Common
newPart.addTag('hexID',hexId)

######  Housekeeping
newPart = OOMPtags.addTags(newPart,oompId)
OOMP.parts.append(newPart)
