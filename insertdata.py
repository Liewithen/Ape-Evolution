#!/usr/bin/env python
# coding:utf-8

import os
import codecs
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Evolution.settings")
import django
django.setup()


import django

if django.VERSION >= (1, 7):
	django.setup()

def main():
	from breakthrough.models import DataBank1,DataBank2,DataBank3
	DataBank = []
	with codecs.open("1.txt", "r", "utf-8-sig") as f:
		for line in f:
			parts = line.split('*')
			DataBank.append(DataBank1(q_class=int(parts[0]),q_id=int(parts[1]),answer=parts[2],content=parts[3],option1=parts[4],option2=parts[5],option3=parts[6],option4=parts[7]))
	f.close()
	DataBank1.objects.bulk_create(DataBank)
	DataBank = []
	with codecs.open("2.txt", "r", "utf-8-sig") as f:
		for line in f:
			parts = line.split('*')
			DataBank.append(DataBank2(q_class=int(parts[0]),q_id=int(parts[1]),answer=parts[2],content=parts[3],option1=parts[4],option2=parts[5],option3=parts[6],option4=parts[7]))
	f.close()
	DataBank2.objects.bulk_create(DataBank)
	DataBank = []
	with codecs.open("3.txt", "r", "utf-8-sig") as f:
		for line in f:
			parts = line.split('*')
			DataBank.append(DataBank3(q_class=int(parts[0]),q_id=int(parts[1]),answer=parts[2],content=parts[3],option1=parts[4],option2=parts[5],option3=parts[6],option4=parts[7]))
	f.close()
	DataBank3.objects.bulk_create(DataBank)
if __name__ == "__main__":
	main()
	print ('Data Insert Successfully !')