#libraries3
#type libraries:
# 1-    module :single file ,os
# 2-    package: اكثرمن module more than file 
        #librarie :تشمل الاثنين مع بعض module or package

#انوع المكتبات التي تنزل مع بايثون
#+600 عدد المكتبات التي تنزل مع بايثون

    #-internal : داخلية وتنزل مع بايثون :import تستخدم على طول
    #-extetnal : user defined الخارجية التي تعرفها المستخدم : install + import تسطيب وبعدين استخدام

#طريقة استدعاء المكتبة library call method:
# -import
        #  1 : import os
             # os.mkdir('test')
             # os.chdir('/')
             # وتعتبر افضل طريقة اذا كنت تستخدم مكاتب كثيره
             #لديها عيوب ولكن الحل للعيوب الاسماء الطويلة وهو عمل اختصار لتسميتها
             #import beatutifulsoup4 as bs4
             #import numpy as np
             #import pandas as pd


        #  2 : from os import mkdir , chdir , getcwd 
             # mkdir('test')
             #مفضلة ايضا في حال كنت مستدعي مكاتب محدده
             

        #  2 : from os import *
             # mkdir('')
             # getcwd()
             # chdir()
             #ليست مفضلة لكنها تستدعى جميع المكتبات
