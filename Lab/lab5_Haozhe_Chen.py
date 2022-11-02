"""
#Sorry professor, but i dont have any idea about today's lab.
#I even don't remember are we study that part before.
#Sorry about that.

"""





from dataclasses import replace


# def main():
	
# 	DecodeWord()




#Your code goes here.

def DecodeWord():
	encodedWord = "WBLARF8TTS"
	#encodedWord = "L8KAOUL"
	#encodedWord = "E8N8N8"
	#encodedWord = "8TRA8DY T8LA"
	#encodedWord = "8TT LHA TILLTA LIMAS"	
	#encodedWord = "LHA GRAAN FIATD GTA8MS IN LHA W8RM SUNEABMS"
	#encodedWord = "TONG T8E T8CKS L8SLY L8CO LIMA 8L TA8SL T8LATY"
	
	
	
	#encodedWord = "UUHO"  		#Used for Bonus
	#encodedWord = "EOUUUUOUU" 	#Used for Bonus
	
	#LOOP 
	for i in encodedWord:
		i.replace("L","T")
		i.replace("T","L")
		i.replace(8,"A")
		i.replace("B","A")
		i.replace("A","E")
		i.replace("E","A")
	print(i)





#This code triggers the main to run
# we'll talk about this more in chapters 6,7, & 8.	
# if __name__ == "__main__":
# 	main()
