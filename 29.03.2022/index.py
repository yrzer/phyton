import matplotlib.pyplot as plt

labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')


z = ["Unia\nEuropejska","Włochy","Węgry","Szwecja","Słowenia","Słowacja","Rumunia","Portugalia","Polska","Niemcy","Malta","Łotwa","Luksemburg","Litwa","Irlandia","Holandia","Hiszpania","Grecja","Francja","Finlandia","Estonia","Dania","Czechy","Cypr","Chorwacja","Bułgaria","Belgia","Austria"]
w = [14824756,1672438,112399,462057,39769,80958,169578,184931,424269,3134070,9898,25021,54195,38637,265835,697219,1113851,175888,2228857,214062,20916,276805,174412,17901,45557,47364,421611,349344]

plt.rcdefaults()
fig, ax = plt.subplots()
ax.barh(z, w, xerr=len(z) )


plt.show()
