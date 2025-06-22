
# role base access control 

# authentication
# authentication matlab user ko login karwana ke matlab ke kisi website pe jake login kiya to aap authenticated ho 
# aur authentication karne ke liye ek login system hona chahiye aur login system ke bohot sare types hote he for exp authenticate with google,authenticate with auth,authenticate with email password,authenticate with magic link authentication


# autherization
# kisi cheez ko use karne ki authority hona usi ko autherization bolte he


# autherization patterns

# jese ek bloging website he uspe blog vo hi add aur delete kar sakta he jiska bhi role admin ho aur ek role editor he to jiska bhi role editor hoga vo sirf edit kar sakta he nake add aur delete 
# aur jiska role user hoga vo sirf dekh sakta he 
# isiko role base access control (RBAC) bolte he


# facebook pe aapne ek js developers group banaya jiske andar aap admin jiske andar aur memebres add kar skate he member is group me post kar skate he aur iske andar kitni post aap use delete kar sakte ho taki aap admin ho iske andar jo members he vo bas psot kar sakte he
# aur facebook pe ek aur group he python developers name se jispe aap sirf member ho to aap sirf post kar sakte he


# fine grained base access control
# ye hota he jese aaki bloging website he jispe aap admin ho aur usme bohot sare users he aur aapne ek user ko admin nbana diya aur user ko mderator bana diya to usi ko fine grained base access control bolte he


# attribute base access control

# aapne ek blog banaya aur usme aapne ek attribute daal diya marketing name se to marketing team ke editors  he bas ho hi is blog ko edit kar sakte he 
# aur aapne ek aur blog banaya aur aapne isko attribute de diya dev to dev team ke members hi isko dekh sakte he marketing team ke members nahi dekh sakte
# aur aapne ek aur blog banaya aur aapne isko attribute de diya dev aur marketing to dono team ke members isko dekh sakte he
# aur is tarike se attribute dete he attribute:[dev,marketing]
# isi ko attribute base access control bolte he


# relationship base access control (Rebac)

# iske andar 2 types ke access hote he direct access aur parent base access 
# jese ek file he aur user1 he aur user2 he  
# aur user1 ke paas direct access he file ka 
# aur jo user2 he uske paas file ke folder ka bhi jo folder he uska access he to isse parent base access bolenge
# aur in sab ko relationship base access control bolte he














