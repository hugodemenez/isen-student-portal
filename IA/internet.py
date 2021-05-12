query='iron man'

site=['&oq=&gs_l=psy-ab.1.2.35i39l6.0.0..10558...2.0..0.318.318.3-1......0......gws-wiz.....6.X_oDmQRq4Zo']
site.append(query)
site.append('https://www.google.com/search?source=hp&ei=rrTSXKHVKtOHjLsP_4GQuAo&q=')
site2=site[2]+site[1]+site[0]


webbrowser.open(site2)


