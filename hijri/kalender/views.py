# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests
import datetime
from bs4 import BeautifulSoup

# Create your views here.
def index(request):
	template = loader.get_template('kalender/index.html')
	url = 'https://calendar.zoznam.sk/islamic_calendar-en.php'
	response = requests.get(url)
	html = response.content

	soup = BeautifulSoup(html, 'html.parser')
	tanggalan = soup.find(id='headline21')
	a = ' '.join(str(tanggalan).split())
	t = str(tanggalan).split()
	hari = t[2].strip('.')
	bulan = t[3]
	tahun = t[4].strip('</div>') + ' H'

	system_hari = datetime.datetime.now().strftime ("%A")
	system_tanggal = datetime.datetime.now().strftime ("%d")
	system_bulan = datetime.datetime.now().strftime ("%B")
	system_tahun = datetime.datetime.now().strftime ("%Y")
	context = {
		'hari' : hari,
		'bulan' : bulan,
		'tahun' : tahun,
		'system_hari' : system_hari,
		'system_tanggal' : system_tanggal,
		'system_bulan' : system_bulan,
		'system_tahun' : system_tahun,
	}
	return HttpResponse(template.render(context, request))