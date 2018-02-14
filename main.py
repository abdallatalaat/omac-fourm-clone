from fourms import*

m_store = MemberStore()
for i in range(4):
    m_store.add(Member(i, "mem"+str(i), i+15))

p_store = PostStore()
for i in range(4):
    p_store.add(Post(i, "POST "+str(i), i+15))
