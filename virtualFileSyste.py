data={
    "a/a":"xyz",
}

class Dict:
    data=[]
    mapId=[]
    lastid=0
    def __init__(self,data):
        self.data=data
        self.initData()
    def initData(self):
        key=self.data.keys()
        #creating main data file
        for i in key:
            dataM=self.data[i]
            columns=i.split("/")
            for i in range(0,len(columns)):
                a={}
                if i+1<len(columns):
                    a={
                        "path":columns[:i],
                        "name":columns[i],
                        "type":"d"
                    }
                else:
                    a={
                        "path":columns[:i],
                        "name":columns[i],
                        "type":"f",
                        "data":dataM
                    }
                if a not in self.mapId:
                    self.mapId.append(a)
        #create id
        ide=0
        for i in self.mapId:
            i["id"]=ide
            ide+=1
        self.lastid=ide
        for i in self.mapId:
            row=i["path"]
            path="/"
            if len(row)==0:
                path=""
            for j in range(0,len(row)):
                if(j+1<len(row)):
                    path=path+row[j]+"/"
                else:
                    path=path+row[j]
            i["path"]=path

        for i in self.mapId:
            if "child" not in i.keys():
                if i["type"]=="d":
                    i["child"]=[]
            for j in self.mapId:
                if(i["path"]+"/"+i["name"]==j["path"]):
                    i["child"].append(j["id"])
                    j["parent"]=i["id"]
    def printData(self):
        print("\n\n")
        for i in self.mapId:
            if i["type"]=="d":
                print("id     :",i["id"])
                print("type   : Dictionary")
                print("path   :",i["path"])
                print("name   :",i["name"])
                print("child  :",i["child"])
                if "parent" in i.keys():
                    print("parent :",i["parent"])
            else:
                print("id     :",i["id"])
                print("type   : file")
                print("path   :",i["path"])
                print("name   :",i["name"])
                if "parent" in i.keys():
                    print("parent :",i["parent"])
                print("data   :",i["data"])
            print("\n")
        print("\n\n")
    def deleteById(self,ide):
        for i in self.mapId:
            if i["id"]==ide:
                if i["type"]=="d":
                    while(len(i["child"])>0):
                        self.deleteById(i["child"][0])
                    self.mapId.remove(i)
                else:
                    for k in self.mapId:
                        if k["id"]==i["parent"]:
                            k["child"].remove(i["id"])
                    self.mapId.remove(i)
    def createFile(self,name,content,path):
        a={
            "name":name,
            "type":"f",
            "id":self.lastid,
            "path":path,
            "data":content
        }
        if path=="":
            self.mapId.append(a)
            self.lastid+=1
            return True
        if(not (self.getParentId(path) == -1)):
            a["parent"]=self.getParentId(path)
            self.setChildIdinParent(path,self.lastid)
            self.mapId.append(a)
            self.lastid+=1
            return True
        else:
            return False,"path not found"
    def getParentId(self,path):
        for i in self.mapId:
            if((i["path"]+"/"+i["name"])==path):
                return i["id"]
        return -1
    def setChildIdinParent(self,path,ide):
        for i in self.mapId:
            if((i["path"]+"/"+i["name"])==path):
                i["child"].append(ide)
    def getDictINPath(self,ide):
        for i in self.mapId:
            if(i["id"]==ide and i["type"]=="d"):
                return (i["path"]+"/"+i["name"])
        return -1
    def createDictionary():
        return 0
myObject=Dict(data)
myObject.printData()
myObject.createFile("a","nm\r","")
myObject.printData()








