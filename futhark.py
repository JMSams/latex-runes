runes = [
    ("ᚠ", "f"),
    ("ᚢ", "u"),
    ("ᚦ", "\\th"),
    ("ᚭ", "A"),
    ("ᚱ", "r")
]

with open("unicoderunes.sty", "w") as f:
	f.write("\\usepackage[utf8]{inputenc}\n\\usepackage{newunicodechar}\n\n\\usepackage{allrunes}\n\n")
	
	for rune, tex in runes:
		f.write("\\newunicodechar{{{0}}}{{\\textarn{{{1}}}}}\n".format(rune, tex))
	f.write("\n\n\\newcommand{\\allrunes}{")
	for rune, tex in runes:
		f.write(rune)
	f.write("}\n")
