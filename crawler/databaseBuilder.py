import sys
sys.path.append('..')
import helpers
log = helpers.log
from fileIO import FileIO
from mongoengine import *
from mongoConfig import *
import math

connect('chefmateDB', host='18.222.251.5', port=27017)

class DatabaseBuilder:
  docCount = 0

  def __init__(self, domain, mode='DEV'):
    self.domain = domain
    self.mode = mode
  
  def build(self):
    filePath = 'domains/'+self.domain +'/'+self.domain+"_index.txt" 

    rawData = FileIO.readJsonFile(filePath)
    count=0
    for entry in rawData.keys():
      count+=1
      doc = rawData[entry]
      if doc['title'] == None:
        doc['title']='No Title'
      self.addDocumentToCollection(docId=doc['docId'], url=entry, title=doc['title'], body=doc['body'])
      self.buildInvertedIndex(doc['body'], entry)

      if self.mode=='DEV' and count>=10:
        break

 
  def buildRawText(self, printStatements=False):
    filePath = 'domains/'+self.domain +'/'+self.domain+"_index.txt" 

    file = open(filePath, 'r')
    for line in file:
      if line == "\n":
        continue
      docID = line
      link = file.readline()
      title = file.readline()
      body = file.readline()

      docID = docID[7:len(docID)-1]
      link = link[6:len(link)-1]
      title = title[7:len(title)-1]
      body = body[6:len(body)-1]

      self.addDocumentToCollection(docID, link, title, body)
      if printStatements:
        log('entry', docID)
        log('entry', link)
        log('entry', title)
        log('entry', body)
  
  def addDocumentToCollection(self, docId, url, title, body):
    log("new entry", "Adding "+url+" to collection.")
    crawlerDoc = Crawler(url=url, title=title, body=body, docId=docId)
    crawlerDoc.save()
    DatabaseBuilder.docCount+=1
    
  def buildInvertedIndex(self, body, url):
    termPos = 0
    for term in body:
      termPos += 1
      try:
        termEntry = InvertedIndex.objects.get(term=term)
        log('update entry', "Updating InvertedIndex entry for \'"+term+"\'.")
        hasDoc = False

        for i in range(0, len(termEntry.doc_info)):
          doc = termEntry.doc_info[i]
          if doc['url'] == url:
            hasDoc=True
            termEntry.doc_info[i]['termCount']+=1
            termEntry.doc_info[i]['pos'].append(termPos)
            break

        if not hasDoc:
          termEntry.doc_info.append({'url':url, 'termCount': 1, 'pos':[termPos]})
        termEntry.save()

      except DoesNotExist:
        log('new entry', 'Creating InvertedIndex entry for \''+term+'\'.')
        newTermEntry = InvertedIndex(term=term, 
        doc_info=[{
          'url': url,
          'termCount': 1,
          'pos':[termPos]
        }],
        tfidf={}
        )
        newTermEntry.save()

      if self.mode=='DEV' and termPos>=50:
        break

  @staticmethod
  def calculateIDF():
    terms = InvertedIndex.objects()
    for termEntry in terms:
      docsContaining = float(len(termEntry.doc_info))
      termEntry['idf'] = math.log(DatabaseBuilder.docCount / docsContaining, 2)
      log('update idf', termEntry['term']+"= "+str(termEntry['idf']))
      termEntry.save()

if __name__ == "__main__":
  d = DatabaseBuilder('EpiCurious')
  d.build()
  calculateIDF(20)
  # terms = InvertedIndex.objects()
        
