import requests
import os

class website():
    def __init__(self,website,webContent):
        self.website = website
        self.websiteContent = webContent.content
        self.websiteLen = len(str(webContent.content))


    def createHtmlfile(self):
            open('index.html.', 'wb').write(self.websiteContent)
            print(self.websiteLen)
            print(self.websiteContent)

    def createCssfiles(self):

        f = str(self.websiteContent)
        x = self.checkEqual(0)
    def checkEqual(self,x):

        f = str(self.websiteContent)

        while x <  self.websiteLen:
            if f[x : x+4] == ".css":
                self.findCssname(x)
            x = x+1

    def findCssname(self,css):

        cssName = css
        f = str(self.websiteContent)
        while css > 0:
            if f[css : css+4] == "http":
                return 0
            if f[css : css+2] =="//":
                return 0
            if f[css] =="}":
               return 0

            elif f[css] == "=":
                r = cssName - css
                r = r+css
                if f[r+1] == "c":
                    g = 0
                    while g < 30:
                        g = g+1
                        if f[r+g] == ">":
                            self.createCssFile(r)
                            return 0

            css = css - 1
    def createCssFile(self,r):
        cssName = []
        x =0
        z = 0
        f = str(self.websiteContent)
        while r > x:
            if f[r] == "=":
                cssName1 = ''
                r1 = r
                while r1 < r1+1:
                    r1 = r1+1
                    cssName.append([f[r1]])
                    cssName1 = cssName1 + ''.join(cssName[z])
                    z = z+1
                    if f[r1 : r1+4] == ".css":
                        self.createCssFoldr(cssName1)
                        return 0



            r =r-1

    def createCssFoldr(self,folder):
        foldery = []
        folder13 = []
        folderLn = len(folder)
        while folderLn > 0:
            folderLn = folderLn -1
            if folder[folderLn]=="/":
             foldery.append(folder[folderLn])
            if folder[folderLn]==".":
             foldery.append(folder[folderLn])
            if folder[folderLn]=="-":
             foldery.append(folder[folderLn])
            if folder[folderLn]=="_":
             foldery.append(folder[folderLn])
            if folder[folderLn]==",":
             foldery.append(folder[folderLn])
            if folder[folderLn] =="0" or folder[folderLn]=="1" or folder[folderLn]=="2" or folder[folderLn]=="3" or folder[folderLn]=="4" or folder[folderLn]=="5" or folder[folderLn]=="6" or folder[folderLn]=="8" or folder[folderLn] == "9":
             foldery.append(folder[folderLn])
            if folder[folderLn].islower() != folder[folderLn].isupper():
                foldery.append(folder[folderLn])
        for e in reversed(foldery):
            folder13.append(e)
            folder14 =''.join(folder13)
        print(folder14)
        if "/" not in folder14:
            webContent = requests.get(self.website+"/"+folder14+"css")
            open(folder14+"css", 'wb').write(webContent.content)
            return 0
        else:
            if folder14[0] =="/":
                folder14 =''.join(folder14.split('/', 1))

            folder14 = folder14+"css"
            os.makedirs(os.path.dirname(folder14), exist_ok=True)
            with open(folder14, "w") as f:
                webContent = requests.get(self.website+"/"+folder14)
                f.write(str(webContent.content))
                return 0
    def javaScriptfiles(self):
        f = str(self.websiteContent)
        x = self.checkEqual1(0)

    def checkEqual1(self,x):
         f = str(self.websiteContent)

         while x <  self.websiteLen:
            if f[x : x+3] == ".js":
               self.findJavascriptName(x)
            x = x+1
    def findJavascriptName(self,java):

        cssName = java
        f = str(self.websiteContent)
        while java > 0:
            if f[java : java+4] == "http":
                return 0
            if f[java : java+2] =="//":
                return 0
            elif f[java] == "=":
                r = cssName - java
                r = r+java
                if f[r+1] == "j":

                    g = 0
                    while g < 10:
                        g = g+1
                        if f[r+g] == ">":
                            self.createJavaFile(r)
                            return 0
            java = java - 1

    def createJavaFile(self,r):
      cssName = []
      x =0
      z = 0

      f = str(self.websiteContent)
      while r > x:
        if f[r] == "=":
            cssName1 = ''
            r1 = r
            while r1 < r1+1:
                r1 = r1+1
                cssName.append([f[r1]])
                cssName1 = cssName1 + ''.join(cssName[z])
                z = z+1
                if f[r1+1 : r1+3] == "js":
                    if f[r1+3] == "o":
                        return 0
                    else:
                        self.createJavaFoldr(cssName1)
                        return 0

        r =r-1

    def createJavaFoldr(self,folder):


        foldery = []
        folder13 = []
        folderLn = len(folder)
        while folderLn > 0:
            folderLn = folderLn -1
            if folder[folderLn]=="/":
                foldery.append(folder[folderLn])
            if folder[folderLn]==".":
                foldery.append(folder[folderLn])
            if folder[folderLn]=="-":
                foldery.append(folder[folderLn])
            if folder[folderLn]=="_":
                foldery.append(folder[folderLn])
            if folder[folderLn]==",":
                foldery.append(folder[folderLn])
            if folder[folderLn] =="0" or folder[folderLn]=="1" or folder[folderLn]=="2" or folder[folderLn]=="3" or folder[folderLn]=="4" or folder[folderLn]=="5" or folder[folderLn]=="6" or folder[folderLn]=="8" or folder[folderLn] == "9":
                foldery.append(folder[folderLn])
            if folder[folderLn].islower() != folder[folderLn].isupper():
                foldery.append(folder[folderLn])
        for e in reversed(foldery):
            folder13.append(e)
            folder14 =''.join(folder13)
        if "/" not in folder14:
            webContent = requests.get(self.website+"/"+folder14+"js")
            open(folder14+"js", 'wb').write(webContent.content)
        else:
            if folder14[0] =="/":
                folder14 =''.join(folder14.split('/', 1))

            folder14 = folder14+"js"
            os.makedirs(os.path.dirname(folder14), exist_ok=True)
            with open(folder14, "w") as f:
                webContent = requests.get(self.website+"/"+folder14)
                f.write(str(webContent.content))

websiteName = "https://bankofamerica.com"
webContent = requests.get(websiteName)
website = website(websiteName,webContent)
website.createHtmlfile()
website.createCssfiles()
website.javaScriptfiles()
