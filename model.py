#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import feedparser, gtk, datetime

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
		self.date = self.format_xml_unicode_date_to_datetime_date(date)
		
	def format_xml_unicode_date_to_datetime_date(self, xml_unicode_date):
		list_date = xml_unicode_date.split(' ')
		
		Month = {
			'Jan' : 1,
			'Feb' : 2, 'Fev' : 2,
			'Mar' : 3,
			'Apr' : 4,
			'May' : 5,
			'Jun' : 6,
			'Jul' : 7,
			'Aug' : 8,
			'Sep' : 9,
			'Oct' : 10,
			'Nov' : 11,
			'Dec' : 12	
		}
		
		# try:
		# 	self.date = datetime.date(list_date[0], Month[list_date[1]], list_date[2])
		# except ValueError:
		# 	self.date = datetime.date(list_date[1], Month[list_date[2]], list_date[3])

		# When feed dates has the week day as first item, the index should be 1 instead 0; that way ingnoring the week day
		index = [1 if len(list_date) == 6 else 0]
			
		year = list_date[index]
		month = Month[list_date[index+1]]
		day = list_date[index+2]
		
		list_time = list_date[index+3].split(':')
		
		hour = list_time[0]
		minute = list_time[1]
		second = list_time[2]
		
		date = datetime.datetime(year, month, day, hour, minute, second)
		return date

