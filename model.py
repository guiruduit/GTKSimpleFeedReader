import feedparser, gtk

class Feader(object):

	feeds = []

	def __init__(self, url):
		self.url = url
		parsedfeed = feedparser.parse(self.url)
		self.title = parsedfeed.channel.title
		self.format_feeds(parsedfeed.entries)

	def format_feeds(self, xml_feeds):
		self.feeds = xml_feeds
		index = 0
		for feed in self.feeds:
			self.feeds[index] = Feed(self.title, feed.title, feed.description, feed.link, feed.date)
			index = index + 1

	def reset(self):
		parsedfeed = feedparser.parse(self.url)
		self.format_feeds(parsedfeed.entries)
	
	def get_feeds(self):
		return self.feeds

	def get_feeds_titles(self):
		list_feeds_titles = []
		for feed in self.feeds:
			list_feeds_titles.append(feed.title)
		return list_feeds_titles

class Feed(object):

	def __init__(self, feader_title, title, description, link, date):
		self.feader_title = feader_title
		self.title = (title + ' | date: ' + date + ' | ' + feader_title)
		self.description = description
		self.link = link
		self.date = date
