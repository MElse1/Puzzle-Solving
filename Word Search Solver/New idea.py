import pytesseract

word_search = pytesseract.image_to_string("C:\\Users\\elseh\\OneDrive\\Pictures\\Screenshots\\Word Search.png") #function to OCR the word search
print(word_search)