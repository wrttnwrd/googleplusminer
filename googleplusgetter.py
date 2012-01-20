import os
import simplejson
import httplib
from datetime import *

apiurl = "www.googleapis.com"
idlist = [117045937808371931146,112707199408484711520,100000772955143706751,114474252347218597235,104629412415657030658,112599748506977857728,117962666888533781522,115040231829422107651,110717292631787068538,103533326117556337218,100021025784352405813,113756014567052941747,118177189004466545044,102150693225130002912,101261243957067319422,111294201325870406922,113217924531763968801,102150693225130002912,115675748062237570841,115777169768345614675,102261756656790911682,117663015413546257905,118216759969087724610,111717275116289870961,111667704476323287430]

print "theid","\t","verb","\t","author","\t","authorID","\t","title","\t","url","\t","reshares","\t","replies","\t","plusones","\t","content","\t", "pdate"

for theid in idlist:
	requesturl = "/plus/v1/people/" + str(theid) + "/activities/public?fields=items(actor(displayName,id),annotation,crosspostSource,id,kind,object(actor/id,attachments(content,displayName,image/url,objectType),content,objectType,originalContent,plusoners,replies,resharers,url),placeId,placeName,placeholder,published,title,updated,url,verb),kind&key=AIzaSyB821z11J56ZrmbH9F7mzQybuZqUSBSS2M"
	requesturl = str(requesturl)
	conn = httplib.HTTPSConnection(apiurl)
	conn.request("GET",requesturl)
	res = conn.getresponse()
	foo = res.read()
	conn.close()
	#print foo
	data = simplejson.loads(foo)
	items = data["items"]
	for d in items:
		kind = d["kind"]
		kind = kind.strip()
		kind = kind.replace("\r\n","")
		title = d["title"]
		title = title.strip()
		title = title.replace("\r\n","")
		title = title.replace("\r","")
		title = title.replace("\n","")
		url = d["url"]
		url = url.strip()
		verb = d["verb"]
		verb = verb.strip()
		verb = verb.replace("\r\n","")
		reshares = d["object"]["resharers"]["totalItems"]
		author = d["actor"]["displayName"]
		authorID = d["actor"]["id"]
		pdate = d["published"]
		replies = d["object"]["replies"]["totalItems"]
		plusones = d["object"]["plusoners"]["totalItems"]
		try:
			content = d["object"]["attachments"]
			content = content[0]["content"]
			content = content.replace("\r\n","")
			content = content.replace("\r","")
			content = content.replace("\n","")
			content = content.strip()
		except KeyError:
			content = " "
	#	try:
	#		content = d["object"]["attachments"]["content"]
	#	except:
	#		content = " "
		print theid,"\t",verb,"\t",author,"\t",authorID,"\t",title,"\t",url,"\t",reshares,"\t",replies,"\t",plusones,"\t",content,"\t", pdate
