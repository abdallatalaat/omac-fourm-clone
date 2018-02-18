from fourms import models
from fourms import store
m_store = store.MemberStore()
for i in range(4):
    m_store.add(models.Member("mem"+str(i), i+15))

p_store = store.PostStore()
for i in range(4):
    p_store.add(models.Post("POST "+str(i), i+15))
