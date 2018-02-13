from fourms import models as m

mem0 = m.Member(0, "mem0", 13)
mem1 = m.Member(1, "mem1", 34)
mem2 = m.Member(2, "mem2", 23)
for i in range(10):
    mem0.new_post(i, "POST TITLE", "POST CONTENT")

print mem0.posts[0]
