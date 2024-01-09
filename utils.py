def year_classification (year):
    if year < 1970 :
        return "1960-1970"
    elif year < 1980 :
        return "1970-1980"
    elif year < 1990 :
        return "1980-1990"
    elif year < 2000 :
        return "1990-2000"
    elif year < 2010 :
        return "2000-2010"
    elif year < 2020 :
        return "2010-2020"
    else :
        return None
    
