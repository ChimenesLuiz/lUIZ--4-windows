def worldcuptitles(country, *args):
    print(f"Country: {country}")
    for title in args:  print(f"Year: {title}")
worldcuptitles("Brasil", "2002 ", "2003", "2004", "2005")