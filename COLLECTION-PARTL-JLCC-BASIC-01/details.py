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
newPart.addTag('collection',['CAPC-0402-X-NF1-V50', 'CAPC-0402-X-NF10-V50', 'CAPC-0402-X-NF100-V16', 'CAPC-0402-X-NF100-V50', 'CAPC-0402-X-NF2-V50', 'CAPC-0402-X-NF20-V16', 'CAPC-0402-X-NF3-V50', 'CAPC-0402-X-NF47D-V50', 'CAPC-0402-X-NF70-V10', 'CAPC-0402-X-NF8-V50', 'CAPC-0402-X-PF1-V50', 'CAPC-0402-X-PF10-V50', 'CAPC-0402-X-PF100-V50', 'CAPC-0402-X-PF12-V50', 'CAPC-0402-X-PF15D-V50', 'CAPC-0402-X-PF20-V50', 'CAPC-0402-X-PF22-V50', 'CAPC-0402-X-PF22D-V50', 'CAPC-0402-X-PF3-V50', 'CAPC-0402-X-PF30-V50', 'CAPC-0402-X-PF47D-V50', 'CAPC-0402-X-PF5-V50', 'CAPC-0402-X-PF50-V50', 'CAPC-0402-X-PF7-V50', 'CAPC-0402-X-PF70-V50', 'CAPC-0402-X-PF8-V50', 'CAPC-0402-X-UF1-V25', 'CAPC-0402-X-UF10-V63D', 'CAPC-0402-X-UF2-V63D', 'CAPC-0402-X-UF47D-V10', 'CAPC-0603-X-NF1-V50', 'CAPC-0603-X-NF10-V50', 'CAPC-0603-X-NF100-V50', 'CAPC-0603-X-NF2-V50', 'CAPC-0603-X-NF20-V25', 'CAPC-0603-X-NF3-V50', 'CAPC-0603-X-NF30-V25', 'CAPC-0603-X-NF47D-V50', 'CAPC-0603-X-NF5-V50', 'CAPC-0603-X-NF7-V50', 'CAPC-0603-X-NF70-V25', 'CAPC-0603-X-NF8-V50', 'CAPC-0603-X-PF1-V50', 'CAPC-0603-X-PF10-V50', 'CAPC-0603-X-PF100-V50', 'CAPC-0603-X-PF12-V50', 'CAPC-0603-X-PF20-V50', 'CAPC-0603-X-PF200-V50', 'CAPC-0603-X-PF22-V50', 'CAPC-0603-X-PF3-V50', 'CAPC-0603-X-PF30-V50', 'CAPC-0603-X-PF47D-V50', 'CAPC-0603-X-PF5-V50', 'CAPC-0603-X-PF50-V50', 'CAPC-0603-X-PF6-V50', 'CAPC-0603-X-PF7-V50', 'CAPC-0603-X-PF70-V50', 'CAPC-0603-X-PF8-V50', 'CAPC-0603-X-PF80-V50', 'CAPC-0603-X-UF1-V50', 'CAPC-0603-X-UF10-V10', 'CAPC-0603-X-UF10-V25', 'CAPC-0603-X-UF2-V16', 'CAPC-0603-X-UF2-V63D', 'CAPC-0603-X-UF47D-V16', 'CAPC-0805-X-NF1-V50', 'CAPC-0805-X-NF10-V50', 'CAPC-0805-X-NF100-V100', 'CAPC-0805-X-NF100-V50', 'CAPC-0805-X-NF2-V50', 'CAPC-0805-X-NF20-V50', 'CAPC-0805-X-NF3-V50', 'CAPC-0805-X-NF30-V50', 'CAPC-0805-X-NF47D-V50', 'CAPC-0805-X-NF5-V50', 'CAPC-0805-X-NF7-V50', 'CAPC-0805-X-NF70-V50', 'CAPC-0805-X-NF8-V50', 'CAPC-0805-X-PF10-V50', 'CAPC-0805-X-PF100-V50', 'CAPC-0805-X-PF12-V50', 'CAPC-0805-X-PF20-V50', 'CAPC-0805-X-PF22-V50', 'CAPC-0805-X-PF3-V50', 'CAPC-0805-X-PF30-V50', 'CAPC-0805-X-PF5-V50', 'CAPC-0805-X-PF50-V50', 'CAPC-0805-X-PF7-V50', 'CAPC-0805-X-PF70-V50', 'CAPC-0805-X-PF8-V50', 'CAPC-0805-X-UF1-V50', 'CAPC-0805-X-UF10-V25', 'CAPC-0805-X-UF10-V50', 'CAPC-0805-X-UF2-V50', 'CAPC-0805-X-UF47D-V25', 'CAPC-0805-X-UF7-V63D', 'CAPC-1206-X-NF1-V2000', 'CAPC-1206-X-NF1-V500', 'CAPC-1206-X-NF10-V50', 'CAPC-1206-X-NF100-V50', 'CAPC-1206-X-NF20-V50', 'CAPC-1206-X-UF1-V50', 'CAPC-1206-X-UF10-V50', 'CAPC-1206-X-UF100-V63D', 'CAPC-1206-X-UF2-V10', 'CAPC-1206-X-UF2-V25', 'CAPC-1206-X-UF2-V50', 'CAPC-1206-X-UF47D-V50', 'CAPC-1206-X-UF7-V10', 'RESE-0402-X-O000-01', 'RESE-0402-X-O100-01', 'RESE-0402-X-O101-01', 'RESE-0402-X-O102-01', 'RESE-0402-X-O103-01', 'RESE-0402-X-O104-01', 'RESE-0402-X-O105-01', 'RESE-0402-X-O106-01', 'RESE-0402-X-O10X-01', 'RESE-0402-X-O121-01', 'RESE-0402-X-O123-01', 'RESE-0402-X-O124-01', 'RESE-0402-X-O151-01', 'RESE-0402-X-O153-01', 'RESE-0402-X-O154-01', 'RESE-0402-X-O183-01', 'RESE-0402-X-O201-01', 'RESE-0402-X-O202-01', 'RESE-0402-X-O203-01', 'RESE-0402-X-O204-01', 'RESE-0402-X-O220-01', 'RESE-0402-X-O221-01', 'RESE-0402-X-O222-01', 'RESE-0402-X-O223-01', 'RESE-0402-X-O224-01', 'RESE-0402-X-O243-01', 'RESE-0402-X-O273-01', 'RESE-0402-X-O301-01', 'RESE-0402-X-O304-01', 'RESE-0402-X-O330-01', 'RESE-0402-X-O331-01', 'RESE-0402-X-O332-01', 'RESE-0402-X-O333-01', 'RESE-0402-X-O334-01', 'RESE-0402-X-O393-01', 'RESE-0402-X-O402-01', 'RESE-0402-X-O470-01', 'RESE-0402-X-O471-01', 'RESE-0402-X-O473-01', 'RESE-0402-X-O474-01', 'RESE-0402-X-O4992-01', 'RESE-0402-X-O499D-01', 'RESE-0402-X-O502-01', 'RESE-0402-X-O510-01', 'RESE-0402-X-O511-01', 'RESE-0402-X-O512-01', 'RESE-0402-X-O513-01', 'RESE-0402-X-O514-01', 'RESE-0402-X-O563-01', 'RESE-0402-X-O602-01', 'RESE-0402-X-O681-01', 'RESE-0402-X-O683-01', 'RESE-0402-X-O702-01', 'RESE-0402-X-O750-01', 'RESE-0402-X-O752-01', 'RESE-0402-X-O753-01', 'RESE-0402-X-O802-01', 'RESE-0402-X-O822-01', 'RESE-0402-X-O902-01', 'RESE-0603-X-O000-01', 'RESE-0603-X-O100-01', 'RESE-0603-X-O101-01', 'RESE-0603-X-O102-01', 'RESE-0603-X-O103-01', 'RESE-0603-X-O104-01', 'RESE-0603-X-O105-01', 'RESE-0603-X-O106-01', 'RESE-0603-X-O10X-01', 'RESE-0603-X-O112-01', 'RESE-0603-X-O113-01', 'RESE-0603-X-O114-01', 'RESE-0603-X-O121-01', 'RESE-0603-X-O123-01', 'RESE-0603-X-O124-01', 'RESE-0603-X-O133-01', 'RESE-0603-X-O134-01', 'RESE-0603-X-O150-01', 'RESE-0603-X-O151-01', 'RESE-0603-X-O153-01', 'RESE-0603-X-O154-01', 'RESE-0603-X-O164-01', 'RESE-0603-X-O181-01', 'RESE-0603-X-O183-01', 'RESE-0603-X-O184-01', 'RESE-0603-X-O200-01', 'RESE-0603-X-O201-01', 'RESE-0603-X-O202-01', 'RESE-0603-X-O203-01', 'RESE-0603-X-O204-01', 'RESE-0603-X-O205-01', 'RESE-0603-X-O220-01', 'RESE-0603-X-O221-01', 'RESE-0603-X-O222-01', 'RESE-0603-X-O223-01', 'RESE-0603-X-O224-01', 'RESE-0603-X-O225-01', 'RESE-0603-X-O22X-01', 'RESE-0603-X-O241-01', 'RESE-0603-X-O243-01', 'RESE-0603-X-O244-01', 'RESE-0603-X-O270-01', 'RESE-0603-X-O271-01', 'RESE-0603-X-O273-01', 'RESE-0603-X-O274-01', 'RESE-0603-X-O301-01', 'RESE-0603-X-O302-01', 'RESE-0603-X-O303-01', 'RESE-0603-X-O304-01', 'RESE-0603-X-O305-01', 'RESE-0603-X-O330-01', 'RESE-0603-X-O331-01', 'RESE-0603-X-O332-01', 'RESE-0603-X-O333-01', 'RESE-0603-X-O334-01', 'RESE-0603-X-O361-01', 'RESE-0603-X-O363-01', 'RESE-0603-X-O364-01', 'RESE-0603-X-O391-01', 'RESE-0603-X-O393-01', 'RESE-0603-X-O394-01', 'RESE-0603-X-O402-01', 'RESE-0603-X-O4022-01', 'RESE-0603-X-O431-01', 'RESE-0603-X-O432-01', 'RESE-0603-X-O433-01', 'RESE-0603-X-O434-01', 'RESE-0603-X-O470-01', 'RESE-0603-X-O471-01', 'RESE-0603-X-O473-01', 'RESE-0603-X-O474-01', 'RESE-0603-X-O47X-01', 'RESE-0603-X-O4992-01', 'RESE-0603-X-O499D-01', 'RESE-0603-X-O502-01', 'RESE-0603-X-O505-01', 'RESE-0603-X-O510-01', 'RESE-0603-X-O511-01', 'RESE-0603-X-O512-01', 'RESE-0603-X-O513-01', 'RESE-0603-X-O514-01', 'RESE-0603-X-O515-01', 'RESE-0603-X-O560-01', 'RESE-0603-X-O561-01', 'RESE-0603-X-O563-01', 'RESE-0603-X-O564-01', 'RESE-0603-X-O602-01', 'RESE-0603-X-O621-01', 'RESE-0603-X-O622-01', 'RESE-0603-X-O623-01', 'RESE-0603-X-O680-01', 'RESE-0603-X-O681-01', 'RESE-0603-X-O683-01', 'RESE-0603-X-O684-01', 'RESE-0603-X-O702-01', 'RESE-0603-X-O705-01', 'RESE-0603-X-O750-01', 'RESE-0603-X-O751-01', 'RESE-0603-X-O752-01', 'RESE-0603-X-O753-01', 'RESE-0603-X-O754-01', 'RESE-0603-X-O802-01', 'RESE-0603-X-O820-01', 'RESE-0603-X-O821-01', 'RESE-0603-X-O822-01', 'RESE-0603-X-O823-01', 'RESE-0603-X-O902-01', 'RESE-0603-X-O912-01', 'RESE-0603-X-O913-01', 'RESE-0603-X-O993-01', 'RESE-0805-X-O000-01', 'RESE-0805-X-O100-01', 'RESE-0805-X-O101-01', 'RESE-0805-X-O102-01', 'RESE-0805-X-O103-01', 'RESE-0805-X-O104-01', 'RESE-0805-X-O105-01', 'RESE-0805-X-O106-01', 'RESE-0805-X-O10X-01', 'RESE-0805-X-O113-01', 'RESE-0805-X-O121-01', 'RESE-0805-X-O123-01', 'RESE-0805-X-O124-01', 'RESE-0805-X-O133-01', 'RESE-0805-X-O150-01', 'RESE-0805-X-O151-01', 'RESE-0805-X-O153-01', 'RESE-0805-X-O154-01', 'RESE-0805-X-O163-01', 'RESE-0805-X-O181-01', 'RESE-0805-X-O183-01', 'RESE-0805-X-O184-01', 'RESE-0805-X-O200-01', 'RESE-0805-X-O201-01', 'RESE-0805-X-O202-01', 'RESE-0805-X-O203-01', 'RESE-0805-X-O204-01', 'RESE-0805-X-O205-01', 'RESE-0805-X-O220-01', 'RESE-0805-X-O221-01', 'RESE-0805-X-O222-01', 'RESE-0805-X-O223-01', 'RESE-0805-X-O224-01', 'RESE-0805-X-O225-01', 'RESE-0805-X-O22X-01', 'RESE-0805-X-O241-01', 'RESE-0805-X-O243-01', 'RESE-0805-X-O270-01', 'RESE-0805-X-O271-01', 'RESE-0805-X-O273-01', 'RESE-0805-X-O274-01', 'RESE-0805-X-O301-01', 'RESE-0805-X-O302-01', 'RESE-0805-X-O303-01', 'RESE-0805-X-O304-01', 'RESE-0805-X-O330-01', 'RESE-0805-X-O331-01', 'RESE-0805-X-O332-01', 'RESE-0805-X-O333-01', 'RESE-0805-X-O334-01', 'RESE-0805-X-O363-01', 'RESE-0805-X-O391-01', 'RESE-0805-X-O393-01', 'RESE-0805-X-O394-01', 'RESE-0805-X-O402-01', 'RESE-0805-X-O432-01', 'RESE-0805-X-O433-01', 'RESE-0805-X-O470-01', 'RESE-0805-X-O471-01', 'RESE-0805-X-O473-01', 'RESE-0805-X-O474-01', 'RESE-0805-X-O47X-01', 'RESE-0805-X-O4992-01', 'RESE-0805-X-O499D-01', 'RESE-0805-X-O502-01', 'RESE-0805-X-O510-01', 'RESE-0805-X-O511-01', 'RESE-0805-X-O512-01', 'RESE-0805-X-O513-01', 'RESE-0805-X-O514-01', 'RESE-0805-X-O560-01', 'RESE-0805-X-O561-01', 'RESE-0805-X-O563-01', 'RESE-0805-X-O602-01', 'RESE-0805-X-O622-01', 'RESE-0805-X-O623-01', 'RESE-0805-X-O680-01', 'RESE-0805-X-O681-01', 'RESE-0805-X-O683-01', 'RESE-0805-X-O684-01', 'RESE-0805-X-O702-01', 'RESE-0805-X-O751-01', 'RESE-0805-X-O752-01', 'RESE-0805-X-O753-01', 'RESE-0805-X-O802-01', 'RESE-0805-X-O821-01', 'RESE-0805-X-O822-01', 'RESE-0805-X-O823-01', 'RESE-0805-X-O902-01', 'RESE-0805-X-O912-01', 'RESE-0805-X-O993-01', 'RESE-1206-X-O000-01', 'RESE-1206-X-O100-01', 'RESE-1206-X-O101-01', 'RESE-1206-X-O102-01', 'RESE-1206-X-O103-01', 'RESE-1206-X-O104-01', 'RESE-1206-X-O105-01', 'RESE-1206-X-O10X-01', 'RESE-1206-X-O121-01', 'RESE-1206-X-O181-01', 'RESE-1206-X-O200-01', 'RESE-1206-X-O202-01', 'RESE-1206-X-O205-01', 'RESE-1206-X-O220-01', 'RESE-1206-X-O301-01', 'RESE-1206-X-O702-01', 'RESE-1206-X-O751-01'])


######  Common
newPart.addTag('hexID',hexId)

######  Housekeeping
newPart = OOMPtags.addTags(newPart,oompId)
OOMP.parts.append(newPart)
